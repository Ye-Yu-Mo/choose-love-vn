#!/usr/bin/env python3
"""批量出图：读 manifest，线程池并发请求 gpt-image-2，失败重试。

用法：
  python3 tools/gen_images.py --manifest assets/characters_manifest.json \
      --out assets/characters --jobs 3

manifest 格式：
[
  {"name": "shen_lan_sheet", "prompt": "...", "size": "1536x1024"},
  ...
]
"""
import argparse
import base64
import json
import os
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

API = "https://llm-proxy.ftai.chat/v1/images/generations"
PROXY = "http://127.0.0.1:7890"


def generate(job, out_dir, retries=4):
    token = os.environ.get("ANTHROPIC_AUTH_TOKEN")
    if not token:
        return job["name"], None, "ANTHROPIC_AUTH_TOKEN 未设置"
    body = {
        "model": job.get("model", "gpt-image-2"),
        "prompt": job["prompt"],
        "n": 1,
        "size": job.get("size", "1536x1024"),
    }
    for key in ("background", "output_format", "quality"):
        if job.get(key):
            body[key] = job[key]
    data = json.dumps(body).encode()
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"https": PROXY, "http": PROXY})
    )
    start = time.time()
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(
                API,
                data=data,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                },
            )
            with opener.open(req, timeout=300) as resp:
                payload = json.load(resp)
            item = payload["data"][0]
            if not item.get("b64_json"):
                raise RuntimeError(f"no b64_json: {str(payload)[:200]}")
            path = os.path.join(out_dir, job["name"] + ".png")
            with open(path, "wb") as f:
                f.write(base64.b64decode(item["b64_json"]))
            return job["name"], path, round(time.time() - start, 1)
        except Exception as exc:  # noqa: BLE001 - 批量任务要容错
            last_err = exc
            if attempt < retries:
                time.sleep(1.5 * attempt)
    return job["name"], None, f"失败 {retries} 次: {last_err}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--jobs", type=int, default=3)
    args = parser.parse_args()

    with open(args.manifest, "r", encoding="utf-8") as f:
        jobs = json.load(f)
    os.makedirs(args.out, exist_ok=True)

    started = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(generate, job, args.out): job for job in jobs}
        for future in as_completed(futures):
            name, path, info = future.result()
            results.append((name, path, info))
            print(f"{name}: {path or '-'} ({info}s)" if path else f"{name}: {info}")

    ok = sum(1 for _, path, _ in results if path)
    print(f"\n完成 {ok}/{len(results)}，总耗时 {round(time.time() - started, 1)} 秒")


if __name__ == "__main__":
    main()
