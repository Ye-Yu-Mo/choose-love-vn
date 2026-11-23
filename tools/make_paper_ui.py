#!/usr/bin/env python3
"""用纸张纹理生成主菜单用的 UI 层：暗角、左侧压暗、纸质按钮、翻页转场遮罩。"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

TEX = "game/images/ui/raw/ui_paper_texture.png"
OUT = "game/images/ui"
W, H = 1280, 720


def vignette():
    yy, xx = np.mgrid[0:H, 0:W]
    dx = (xx - W / 2) / (W / 2)
    dy = (yy - H / 2) / (H / 2)
    d = np.sqrt(dx * dx + dy * dy * 0.85)
    a = np.clip((d - 0.55) / 0.55, 0, 1) ** 1.8 * 205
    img = np.zeros((H, W, 4), dtype=np.uint8)
    img[:, :, 0] = 10
    img[:, :, 1] = 7
    img[:, :, 2] = 4
    img[:, :, 3] = a.astype(np.uint8)
    Image.fromarray(img, "RGBA").save(os.path.join(OUT, "vignette.png"))
    print("vignette.png")


def left_shade():
    img = np.zeros((H, W, 4), dtype=np.uint8)
    xs = np.arange(W)
    a = np.clip((640 - xs) / 640, 0, 1) ** 1.4 * 215
    img[:, :, 0] = 18
    img[:, :, 1] = 12
    img[:, :, 2] = 7
    img[:, :, 3] = a.astype(np.uint8)[None, :]
    Image.fromarray(img, "RGBA").save(os.path.join(OUT, "menu_left_shade.png"))
    print("menu_left_shade.png")


def tag(tex, path, tint):
    w, h = 420, 104
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=14, fill=255)
    fill = tex.resize((w, h)).convert("RGBA")
    if tint:
        fill = Image.alpha_composite(fill, Image.new("RGBA", (w, h), tint))
    tagimg = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    tagimg.paste(fill, (0, 0), mask)
    d = ImageDraw.Draw(tagimg)
    d.rounded_rectangle([1, 1, w - 2, h - 2], radius=14, outline=(150, 118, 84, 120), width=2)
    tagimg.save(path)
    print(os.path.basename(path))


def paper_mask():
    rng = np.random.default_rng(7)
    noise = rng.random((H // 4, W // 4)).astype(np.float32) * 255
    noise_img = Image.fromarray(noise.astype(np.uint8), "L").resize((W, H), Image.BICUBIC)
    noise_img = noise_img.filter(ImageFilter.GaussianBlur(6))
    n = np.array(noise_img).astype(np.float32) / 255

    yy, xx = np.mgrid[0:H, 0:W]
    grad = (xx / W * 0.65 + yy / H * 0.35)
    m = np.clip(grad * 0.82 + n * 0.18, 0, 1)
    m = (m - m.min()) / (m.max() - m.min())
    Image.fromarray((m * 255).astype(np.uint8), "L").save(os.path.join(OUT, "paper_mask.png"))
    print("paper_mask.png")


def main():
    os.makedirs(OUT, exist_ok=True)
    tex = Image.open(TEX).convert("RGB")
    vignette()
    left_shade()
    tag(tex, os.path.join(OUT, "paper_tag_idle.png"), None)
    tag(tex, os.path.join(OUT, "paper_tag_hover.png"), (255, 246, 230, 46))
    paper_mask()


if __name__ == "__main__":
    main()