#!/usr/bin/env python3
"""生成物件特写：菜单板、转让牌、咖啡+纸星静物。"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

FONT = "game/fonts/SourceHanSansLite.ttf"
OUT = "game/images/props"


def font(size):
    return ImageFont.truetype(FONT, size)


def menu_board():
    w, h = 680, 500
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(out)
    # 木框
    d.rounded_rectangle([10, 10, w - 10, h - 10], 14, fill=(86, 58, 36, 255), outline=(54, 36, 22, 255), width=4)
    # 黑板
    d.rounded_rectangle([34, 34, w - 34, h - 34], 8, fill=(28, 38, 36, 255), outline=(120, 92, 62, 255), width=2)
    d.text((w // 2, 66), "菜单", font=font(38), fill=(238, 228, 206), anchor="mm")
    d.line([90, 104, w - 90, 104], fill=(190, 176, 150), width=2)
    items = [("美式", "18"), ("拿铁", "22"), ("手冲", "28"), ("当日甜点", "15")]
    y = 150
    for name, price in items:
        d.text((90, y), name, font=font(30), fill=(232, 224, 204))
        d.text((w - 90, y), price, font=font(30), fill=(232, 224, 204), anchor="ra")
        d.line([90, y + 48, w - 90, y + 48], fill=(70, 82, 78), width=1)
        y += 74
    d.text((w // 2, h - 58), "咖啡 — 手工 — 星星", font=font(20), fill=(160, 154, 140), anchor="mm")
    out.save(os.path.join(OUT, "menu_board.png"))
    print("menu_board.png")


def transfer_sign():
    w, h = 640, 440
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(out)
    # 绳子
    d.line([(190, 0), (270, 66)], fill=(120, 96, 68), width=6)
    d.line([(450, 0), (370, 66)], fill=(120, 96, 68), width=6)
    # 木牌
    d.rounded_rectangle([70, 56, w - 70, h - 40], 18, fill=(150, 108, 68, 255), outline=(92, 62, 38, 255), width=4)
    for i in range(10):
        y = 80 + i * 30
        d.line([86, y, w - 86, y + 8], fill=(128, 90, 56, 255), width=2)
    d.text((w // 2, 158), "转让", font=font(104), fill=(58, 34, 20), anchor="mm")
    d.text((w // 2, 268), "店面转让", font=font(34), fill=(72, 44, 26), anchor="mm")
    d.text((w // 2, 320), "有意者面谈", font=font(24), fill=(90, 58, 34), anchor="mm")
    out.save(os.path.join(OUT, "transfer_sign.png"))
    print("transfer_sign.png")


def coffee_star():
    w, h = 900, 600
    bg = Image.open("game/images/bg shop night.png").convert("RGB").resize((w, h))
    bg = bg.filter(ImageFilter.GaussianBlur(20))
    arr = np.array(bg).astype(np.float32) * 0.45
    bg = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")

    # 只在杯子后方加一层很淡的暖光
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([100, 120, 700, 640], fill=(255, 190, 112, 34))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    bg.alpha_composite(glow)

    # 桌面暖色带
    table = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    td = ImageDraw.Draw(table)
    td.rectangle([0, 470, w, h], fill=(92, 52, 26, 60))
    table = table.filter(ImageFilter.GaussianBlur(30))
    bg.alpha_composite(table)

    cup = Image.open("game/images/mem/mem_cup.png").convert("RGBA")
    cup = cup.resize((470, 470), Image.LANCZOS)
    star = Image.open("game/images/mem/mem_paper_star.png").convert("RGBA")
    star = star.resize((205, 205), Image.LANCZOS)

    def shadow(box, blur=16, alpha=120):
        s = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(s).ellipse(box, fill=(0, 0, 0, alpha))
        bg.alpha_composite(s.filter(ImageFilter.GaussianBlur(blur)))

    shadow([165, 505, 585, 590])
    bg.alpha_composite(cup, (135, 135))
    shadow([600, 455, 780, 550], blur=12, alpha=100)
    star = star.rotate(-18, expand=True, resample=Image.BICUBIC)
    bg.alpha_composite(star, (590, 300))

    # 轻微暗角
    vig = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-160, -160, w + 160, h + 160], outline=(0, 0, 0, 0), width=1)
    bg.save(os.path.join(OUT, "coffee_star.png"))
    print("coffee_star.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    menu_board()
    transfer_sign()
    coffee_star()
