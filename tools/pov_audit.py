#!/usr/bin/env python3
"""POV 审核：只找旁白里的「我/他/她」视角错误，不改文风。"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from polish_dialogue import API, DIALOGUE_RE, PROXY, dialogue_lines, sections  # noqa: E402

PROMPT = """你是视觉小说 POV 审核员。只找视角错误，不改文风。
规则：
- 在 `if pov == "luyao":` 分支里：叙述者「我」=陆遥；沈岚=她；陆遥=我。
- 在 `else:`（沈岚视角）里：叙述者「我」=沈岚；陆遥=他；沈岚=我。
- 注意：对白里的「我」是说话人自己，不要把对白算错。
- 找出：叙述旁白把「我/他/她」用错；沈岚视角却写了陆遥的内心/感官；陆遥视角却写了沈岚的内心/感官。
只输出有问题的行，最多 10 条。没有就输出空数组。
输出 JSON：{"issues":[{"i":行号,"old":"原句","why":"一句话原因","t":"建议改法"}]}。不要 markdown。
"""


def call(model, prompt):
    token = os.environ.get("FT_API_KEY")
    body = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 6000,
        },
        ensure_ascii=False,
    )
    last = None
    for attempt in range(1, 4):
        res = subprocess.run(
            [
                "curl",
                "-s",
                "--max-time",
                "300",
                "-x",
                PROXY,
                API,
                "-H",
                f"Authorization: Bearer {token}",
                "-H",
                "Content-Type: application/json",
                "-d",
                body,
            ],
            capture_output=True,
            text=True,
        )
        try:
            data = json.loads(res.stdout)
            content = data["choices"][0]["message"]["content"].strip()
            content = re.sub(r"^```(?:json)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content)
            return json.loads(content)
        except Exception as exc:  # noqa: BLE001
            last = f"{exc}: {res.stdout[:300]}"
            if attempt < 3:
                time.sleep(2 * attempt)
    raise RuntimeError(f"{model} 调用失败: {last}")


def audit(path, lines, start, end, label, model, out_root):
    ids = dialogue_lines(lines, start, end)
    if not ids:
        return label, []
    src = "\n".join(
        (f"[[D{n}]] " if n in ids else "       ") + lines[n - 1]
        for n in range(start, end + 1)
    )
    prompt = f"{PROMPT}\n文件：{path}\n段落：{label}（{start}-{end}）\n\n{src}"
    payload = call(model, prompt)
    issues = payload.get("issues", [])
    if not isinstance(issues, list) or len(issues) > 10:
        raise RuntimeError(f"issues 数量异常: {len(issues) if isinstance(issues, list) else issues}")
    valid = []
    for it in issues:
        try:
            i = int(it["i"])
            if i not in ids:
                continue
            old = DIALOGUE_RE.match(lines[i - 1]).group(3)
            new = str(it.get("t", "")).strip()
            if new.startswith('"') and new.endswith('"') and len(new) >= 2:
                new = new[1:-1].strip()
            m = re.match(r'^[A-Za-z_]\w*\s+"(.*)"$', new)
            if m:
                new = m.group(1).strip()
            if not new or '"' in new or "\n" in new:
                continue
            valid.append({"i": i, "old": old, "why": str(it.get("why", "")), "t": new})
        except Exception:  # noqa: BLE001
            continue
    out_dir = out_root / Path(path).stem / f"pov-{model}"
    out_dir.mkdir(parents=True, exist_ok=True)
    safe = label.replace(":", "_").replace(" ", "_")
    (out_dir / f"{safe}.json").write_text(
        json.dumps(valid, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return label, valid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default="docs/polish")
    ap.add_argument("--only", help="只处理 label 包含这个字符串的段落")
    args = ap.parse_args()
    lines, secs = sections(args.path)
    if args.only:
        secs = [s for s in secs if args.only in s[2]]
    total = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(audit, args.path, lines, s, e, label, args.model, Path(args.out)): label
            for s, e, label in secs
        }
        for fut in as_completed(futures):
            label = futures[fut]
            try:
                _, issues = fut.result()
                total += len(issues)
                print(f"[{label}] {len(issues)} 条", flush=True)
                for it in issues:
                    print(f"  {it['i']}: {it['old']} -> {it['t']}  ({it['why']})", flush=True)
            except Exception as exc:  # noqa: BLE001
                print(f"[{label}] 失败: {exc}", flush=True)
    print(f"共 {total} 条")


if __name__ == "__main__":
    sys.exit(main())
