#!/usr/bin/env python3
"""生成文档/屏幕类特写：裁员邮件、租约、offer、信、3:47 屏幕。"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "game/fonts/SourceHanSansLite.ttf"
TEX = Image.open("game/images/ui/raw/ui_paper_texture.png").convert("RGB")
OUT = "game/images/props"


def font(size):
    return ImageFont.truetype(FONT, size)


def paper(path, title, lines, w=900, h=600, stamp=None):
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        [18, 24, w - 18, h - 10], 18, fill=(20, 12, 6, 120)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    out.alpha_composite(shadow)

    paper = TEX.resize((w - 40, h - 44)).convert("RGBA")
    paper = Image.alpha_composite(paper, Image.new("RGBA", paper.size, (255, 246, 232, 30)))
    mask = Image.new("L", paper.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, paper.width - 1, paper.height - 1], 10, fill=255)
    paper.putalpha(mask)
    out.alpha_composite(paper, (20, 12))

    d = ImageDraw.Draw(out)
    d.text((64, 54), title, font=font(34), fill=(58, 44, 30))
    d.line([64, 106, w - 64, 106], fill=(160, 138, 112), width=2)
    y = 132
    for line in lines:
        if line == "":
            y += 18
            continue
        d.text((64, y), line, font=font(23), fill=(60, 48, 36))
        y += 38

    if stamp:
        cx, cy, r = w - 150, h - 150, 74
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(178, 62, 54), width=4)
        d.text((cx, cy - 10), stamp, font=font(18), fill=(178, 62, 54), anchor="mm")

    out.save(path)
    print(os.path.basename(path))


def dark_screen(path, heading, rows, w=960, h=600, accent=(120, 190, 230), time_text=None):
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        [16, 22, w - 16, h - 8], 16, fill=(0, 0, 0, 150)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    out.alpha_composite(shadow)

    d = ImageDraw.Draw(out)
    d.rounded_rectangle([24, 14, w - 24, h - 20], 14, fill=(22, 26, 33, 250), outline=(70, 78, 92), width=2)
    d.rounded_rectangle([24, 14, w - 24, 66], 14, fill=(34, 39, 49, 255))
    d.rectangle([24, 52, w - 24, 66], fill=(34, 39, 49, 255))
    for i, c in enumerate([(232, 106, 94), (230, 188, 96), (112, 190, 120)]):
        d.ellipse([46 + i * 26, 30, 58 + i * 26, 42], fill=c)
    d.text((w - 150, 32), heading, font=font(18), fill=(190, 196, 208))

    y = 96
    for row in rows:
        color = (225, 231, 240)
        size = 22
        if row.startswith("#"):
            color, size = accent, 26
            row = row[1:]
        d.text((60, y), row, font=font(size), fill=color)
        y += 40

    if time_text:
        d.text((w - 70, h - 96), time_text, font=font(56), fill=(235, 240, 248), anchor="ra")

    out.save(path)
    print(os.path.basename(path))


def main():
    os.makedirs(OUT, exist_ok=True)

    dark_screen(
        os.path.join(OUT, "layoff_mail.png"),
        "邮件 — 人事部",
        [
            "#主题：裁员通知（调整）",
            "发件人：人事部",
            "收件人：陆遥",
            "",
            "上午好：",
            "因业务调整，公司决定对部分岗位进行优化。",
            "你的劳动合同将于本日解除。",
            "在职 1 年 8 个月，补偿按 N+1 执行。",
            "预计补偿金额：96,000 元。",
            "",
            "谢谢你这一年零八个月的工作。",
        ],
    )

    paper(
        os.path.join(OUT, "lease_doc.png"),
        "房屋租赁续约合同",
        [
            "出租方：原房东",
            "承租方：沈岚",
            "房屋地址：临街商铺一层",
            "房屋面积：58 平方米",
            "",
            "原租金：每月 10,000 元",
            "续约租金：每月 18,000 元",
            "付款方式：押二付三（首期 90,000 元）",
            "",
            "期限：下个月十五号之前给准话",
            "逾期未签：十五号后腾房",
        ],
        stamp="合同专用章",
    )

    paper(
        os.path.join(OUT, "offer_letter.png"),
        "录用通知书",
        [
            "陆遥先生：",
            "",
            "我们很高兴地通知您，您已通过面试。",
            "职位：后端开发工程师",
            "月薪：32,000 元（15 薪）",
            "试用期：3 个月",
            "入职日期：下个月一日",
            "工作地点：临江路 88 号",
            "",
            "请在收到本通知后一个月内回复。",
            "星野科技 人力资源部",
        ],
    )

    paper(
        os.path.join(OUT, "letter_xiaoman.png"),
        "给小满",
        [
            "小满：",
            "",
            "如果有一天我不在了，店交给你。",
            "钥匙在底座里。账本在柜台下面。",
            "你做得很好。",
            "不要学我。累了就关门，饿了就吃饭。",
            "",
            "沈岚",
        ],
    )

    paper(
        os.path.join(OUT, "letter_luyao.png"),
        "信",
        [
            "谢谢你每天四点还来。",
            "「留下」那两个字，我写过很多次。",
            "如果我先走了，不要替我扛。",
            "你要好好吃饭。",
        ],
    )

    dark_screen(
        os.path.join(OUT, "screen_347.png"),
        "店铺后台",
        [
            "#今日订单 23",
            "待结算 1,846 元",
            "提交记录",
            "03:46  支付接口修复",
            "03:12  菜单草稿",
            "02:58  租约收据",
            "offer 信  —  未回复",
        ],
        accent=(232, 196, 120),
        time_text="03:47",
    )

    paper(
        os.path.join(OUT, "notebook_page.png"),
        "今天送出去 17 个星星",
        [
            "第 4 位客人问能不能多要一颗，给了。",
            "第 9 位客人说咖啡有点苦，下次少放一点。",
            "",
            "店长要记住：先看人，再看账。",
        ],
    )


if __name__ == "__main__":
    main()
