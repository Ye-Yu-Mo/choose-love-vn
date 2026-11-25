#!/usr/bin/env python3
"""换某个角色的参考音后，重生成该角色所有已有语音（不改台词、不改 voice 语句）。

用法:
  python3 tools/revoice_speaker.py luyao \
    --ref assets/voice_refs/luyao_candidates/a_clear_seed42.wav \
    --ref-text "我看看。这个应该能修。房租的事，我来想办法。你先别关门。"
"""
import argparse
import json
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import numpy as np
from scipy.io import wavfile

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"
MANIFEST = GAME / "audio" / "voice" / "manifest.json"
MODEL = "mlx-community/Breeze-TTS-2-mlx-8bit"

INSTRUCT = {
    "shenlan": "保持这个声音。按台词自然地说，语速慢一点，声音轻，句子之间留一点停顿，不要播音腔。",
    "luyao": "保持这个声音。按台词自然地说，语速中等，克制，咬字自然，不要播音腔。",
    "xiaoman": "保持这个声音。按台词自然地说，语速偏快，带一点笑意，不要播音腔。",
    "landlord": "保持这个声音。按台词自然地说，语气客气、实际。",
    "zhou": "保持这个声音。按台词自然地说，语速慢，话不多。",
}


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
    ap.add_argument("speaker")
    ap.add_argument("--ref", required=True)
    ap.add_argument("--ref-text", required=True)
    ap.add_argument("--instruct", default=None)
    args = ap.parse_args()

    ref = str(Path(args.ref))
    instruct = args.instruct or INSTRUCT[args.speaker]
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    jobs = [x for x in manifest if x["speaker"] == args.speaker]
    print(f"{args.speaker}: {len(jobs)} 条，{len(set(x['text'] for x in jobs))} 句唯一文本")

    from mlx_audio.tts.utils import load_model

    model = load_model(MODEL)
    cache = {}
    started = time.time()
    for n, item in enumerate(jobs, 1):
        text = item["text"]
        target = GAME / item["audio"]
        if text in cache:
            shutil.copyfile(cache[text], target)
            continue
        res = list(
            model.generate(
                text=text,
                voice="S0",
                instruct=instruct,
                ref_audio=ref,
                ref_text=args.ref_text,
                cfg_scale=4,
                seed=42,
            )
        )
        audio = np.concatenate(
            [np.asarray(r.audio, dtype=np.float32).squeeze() for r in res if r.audio.size]
        )
        sr = res[0].sample_rate
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        wavfile.write(str(tmp_path), sr, (audio * 32767).astype(np.int16))
        to_ogg(tmp_path, target)
        tmp_path.unlink(missing_ok=True)
        cache[text] = target
        if n % 20 == 0 or n == len(jobs):
            print(f"{n}/{len(jobs)}  {round(time.time() - started, 1)}s", flush=True)
    print(f"完成，总耗时 {round(time.time() - started, 1)} 秒")


if __name__ == "__main__":
    main()
