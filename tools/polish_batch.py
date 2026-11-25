#!/usr/bin/env python3
"""两阶段台词润色：Astra 起草，Opus 审核，按 label 并行。

用法:
  python3 tools/polish_batch.py game/script.rpy --apply
  python3 tools/polish_batch.py game/story_mid.rpy --workers 4

输出:
  docs/polish/<file>/<draft>/<label>.json   起草
  docs/polish/<file>/<review>/<label>.json  审核后的最终稿
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
    validate,
)

DRAFT_MODEL = "gpt-6.2-astra"
REVIEW_MODEL = "claude-opus-5-5"


def call(model, prompt, max_tokens=8000, retries=3):
    token = os.environ.get("FT_API_KEY")
    if not token:
        raise RuntimeError("FT_API_KEY 未设置")
    body = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": max_tokens,
        },
        ensure_ascii=False,
    )
    last = None
    for attempt in range(1, retries + 1):
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
            if attempt < retries:
                time.sleep(2 * attempt)
    raise RuntimeError(f"{model} 调用失败: {last}")


def body_of(line):
    m = DIALOGUE_RE.match(line)
    return m.group(3) if m else None


def clean_new(text):
    text = str(text).strip()
    if text.startswith('"') and text.endswith('"') and len(text) >= 2:
        return text[1:-1].strip()
    m = re.match(r'^[A-Za-z_]\w*\s+"(.*)"$', text)
    if m:
        return m.group(1).strip()
    return text


def process_section(path, lines, start, end, label, out_root):
    ids = dialogue_lines(lines, start, end)
    if not ids:
        return label, {}, "skip"

    src = "\n".join(
        (f"[[D{n}]] " if n in ids else "       ") + lines[n - 1]
        for n in range(start, end + 1)
    )
    draft_prompt = (
        STYLE
        + f"\n文件：{path}\n段落：{label}（第 {start}-{end} 行）\n"
        + "下面带 [[D]] 的行需要润色；其他行只用于理解上下文，不要输出。\n\n"
        + src
        + '\n\n只输出 JSON 对象：{"lines":[{"i":行号,"t":"新台词"}]}，覆盖全部 [[D]] 行。不要输出 markdown。'
    )
    draft = call(DRAFT_MODEL, draft_prompt)
    draft_changes = validate(lines, ids, draft, allow_missing=True)

    # 只把真正改动的行交给审核，附上前后两行上下文
    changed = [i for i in ids if draft_changes[i] != body_of(lines[i - 1])]
    if changed:
        blocks = []
        last = None
        for i in changed:
            lo, hi = max(start, i - 2), min(end, i + 2)
            if last is not None and lo <= last + 1:
                lo = last + 1
            if lo > hi:
                continue
            block = []
            for n in range(lo, hi + 1):
                mark = "原文" if n == i else "    "
                block.append(f"{mark} {n}: {lines[n - 1].strip()}")
            if i >= lo:
                block.append(f"候选 {i}: {draft_changes[i]}")
            blocks.append("\n".join(block))
            last = hi
        review_prompt = (
            STYLE
            + "\n你是终审编辑。下面每块先给原文和上下文，再给候选改写。\n"
            + "逐行判断：候选是否真的更好？如果候选丢了角色声音、改了视角/事实/语气，或者只是把话说得更满，就改回原文或给出更好的版本；如果候选更好，就保留。不要为了改而改。\n\n"
            + "\n\n".join(blocks)
            + '\n\n只输出 JSON 对象：{"lines":[{"i":行号,"t":"最终台词"}]}，覆盖上面所有“候选”行。不要输出解释或 markdown。'
        )
        try:
            reviewed = call(REVIEW_MODEL, review_prompt)
            reviewed_changes = validate(
                lines, changed, reviewed, allow_missing=True, fill_missing=False
            )
            final_changes = {
                i: reviewed_changes.get(i, draft_changes[i]) for i in changed
            }
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {label} 审核失败，保留起草稿: {exc}", flush=True)
            final_changes = {i: draft_changes[i] for i in changed}
    else:
        final_changes = {i: draft_changes[i] for i in changed}

    draft_dir = out_root / Path(path).stem / DRAFT_MODEL
    final_dir = out_root / Path(path).stem / REVIEW_MODEL
    draft_dir.mkdir(parents=True, exist_ok=True)
    final_dir.mkdir(parents=True, exist_ok=True)
    safe = label.replace(":", "_").replace(" ", "_")
    (draft_dir / f"{safe}.json").write_text(
        json.dumps(draft_changes, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (final_dir / f"{safe}.json").write_text(
        json.dumps(final_changes, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return label, final_changes, f"{len(ids)} 句 / 改 {len(changed)} 句"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default="docs/polish")
    ap.add_argument("--only", help="只处理 label 包含这个字符串的段落")
    args = ap.parse_args()

    lines, secs = sections(args.path)
    secs = [s for s in secs if not args.only or args.only in s[2]]
    out_root = Path(args.out)

    all_changes = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(process_section, args.path, lines, start, end, label, out_root): label
            for start, end, label in secs
        }
        for fut in as_completed(futures):
            label = futures[fut]
            try:
                _, changes, info = fut.result()
                all_changes.update(changes)
                print(f"[{label}] {info}", flush=True)
            except Exception as exc:  # noqa: BLE001
                print(f"[{label}] 失败: {exc}", flush=True)

    if args.apply:
        # 只保留真正改动的行
        changed = {
            i: v for i, v in all_changes.items() if v != body_of(lines[i - 1])
        }
        apply(args.path, changed)
        print(f"已应用 {len(changed)} 句")
    else:
        print(f"已生成建议，未应用。共 {len(all_changes)} 句")


if __name__ == "__main__":
    sys.exit(main())
