#!/usr/bin/env python3
"""生成对话框纸张、章节卡纸片（基于 paper texture）。"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

TEX = "game/images/ui/raw/ui_paper_texture.png"
OUT = "game/images/ui"


def load_tex():
    return Image.open(TEX).convert("RGB")


def paper_window(tex):
    w, h = 1280, 220
    base = tex.resize((w, h)).convert("RGBA")
    overlay = Image.new("RGBA", (w, h), (255, 244, 226, 14))
    base = Image.alpha_composite(base, overlay)

    xs = np.arange(w)
    top = (5 + 2.5 * np.sin(xs / 47.0) + 2 * np.sin(xs / 13.0 + 1.2)).astype(int)
    mask = np.zeros((h, w), dtype=np.uint8)
    for x in range(w):
        mask[top[x]:, x] = 242
    alpha = Image.fromarray(mask, "L")

    shadow = Image.new("RGBA", (w, h), (30, 18, 8, 0))
    smask = np.zeros((h, w), dtype=np.uint8)
    for x in range(w):
        smask[min(h - 1, top[x] + 3):, x] = 110
    shadow.putalpha(Image.fromarray(smask, "L").filter(ImageFilter.GaussianBlur(6)))

    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.alpha_composite(shadow)
    base.putalpha(alpha)
    out.alpha_composite(base)
    out.save(os.path.join(OUT, "paper_window.png"))
    print("paper_window.png")


def paper_card(tex, path, w, h, radius=26, shadow_alpha=90):
    fill = tex.resize((w, h)).convert("RGBA")
    fill = Image.alpha_composite(fill, Image.new("RGBA", (w, h), (255, 246, 232, 14)))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([6, 6, w - 7, h - 7], radius=radius, fill=255)

    shadow = Image.new("RGBA", (w, h), (20, 12, 6, 0))
    shadow.putalpha(mask.point(lambda v: shadow_alpha if v else 0))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    shadow = shadow.transform(shadow.size, Image.AFFINE, (1, 0, -3, 0, 1, -6))

    fill.putalpha(mask)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.alpha_composite(shadow)
    out.alpha_composite(fill)
    out.save(path)
    print(os.path.basename(path))


def main():
    tex = load_tex()
    paper_window(tex)
    paper_card(tex, os.path.join(OUT, "paper_card.png"), 900, 560)
    paper_card(tex, os.path.join(OUT, "paper_card_small.png"), 560, 330, radius=20)


if __name__ == "__main__":
    main()