#!/usr/bin/env python3
"""生成星图用的小星星贴图（点亮 / 未点亮）。"""
import math
import os
from PIL import Image, ImageDraw, ImageFilter

SIZE = 160
OUT = "game/images/ui"


def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def make(path, core, edge, glow):
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    cx = cy = SIZE / 2
    pts = star_points(cx, cy, SIZE * 0.40, SIZE * 0.16)

    # 光晕
    layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.polygon(pts, fill=glow)
    layer = layer.filter(ImageFilter.GaussianBlur(14))
    img.alpha_composite(layer)

    # 星体
    d = ImageDraw.Draw(img)
    d.polygon(pts, fill=edge)
    inner = star_points(cx, cy, SIZE * 0.30, SIZE * 0.12)
    d.polygon(inner, fill=core)
    img.save(path, "PNG")
    print(path)


def main():
    os.makedirs(OUT, exist_ok=True)
    make(os.path.join(OUT, "star_lit.png"),
         core=(255, 244, 222, 255), edge=(232, 199, 168, 255), glow=(255, 196, 130, 150))
    make(os.path.join(OUT, "star_dim.png"),
         core=(120, 132, 156, 150), edge=(84, 96, 118, 120), glow=(60, 72, 96, 40))


if __name__ == "__main__":
    main()