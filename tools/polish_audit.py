#!/usr/bin/env python3
"""定点润色：让模型只挑每场最需要改的 3-6 行，避免全篇重写。

用法:
  python3 tools/polish_audit.py game/script.rpy --model claude-opus-5-5
  python3 tools/polish_audit.py game/script.rpy --model claude-opus-5-5 --apply
"""
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
from polish_dialogue import (  # noqa: E402
    API,
    DIALOGUE_RE,
    PROXY,
    STYLE,
    apply,
    dialogue_lines,
    sections,
)

AUDIT = """你是终审编辑。只找出这场戏里最需要改的 3-6 行：视角错了、解释太多、句子太整齐、重复同一个口头禅、或者不像这个角色会说的话。
已经好的句子不要动。不要为了改而改。每行给一句很短的原因。
不要写性内容、安全词、羞耻表达。
"""


def call(model, prompt):
    token = os.environ.get("FT_API_KEY")
    if not token:
        raise RuntimeError("FT_API_KEY 未设置")
    body = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.4,
            "max_tokens": 3000,
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


def audit_section(path, lines, start, end, label, model, out_root):
    ids = dialogue_lines(lines, start, end)
    if not ids:
        return label, {}
    src = "\n".join(
        (f"[[D{n}]] " if n in ids else "       ") + lines[n - 1]
        for n in range(start, end + 1)
    )
    prompt = (
        STYLE
        + AUDIT
        + f"\n文件：{path}\n段落：{label}（第 {start}-{end} 行）\n\n{src}\n\n"
        + '只输出 JSON：{"notes":[{"i":行号,"t":"建议改成的台词","why":"一句话原因"}]}。没有需要改的就输出 {"notes":[]}。不要输出 markdown。'
    )
    payload = call(model, prompt)
    notes = payload.get("notes", [])
    if not isinstance(notes, list):
        raise RuntimeError("notes 不是数组")
    if len(notes) > 8:
        raise RuntimeError(f"一次给了 {len(notes)} 条，超过上限")
    out = {}
    for note in notes:
        try:
            i = int(note["i"])
            if i not in ids:
                raise ValueError("not in section")
            new = str(note["t"]).strip()
            if new.startswith('"') and new.endswith('"') and len(new) >= 2:
                new = new[1:-1].strip()
            m = re.match(r'^[A-Za-z_]\w*\s+"(.*)"$', new)
            if m:
                new = m.group(1).strip()
            old = DIALOGUE_RE.match(lines[i - 1]).group(3)
            if not new or '"' in new or "\n" in new:
                raise ValueError("invalid text")
            if len(new) > max(12, len(old) * 1.6):
                raise ValueError("too long")
            out[i] = new
        except Exception as exc:  # noqa: BLE001
            print(f"  ! 跳过一条建议: {exc}: {note}", flush=True)
    out_dir = out_root / Path(path).stem / f"audit-{model}"
    out_dir.mkdir(parents=True, exist_ok=True)
    safe = label.replace(":", "_").replace(" ", "_")
    (out_dir / f"{safe}.json").write_text(
        json.dumps(
            {str(k): v for k, v in out.items()}, ensure_ascii=False, indent=2
        ),
        encoding="utf-8",
    )
    return label, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default="docs/polish")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", help="只处理 label 包含这个字符串的段落")
    args = ap.parse_args()

    lines, secs = sections(args.path)
    secs = [s for s in secs if not args.only or args.only in s[2]]
    all_notes = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(
                audit_section,
                args.path,
                lines,
                start,
                end,
                label,
                args.model,
                Path(args.out),
            ): label
            for start, end, label in secs
        }
        for fut in as_completed(futures):
            label = futures[fut]
            try:
                _, notes = fut.result()
                all_notes.update(notes)
                print(f"[{label}] {len(notes)} 条", flush=True)
            except Exception as exc:  # noqa: BLE001
                print(f"[{label}] 失败: {exc}", flush=True)

    if args.apply:
        changed = {
            i: v
            for i, v in all_notes.items()
            if v != DIALOGUE_RE.match(lines[i - 1]).group(3)
        }
        apply(args.path, changed)
        print(f"已应用 {len(changed)} 句")
    else:
        print(f"共 {len(all_notes)} 条建议，未应用")


if __name__ == "__main__":
    sys.exit(main())
