#!/usr/bin/env python3
"""为角色对白生成 Breeze-TTS 语音，并插入 Ren'Py voice 语句。

- 只处理 shenlan / luyao / xiaoman / landlord / zhou 的对白，不处理旁白。
- 用 assets/voice_refs 里的合成参考音做 voice direction，保持每个角色一条声线。
- 新录音按角色和台词命名，改稿挪行后仍能准确复用。
- manifest 记录每个音频文件的角色和台词，旧录音也保留在索引里。

用法:
  python3 tools/make_voice.py --dry-run
  python3 tools/make_voice.py
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
VOICE_RE = re.compile(r'^(\s*)(# 待重配：)?voice\s+"([^"]+)"\s*$')


def clean_text(text):
    text = text.replace("\\n", " ")
    text = re.sub(r"\{[^}]*\}", "", text)
    text = re.sub(r"\[[^\]]*\]", "", text)
    return text.strip()


def voice_key(item):
    return item["speaker"], item["text"]


def is_ogg(path):
    if not path.is_file() or path.stat().st_size <= 1000:
        return False
    with path.open("rb") as stream:
        return stream.read(4) == b"OggS"


def collect(by_audio):
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
            job = {"file": path.name, "line": i, "speaker": m.group(2), "text": text}
            cue = VOICE_RE.fullmatch(lines[i - 2]) if i >= 2 else None
            if cue and cue[1] == m[1] and not cue[2] and is_ogg(GAME / cue[3]):
                old = by_audio.get(cue[3])
                # 保留手工加入、未登记到 manifest 的有效配音。
                if old is None or voice_key(old) == voice_key(job):
                    continue
            jobs.append(job)
    return jobs


def synth(model, refs, speaker, text, seed=42):
    import numpy as np

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
    ap.add_argument("--insert-only", action="store_true", help="只接入 manifest 中与角色和台词匹配的录音")
    args = ap.parse_args()

    manifest_path = OUT / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
    by_audio = {item["audio"]: item for item in manifest}
    cache = {}
    for item in manifest:
        if is_ogg(GAME / item["audio"]):
            cache.setdefault(voice_key(item), item["audio"])

    jobs = collect(by_audio)
    if args.limit is not None:
        jobs = jobs[: args.limit]
    keys = {voice_key(job) for job in jobs}
    print(f"{len(jobs)} 处需配音，{len(keys - cache.keys())} 句需生成", flush=True)
    if args.dry_run:
        for j in jobs[:10]:
            print(j)
        return
    if not jobs:
        return

    insertions = []
    additions = []
    generator = None
    started = time.time()
    for n, job in enumerate(jobs, 1):
        key = voice_key(job)
        if key not in cache:
            if args.insert_only:
                continue
            speaker, line = key
            digest = hashlib.sha256("\0".join(key).encode("utf-8")).hexdigest()[:20]
            target = OUT / f"{speaker}_{digest}.ogg"
            audio = target.relative_to(GAME).as_posix()
            old = by_audio.get(audio)
            if old and voice_key(old) != key:
                raise ValueError(f"录音文件名冲突 | {audio}")
            if not is_ogg(target):
                if generator is None:
                    generator = voice_generator()
                generator(target, speaker, line)
            cache[key] = audio
            if old is None:
                additions.append(dict(job, audio=audio))
        insertions.append(dict(job, audio=cache[key]))
        if n % 10 == 0 or n == len(jobs):
            print(f"{n}/{len(jobs)}  {time.time() - started:.1f}s", flush=True)

    scripts = updated_scripts(insertions)
    if additions:
        write_text(manifest_path, json.dumps(manifest + additions, ensure_ascii=False, indent=2) + "\n")
    for path, content in scripts.items():
        write_text(path, content)
    print(f"接入 {len(insertions)} 处，仍缺 {len(jobs) - len(insertions)} 处，总耗时 {time.time() - started:.1f} 秒")


def voice_generator():
    import numpy as np
    from mlx_audio.tts.utils import load_model
    from scipy.io import wavfile

    refs = json.loads((REF_DIR / "refs.json").read_text(encoding="utf-8"))
    model = load_model(MODEL)
    OUT.mkdir(parents=True, exist_ok=True)

    def generate(target, speaker, text):
        audio, sr = synth(model, refs, speaker, text)
        with tempfile.TemporaryDirectory(dir=OUT) as temp_dir:
            wav = Path(temp_dir) / "speech.wav"
            ogg = wav.with_suffix(".ogg")
            wavfile.write(wav, sr, (np.clip(audio, -1, 1) * 32767).astype(np.int16))
            to_ogg(wav, ogg)
            if not is_ogg(ogg):
                raise RuntimeError(f"录音输出无效 | {speaker} | {text}")
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
            m = DIALOGUE_RE.match(lines[i]) if i < len(lines) else None
            if not m or (m[2], clean_text(m[3])) != voice_key(item):
                raise RuntimeError(f"生成期间台词位置已变化 | {path}:{i + 1}")
            new_cue = f'{m[1]}voice "{item["audio"]}"\n'
            prev = VOICE_RE.fullmatch(lines[i - 1].rstrip("\n")) if i else None
            if prev and prev[1] == m[1]:
                lines[i - 1] = new_cue
            else:
                lines.insert(i, new_cue)
        scripts[path] = "".join(lines)
    return scripts


if __name__ == "__main__":
    main()
