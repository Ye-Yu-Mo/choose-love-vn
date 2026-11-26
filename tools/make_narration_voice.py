#!/usr/bin/env python3
"""为旁白生成双 POV 语音：一周目用沈岚声，二周目用陆遥声。

- 同一句旁白生成两份音频；运行时用 `voice (... if pov == ... else ...)` 选。
- 内容寻址：narr_<speaker>_<hash>.ogg，改稿后只重生成变化的那句。
- 只处理没有角色前缀的旁白行。
"""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"
OUT = GAME / "audio" / "voice"
REF_DIR = ROOT / "assets" / "voice_refs"
MANIFEST = OUT / "narration_manifest.json"
MODEL = "mlx-community/Breeze-TTS-2-mlx-8bit"

SKIP_FILES = {
    "screens.rpy", "gui.rpy", "options.rpy", "guisupport.rpy",
    "ui_menu.rpy", "ui_chapters.rpy", "records.rpy", "audio.rpy",
    "effects.rpy", "images.rpy", "sprites.rpy", "pov.rpy",
}

NARRATION_RE = re.compile(r'^(\s*)"((?:[^"\\]|\\.)*)"\s*$')
VOICE_RE = re.compile(r'^(\s*)(# 待重配：)?voice\s+')

INSTRUCT = {
    "shenlan": "用沈岚的内心语气念旁白。语速慢一点，声音轻，像在说自己的事，句子之间留一点停顿，不要播音腔。",
    "luyao": "用陆遥的内心语气念旁白。语速中等，克制，像在说自己的事，不要播音腔，不煽情。",
}


def clean_text(text):
    text = text.replace("\\n", " ")
    text = re.sub(r"\{[^}]*\}", "", text)
    text = re.sub(r"\[[^\]]*\]", "", text)
    return text.strip()


def is_ogg(path):
    if not path.is_file() or path.stat().st_size <= 1000:
        return False
    with path.open("rb") as stream:
        return stream.read(4) == b"OggS"


def audio_names(text):
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:20]
    return {
        "shenlan": f"narr_shenlan_{digest}.ogg",
        "luyao": f"narr_luyao_{digest}.ogg",
    }


def collect():
    jobs = []
    for path in sorted(GAME.glob("*.rpy")):
        if path.name in SKIP_FILES:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines, 1):
            m = NARRATION_RE.match(line)
            if not m:
                continue
            if line.strip().startswith("centered "):
                continue
            text = clean_text(m.group(2))
            if not text:
                continue
            names = audio_names(text)
            prev = lines[i - 2] if i >= 2 else ""
            cue = VOICE_RE.fullmatch(prev.rstrip("\n"))
            if cue and cue[1] == m.group(1) and not cue[2]:
                if names["shenlan"] in prev and names["luyao"] in prev:
                    if is_ogg(GAME / "audio/voice" / names["shenlan"]) and is_ogg(
                        GAME / "audio/voice" / names["luyao"]
                    ):
                        continue
            jobs.append({"file": path.name, "line": i, "text": text})
    return jobs


def to_ogg(wav_path, ogg_path):
    subprocess.run(
        ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(wav_path),
         "-af", "loudnorm=I=-18:TP=-1.5:LRA=11", "-c:a", "libvorbis", "-q:a", "5",
         str(ogg_path)],
        check=True,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--insert-only", action="store_true")
    args = ap.parse_args()

    refs = json.loads((REF_DIR / "refs.json").read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else []
    by_text = {x["text"]: x for x in manifest}
    jobs = collect()
    if args.limit is not None:
        jobs = jobs[: args.limit]
    need = [j for j in jobs if not all(
        is_ogg(GAME / "audio/voice" / f) for f in audio_names(j["text"]).values()
    )]
    print(f"{len(jobs)} 处旁白，{len(need)} 句需生成（双 POV）", flush=True)
    if args.dry_run:
        for j in jobs[:10]:
            print(j)
        return
    if not jobs:
        return

    generator = None
    insertions = []
    additions = []
    started = time.time()
    for n, job in enumerate(jobs, 1):
        text = job["text"]
        names = audio_names(text)
        for speaker in ("shenlan", "luyao"):
            target = OUT / names[speaker]
            if not is_ogg(target):
                if args.insert_only:
                    continue
                if generator is None:
                    generator = make_generator(refs)
                generator(target, speaker, text)
        if all(is_ogg(OUT / f) for f in names.values()):
            insertions.append(dict(job, **names))
            if text not in by_text:
                additions.append({"text": text, **names})
                by_text[text] = {"text": text, **names}
        if n % 10 == 0 or n == len(jobs):
            print(f"{n}/{len(jobs)}  {time.time() - started:.1f}s", flush=True)

    scripts = updated_scripts(insertions)
    if additions:
        write_text(MANIFEST, json.dumps(manifest + additions, ensure_ascii=False, indent=2) + "\n")
    for path, content in scripts.items():
        write_text(path, content)
    print(f"接入 {len(insertions)} 处，总耗时 {time.time() - started:.1f} 秒")


def make_generator(refs):
    import numpy as np
    from mlx_audio.tts.utils import load_model
    from scipy.io import wavfile

    model = load_model(MODEL)
    OUT.mkdir(parents=True, exist_ok=True)

    def generate(target, speaker, text):
        ref = refs[speaker]
        res = list(
            model.generate(
                text=text,
                voice="S0",
                instruct=INSTRUCT[speaker],
                ref_audio=ref["path"],
                ref_text=ref["text"],
                cfg_scale=4,
                seed=42,
            )
        )
        audio = np.concatenate(
            [np.asarray(r.audio, dtype=np.float32).squeeze() for r in res if r.audio.size]
        )
        sr = res[0].sample_rate
        with tempfile.TemporaryDirectory(dir=OUT) as temp_dir:
            wav = Path(temp_dir) / "speech.wav"
            ogg = wav.with_suffix(".ogg")
            wavfile.write(wav, sr, (np.clip(audio, -1, 1) * 32767).astype(np.int16))
            to_ogg(wav, ogg)
            if not is_ogg(ogg):
                raise RuntimeError(f"旁白录音无效 | {speaker} | {text}")
            ogg.replace(target)

    return generate


def write_text(path, content):
    with tempfile.TemporaryDirectory(dir=path.parent) as temp_dir:
        staged = Path(temp_dir) / path.name
        staged.write_text(content, encoding="utf-8")
        staged.replace(path)


def updated_scripts(insertions):
    by_file = {}
    for item in insertions:
        by_file.setdefault(item["file"], []).append(item)
    scripts = {}
    for fname, items in by_file.items():
        path = GAME / fname
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for item in sorted(items, key=lambda x: x["line"], reverse=True):
            i = item["line"] - 1
            m = NARRATION_RE.match(lines[i]) if i < len(lines) else None
            if not m or clean_text(m.group(2)) != item["text"]:
                raise RuntimeError(f"生成期间旁白位置已变化 | {path}:{i + 1}")
            new_cue = (
                f'{m.group(1)}voice ("audio/voice/{item["shenlan"]}" '
                f'if pov == "shenlan" else "audio/voice/{item["luyao"]}")\n'
            )
            prev = VOICE_RE.fullmatch(lines[i - 1].rstrip("\n")) if i else None
            if prev and prev[1] == m.group(1):
                lines[i - 1] = new_cue
            else:
                lines.insert(i, new_cue)
        scripts[path] = "".join(lines)
    return scripts


if __name__ == "__main__":
    main()
