#!/usr/bin/env python3
"""CG 后处理：中心裁成 16:9，缩到 1280x720。

用法: python3 tools/process_cgs.py raw_dir out_dir [names...]
"""
import sys
import os
from PIL import Image, ImageFilter


def process(src, dst):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target = 16 / 9
    if w / h > target:
        nw = int(h * target)
        x = (w - nw) // 2
        im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target)
        y = (h - nh) // 2
        im = im.crop((0, y, w, y + nh))
    im = im.resize((1280, 720), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    im.save(dst, "PNG")
    print(f"{os.path.basename(dst)} 1280x720")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    raw, out = sys.argv[1], sys.argv[2]
    names = sys.argv[3:]
    files = names or [f[:-4] for f in os.listdir(raw) if f.endswith(".png")]
    for name in files:
        src = os.path.join(raw, name + ".png")
        if not os.path.exists(src):
            print(f"skip {name}: not found")
            continue
        process(src, os.path.join(out, name + ".png"))


if __name__ == "__main__":
    main()
