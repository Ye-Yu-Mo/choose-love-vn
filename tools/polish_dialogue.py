#!/usr/bin/env python3
"""按 label 分块润色 Ren'Py 台词：只改引号里的中文，不动代码。

用法:
  python3 tools/polish_dialogue.py game/script.rpy --model gpt-6.1-terra
  python3 tools/polish_dialogue.py game/script.rpy --apply

建议先不带 --apply 跑一遍，看一眼 docs/polish/ 下的建议，再决定是否应用。
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

API = "https://llm-proxy.ftai.chat/v1/chat/completions"
PROXY = "http://127.0.0.1:7890"

STYLE = """人物声音：
- 沈岚（24，咖啡店主，叙述者）：句子短，具体，少比喻；用做事挡回情绪；真正坦白时反而很平，像在说别人的事。绝不会长篇自我剖析。
- 陆遥（25，程序员）：中等长度，技术/修理比喻，轻描淡写（还行、能修、我看看）；用实际问题代替情感问题；被逼急时沉默或解释过多。绝不邀功、算账。
- 小满（22，店员）：快、跳，爱用叠词和手工比喻；叫沈岚「老板」；开心时数数；受伤时变得特别客气。绝不拿离开威胁人。
- 老周（60+，调琴师）：慢、短，说一半留一半，不说教。
- 房东：客气、实际、算账，给期限但不威胁。
规则：
1. 只改台词和旁白的中文，不改任何代码、标签、变量、选项、数值、日期、道具事实、分支结果。
2. 保持每句原本的视角：在 `if pov == "luyao":` 分支里「我」是陆遥；否则「我」是沈岚。不要串视角。
3. 去掉解释性旁白、过于整齐的排比、把情绪说满的句子；优先用具体动作和停顿。
4. 不增加新剧情，不删关键信息；每句长度尽量不超过原文的 1.3 倍。
5. 不要写性内容、安全词、羞耻表达；不要用「她很脏」这类说法。
6. 保留原有的引号内标点风格（中文引号、省略号）。
7. 如果原句已经符合角色声音，可以原样返回；不要为了改而改。
"""

DIALOGUE_RE = re.compile(r'^(\s*)((?:[A-Za-z_]\w*\s+)?")((?:[^"\\]|\\.)*)("\s*)$')


def sections(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    starts = []
    for i, line in enumerate(lines):
        if re.match(r"^label\s+\w+\s*:", line):
            starts.append((i + 1, line.strip()))
    if not starts:
        starts = [(1, "file")]
    out = []
    for j, (start, label) in enumerate(starts):
        end = starts[j + 1][0] - 1 if j + 1 < len(starts) else len(lines)
        out.append((start, end, label))
    return lines, out


def dialogue_lines(lines, start, end):
    out = []
    for n in range(start, end + 1):
        line = lines[n - 1]
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.endswith('":'):
            continue
        if s.startswith("centered "):
            continue
        if s.startswith(("voice ", "play ", "queue ", "stop ")):
            continue
        m = DIALOGUE_RE.match(line)
        if not m:
            continue
        body = m.group(3)
        # 跳过含插值/转义的句子，避免破坏代码
        if any(ch in body for ch in "[]{}%\\"):
            continue
        out.append(n)
    return out


def call(prompt, model):
    token = os.environ.get("FT_API_KEY")
    if not token:
        raise RuntimeError("FT_API_KEY 未设置")
    body = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 8000,
        },
        ensure_ascii=False,
    )
    for attempt in range(1, 4):
        res = subprocess.run(
            [
                "curl",
                "-s",
                "--max-time",
                "240",
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
            if attempt == 3:
                raise RuntimeError(f"模型返回解析失败: {exc}: {res.stdout[:500]}")
            time.sleep(2 * attempt)


def validate(lines, ids, payload, allow_missing=False, fill_missing=True):
    got = payload.get("lines", [])
    if not isinstance(got, list):
        raise RuntimeError("lines 不是数组")
    by_id = {int(x["i"]): str(x["t"]).strip() for x in got if "i" in x and "t" in x}
    missing = [i for i in ids if i not in by_id]
    extra = [i for i in by_id if i not in ids]
    if extra:
        raise RuntimeError(f"行号不匹配 extra={extra[:5]}")
    if missing and not allow_missing:
        raise RuntimeError(f"行号不匹配 missing={missing[:5]}")
    result = {}
    for i in ids:
        if i in missing:
            if fill_missing:
                result[i] = DIALOGUE_RE.match(lines[i - 1]).group(3)
            continue
        new = by_id[i].strip()
        # 模型有时会把说话人/外层引号一起返回，这里剥掉
        if new.startswith('"') and new.endswith('"') and len(new) >= 2:
            new = new[1:-1].strip()
        else:
            m = re.match(r'^[A-Za-z_]\w*\s+"(.*)"$', new)
            if m:
                new = m.group(1).strip()
        if not new or '"' in new or "\n" in new:
            raise RuntimeError(f"第 {i} 行新文本无效: {new!r}")
        old = DIALOGUE_RE.match(lines[i - 1]).group(3)
        if len(new) > max(12, len(old) * 1.6):
            raise RuntimeError(f"第 {i} 行改得过长: {old!r} -> {new!r}")
        result[i] = new
    return result


def apply(path, changes):
    p = Path(path)
    lines = p.read_text(encoding="utf-8").splitlines()
    for i, new in changes.items():
        line = lines[i - 1]
        m = DIALOGUE_RE.match(line)
        if not m:
            raise RuntimeError(f"第 {i} 行不再匹配: {line!r}")
        lines[i - 1] = f"{m.group(1)}{m.group(2)}{new}{m.group(4)}"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--model", default="gpt-6.1-terra")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--out", default="docs/polish")
    ap.add_argument("--label", help="只处理这个 label")
    args = ap.parse_args()

    lines, secs = sections(args.path)
    out_dir = Path(args.out) / Path(args.path).stem / args.model
    out_dir.mkdir(parents=True, exist_ok=True)

    total = 0
    applied = {}
    for start, end, label in secs:
        if args.label and args.label not in label:
            continue
        ids = dialogue_lines(lines, start, end)
        if not ids:
            continue
        src = "\n".join(
            (f"[[D{n}]] " if n in ids else "       ") + lines[n - 1]
            for n in range(start, end + 1)
        )
        prompt = (
            STYLE
            + f"\n文件：{args.path}\n段落：{label}（第 {start}-{end} 行）\n"
            + "下面带 [[D]] 的行需要润色；其他行只用于理解上下文，不要输出。\n\n"
            + src
            + '\n\n只输出 JSON 对象：{"lines":[{"i":行号,"t":"新台词"}]}，覆盖全部 [[D]] 行。不要输出 markdown。'
        )
        print(f"[{label}] {len(ids)} 句 …", flush=True)
        payload = call(prompt, args.model)
        changes = validate(lines, ids, payload)
        (out_dir / f"{label.replace(':', '_').replace(' ', '_')}.json").write_text(
            json.dumps(changes, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        applied.update(changes)
        total += len(changes)

    if args.apply:
        apply(args.path, applied)
        print(f"已应用 {len(applied)} 句")
    else:
        print(f"已生成 {total} 句建议，未应用")


if __name__ == "__main__":
    sys.exit(main())
