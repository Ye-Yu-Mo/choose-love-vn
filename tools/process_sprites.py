#!/usr/bin/env python3
"""立绘后处理：裁切透明边、去边缘杂色、1.5x 放大、锐化。

用法: python3 tools/process_sprites.py raw_dir out_dir [names...]
"""
import sys
import os
import numpy as np
from PIL import Image, ImageFilter


def defringe(im):
    arr = np.array(im.convert("RGBA"))
    rgb = arr[:, :, :3].astype(np.float32)
    alpha = arr[:, :, 3]
    filled = rgb.copy()
    fm = alpha > 250
    for _ in range(6):
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb_rgb = np.roll(filled, (dy, dx), axis=(0, 1))
            nb_m = np.roll(fm, (dy, dx), axis=(0, 1))
            take = (~fm) & nb_m
            filled[take] = nb_rgb[take]
            fm = fm | take
    out = np.dstack([filled, alpha.astype(np.float32)]).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def clean_edges(im):
    """边缘 3px 内用 3x3 中值压掉 AI 生成的彩色噪点。"""
    arr = np.array(im)
    rgb = Image.fromarray(arr[:, :, :3], "RGB")
    med = np.array(rgb.filter(ImageFilter.MedianFilter(3)))
    band = np.array(im.getchannel("A").filter(ImageFilter.MinFilter(7))) < 255
    wide = np.array(im.getchannel("A").filter(ImageFilter.MinFilter(11))) < 255
    # 冷色相（绿/青/蓝/品红）基本不该出现在皮肤和头发边缘
    hsv = np.array(im.convert("HSV"))
    hue = hsv[:, :, 0].astype(int)
    sat = hsv[:, :, 1].astype(int)
    cool = (hue > 45) & (hue < 210) & (sat > 50)
    mask = band | (wide & cool)
    out_rgb = np.where(mask[:, :, None], med, arr[:, :, :3])
    out = np.dstack([out_rgb, arr[:, :, 3]]).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def process(src, dst):
    im = Image.open(src).convert("RGBA")
    im = defringe(im)
    im = clean_edges(im)
    # 轻微腐蚀 alpha，去掉半透明毛边
    a = im.getchannel("A").filter(ImageFilter.MinFilter(3))
    im.putalpha(a)
    # 裁到 alpha 边界
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    # 放大 + 锐化
    w, h = im.size
    im = im.resize((int(w * 1.5), int(h * 1.5)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=90, threshold=2))
    im.save(dst, "PNG")
    print(f"{os.path.basename(dst)} {im.size[0]}x{im.size[1]}")


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
