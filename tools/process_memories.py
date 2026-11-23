#!/usr/bin/env python3
"""记忆物件后处理：裁透明边，缩放到统一画布，方便星图叠加。"""
import sys
import os
from PIL import Image

CANVAS = 560
MAX = 520


def process(src, dst):
    im = Image.open(src).convert("RGBA")
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    w, h = im.size
    scale = min(MAX / w, MAX / h)
    im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    canvas = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    canvas.alpha_composite(im, ((CANVAS - im.width) // 2, (CANVAS - im.height) // 2))
    canvas.save(dst, "PNG")
    print(f"{os.path.basename(dst)} {canvas.width}x{canvas.height}")


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