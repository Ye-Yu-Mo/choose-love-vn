#!/usr/bin/env python3
"""批量表情差分：用参考立绘走 /v1/images/edits，线程池并发。

manifest:
[
  {"name": "...", "ref": "game/images/sprites/xiaoman_neutral_half.png",
   "prompt": "Same character...", "size": "1024x1536"}
]
"""
import argparse
import base64
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

API = "https://llm-proxy.ftai.chat/v1/images/edits"
PROXY = "http://127.0.0.1:7890"


def generate(job, out_dir, retries=3):
    token = os.environ.get("ANTHROPIC_AUTH_TOKEN")
    if not token:
        return job["name"], None, "ANTHROPIC_AUTH_TOKEN 未设置"
    start = time.time()
    last_err = None
    for attempt in range(1, retries + 1):
        cmd = [
            "curl", "-s", "--max-time", "300", "-x", PROXY, API,
            "-H", f"Authorization: Bearer {token}",
            "-F", "model=gpt-image-2",
            "-F", f"image=@{job['ref']}",
            "-F", f"prompt={job['prompt']}",
            "-F", f"size={job.get('size', '1024x1536')}",
            "-F", "output_format=png",
        ]
        if job.get("transparent", True):
            cmd += ["-F", "background=transparent"]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=320)
            payload = json.loads(res.stdout)
            if "error" in payload:
                raise RuntimeError(str(payload["error"])[:200])
            item = payload["data"][0]
            if not item.get("b64_json"):
                raise RuntimeError("no b64_json")
            path = os.path.join(out_dir, job["name"] + ".png")
            with open(path, "wb") as f:
                f.write(base64.b64decode(item["b64_json"]))
            return job["name"], path, round(time.time() - start, 1)
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            if attempt < retries:
                time.sleep(2 * attempt)
    return job["name"], None, f"失败: {last_err}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--jobs", type=int, default=3)
    args = parser.parse_args()

    jobs = json.load(open(args.manifest, encoding="utf-8"))
    os.makedirs(args.out, exist_ok=True)
    started = time.time()
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(generate, j, args.out): j for j in jobs}
        for future in as_completed(futures):
            name, path, info = future.result()
            print(f"{name}: {path or '-'} ({info}s)" if path else f"{name}: {info}")
    print(f"\n总耗时 {round(time.time() - started, 1)} 秒")


if __name__ == "__main__":
    main()
