#!/usr/bin/env python3
"""为角色对白生成 Breeze-TTS 语音，并插入 Ren'Py voice 语句。

- 只处理 shenlan / luyao / xiaoman / landlord / zhou 的对白，不处理旁白。
- 用 assets/voice_refs 里的合成参考音做 voice direction，保持每个角色一条声线。
- 输出 game/audio/voice/<file>_<line>.ogg，并在对白前插入 voice 语句。
- 同一个角色 + 同一句文本只生成一次，其余复用。

用法:
  python3 tools/make_voice.py --dry-run
  python3 tools/make_voice.py
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
from scipy.io import wavfile

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"
OUT = GAME / "audio" / "voice"
REF_DIR = ROOT / "assets" / "voice_refs"
MODEL = "mlx-community/Breeze-TTS-2-mlx-8bit"

SPEAKERS = {"shenlan", "luyao", "xiaoman", "landlord", "zhou"}
SKIP_FILES = {
    "screens.rpy",
    "gui.rpy",
    "options.rpy",
    "guisupport.rpy",
    "ui_menu.rpy",
    "ui_chapters.rpy",
    "records.rpy",
    "audio.rpy",
    "effects.rpy",
    "images.rpy",
    "sprites.rpy",
    "pov.rpy",
}

DIALOGUE_RE = re.compile(r'^(\s*)([A-Za-z_]\w*)\s+"(.*)"\s*$')


def clean_text(text):
    text = text.replace("\\n", " ")
    text = re.sub(r"\{[^}]*\}", "", text)
    text = re.sub(r"\[[^\]]*\]", "", text)
    return text.strip()


def collect():
    jobs = []
    for path in sorted(GAME.glob("*.rpy")):
        if path.name in SKIP_FILES:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines, 1):
            m = DIALOGUE_RE.match(line)
            if not m or m.group(2) not in SPEAKERS:
                continue
            text = clean_text(m.group(3))
            if not text:
                continue
            # 已经有 voice 语句就跳过
            prev = lines[i - 2].strip() if i >= 2 else ""
            if prev.startswith("voice "):
                continue
            jobs.append(
                {
                    "file": path.name,
                    "line": i,
                    "speaker": m.group(2),
                    "text": text,
                    "indent": m.group(1),
                }
            )
    return jobs


def synth(model, refs, speaker, text, seed=42):
    ref = refs[speaker]
    instruct = (
        "保持这个声音。按台词自然地说，不要播音腔。"
        "沈岚：语速慢一点，声音轻，句子之间留一点停顿。"
        if speaker == "shenlan"
        else "保持这个声音。按台词自然地说，不要播音腔。"
    )
    if speaker == "luyao":
        instruct = "保持这个声音。按台词自然地说，语速中等，克制，不要播音腔。"
    elif speaker == "xiaoman":
        instruct = "保持这个声音。按台词自然地说，语速偏快，带一点笑意，不要播音腔。"
    elif speaker == "landlord":
        instruct = "保持这个声音。按台词自然地说，语气客气、实际。"
    elif speaker == "zhou":
        instruct = "保持这个声音。按台词自然地说，语速慢，话不多。"
    res = list(
        model.generate(
            text=text,
            voice="S0",
            instruct=instruct,
            ref_audio=ref["path"],
            ref_text=ref["text"],
            cfg_scale=4,
            seed=seed,
        )
    )
    if not res:
        raise RuntimeError("没有生成音频")
    audio = np.concatenate(
        [np.asarray(r.audio, dtype=np.float32).squeeze() for r in res if r.audio.size]
    )
    return audio, res[0].sample_rate


def to_ogg(wav_path, ogg_path):
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(wav_path),
            "-af",
            "loudnorm=I=-18:TP=-1.5:LRA=11",
            "-c:a",
            "libvorbis",
            "-q:a",
            "5",
            str(ogg_path),
        ],
        check=True,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--insert-only", action="store_true", help="不生成音频，只按已有 manifest 插入 voice")
    args = ap.parse_args()

    refs = json.loads((REF_DIR / "refs.json").read_text(encoding="utf-8"))
    if args.insert_only:
        manifest = json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))
        insert_voice(manifest)
        return
    jobs = collect()
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"{len(jobs)} 句对白")
    if args.dry_run:
        for j in jobs[:10]:
            print(j)
        return

    from mlx_audio.tts.utils import load_model

    OUT.mkdir(parents=True, exist_ok=True)
    model = load_model(MODEL)

    cache = {}
    manifest = []
    started = time.time()
    for n, job in enumerate(jobs, 1):
        key = hashlib.sha1((job["speaker"] + "\0" + job["text"]).encode()).hexdigest()[:12]
        target = OUT / f"{Path(job['file']).stem}_{job['line']}.ogg"
        if target.exists() and target.stat().st_size > 1000:
            manifest.append(
                {
                    "file": job["file"],
                    "line": job["line"],
                    "speaker": job["speaker"],
                    "text": job["text"],
                    "audio": str(target.relative_to(GAME)),
                }
            )
            cache.setdefault(key, target)
            continue
        if key in cache and cache[key].exists():
            shutil.copyfile(cache[key], target)
        else:
            audio, sr = synth(model, refs, job["speaker"], job["text"])
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                tmp_path = Path(tmp.name)
            wavfile.write(str(tmp_path), sr, (audio * 32767).astype(np.int16))
            to_ogg(tmp_path, target)
            tmp_path.unlink(missing_ok=True)
            cache[key] = target
        manifest.append(
            {
                "file": job["file"],
                "line": job["line"],
                "speaker": job["speaker"],
                "text": job["text"],
                "audio": str(target.relative_to(GAME)),
            }
        )
        if n % 20 == 0 or n == len(jobs):
            print(f"{n}/{len(jobs)}  {round(time.time() - started, 1)}s", flush=True)

    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 插入 voice 语句（从后往前，避免行号漂移）
    insert_voice(manifest)
    print(f"完成，总耗时 {round(time.time() - started, 1)} 秒")


def insert_voice(manifest):
    by_file = {}
    for item in manifest:
        by_file.setdefault(item["file"], []).append(item)
    for fname, items in by_file.items():
        path = GAME / fname
        lines = path.read_text(encoding="utf-8").splitlines()
        for item in sorted(items, key=lambda x: x["line"], reverse=True):
            i = item["line"] - 1
            m = DIALOGUE_RE.match(lines[i])
            if not m:
                continue
            prev = lines[i - 1].strip() if i >= 1 else ""
            if prev.startswith("voice "):
                continue
            lines.insert(i, f'{m.group(1)}voice "{item["audio"]}"')
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"插入 {len(items)} 条 voice: {fname}")


if __name__ == "__main__":
    main()
