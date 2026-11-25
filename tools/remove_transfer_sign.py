#!/usr/bin/env python3
"""用邻近玻璃区域覆盖背景图上的「转让」牌，生成无牌背景变体。"""
from PIL import Image, ImageDraw, ImageFilter

JOBS = [
    ("game/images/bg shop day.png", "game/images/bg shop day no sign.png",
     (135, 150, 275, 310), (0, 165)),
    ("game/images/bg shop night.png", "game/images/bg shop night no sign.png",
     (1105, 150, 1225, 300), (0, 160)),
]


def feather_mask(size, feather=18):
    m = Image.new("L", size, 255)
    d = ImageDraw.Draw(m)
    d.rectangle([feather, feather, size[0] - feather, size[1] - feather], fill=255)
    # 边缘渐隐
    m = m.filter(ImageFilter.GaussianBlur(feather))
    return m


for src, dst, box, off in JOBS:
    im = Image.open(src).convert("RGB")
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    sx, sy = x0 + off[0], y0 + off[1]
    patch = im.crop((sx, sy, sx + w, sy + h))
    # 轻微模糊，减少与周围雨丝的接缝感
    patch = patch.filter(ImageFilter.GaussianBlur(1.2))
    mask = feather_mask((w, h), 20)
    im.paste(patch, (x0, y0), mask)
    im.save(dst)
    print(dst)
