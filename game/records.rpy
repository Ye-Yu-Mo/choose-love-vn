# ============================================================
# 星图 · 记录收集
# 点亮过的记忆会变成夜空里的一颗星，
# 点开星星，记忆的物件浮在夜空里，而不是一张卡片。
# ============================================================

default persistent.records = []

init python:
    RECORDS = [
        {"id": "funeral", "title": "模型葬礼", "short": "葬礼", "x": 240, "y": 430, "obj": "mem rabbit",
         "text": "小满给自己办了一场葬礼。她说，二十二岁的她太乖了，想把她埋掉。"},
        {"id": "first_star", "title": "一杯咖啡，一颗星", "short": "第一颗星", "x": 170, "y": 330, "obj": "mem paper star",
         "text": "他点了最便宜的美式，不加糖。我在碟子边放了一颗写着「撑住」的纸星。他把它放进了口袋。"},
        {"id": "card_reader", "title": "刷卡机", "short": "刷卡机", "x": 120, "y": 500, "obj": "mem screwdriver",
         "text": "刷卡机坏了。他蹲下去，把线拔了又插回去。「程序员还修这个？」「都是修东西。」"},
        {"id": "shop_cat", "title": "两个做没用东西的人", "short": "年糕", "x": 330, "y": 535, "obj": "mem cat",
         "text": "打烊后，我捏泥人，他坐在旁边看。一只三花猫从纸箱后面探出头，牌子上写着「年糕」。"},
        {"id": "piano", "title": "满天星", "short": "满天星", "x": 360, "y": 300, "obj": "mem paper star",
         "text": "那首曲子是她自己写的，叫《满天星》。他学会的第一句旋律，后来才知道名字。"},
        {"id": "model", "title": "封好的底座", "short": "底座", "x": 500, "y": 420, "obj": "mem model",
         "text": "底座比看上去厚。小满说，有些东西不是越用力越开。"},
        {"id": "keys", "title": "抽屉里的钥匙", "short": "钥匙", "x": 600, "y": 290, "obj": "mem letter key",
         "text": "抽屉里是店的钥匙，和一封写给小满的信。她把店留下了，把自己带走了。"},
        {"id": "argument", "title": "凌晨三点四十七分", "short": "3:47", "x": 720, "y": 400, "obj": "mem phone",
         "text": "他的手机停在菜单草稿上，最后一次修改是凌晨三点四十七分。他用自己的全部，换她多留一天。"},
        {"id": "finale", "title": "合上的琴盖", "short": "琴盖", "x": 840, "y": 290, "obj": "mem piano",
         "text": "最后一天，店里没有客人。小满把同一只杯子擦了三遍。钢琴盖合着。"},
        {"id": "end_together", "title": "结局 — 一起开", "short": "一起开", "x": 980, "y": 200, "obj": "mem cup",
         "text": "有些星星，要两个人一起抬头，才看得见。"},
        {"id": "end_xiaoman", "title": "结局 — 朋友一个人开", "short": "一个人开", "x": 1070, "y": 340, "obj": "mem key",
         "text": "店还亮着。她替你留了一盏灯。"},
        {"id": "end_depart", "title": "结局 — 她和他走", "short": "和她走", "x": 950, "y": 450, "obj": "mem ticket",
         "text": "这一次，她不是逃跑，是出发。"},
        {"id": "end_alone", "title": "结局 — 没有回头", "short": "没有回头", "x": 1110, "y": 470, "obj": "mem paper star",
         "text": "她走得很干脆，像从来没有来过。"},
        {"id": "end_funeral", "title": "结局 — 完成葬礼", "short": "完成葬礼", "x": 850, "y": 545, "obj": "mem bouquet",
         "text": "满天星开在她的墓碑前。这一次，是别人替她抬头。"},
    ]

    RECORD_BY_ID = {r["id"]: r for r in RECORDS}

    def unlock_record(rid):
        if rid not in persistent.records:
            persistent.records.append(rid)
            renpy.notify("点亮：%s" % RECORD_BY_ID[rid]["title"])


image bg starry sky = "images/bg/bg_starry_sky.png"
image star lit = "images/ui/star_lit.png"
image star dim = "images/ui/star_dim.png"
image glow warm = "images/ui/glow_warm.png"

image mem rabbit = "images/mem/mem_rabbit.png"
image mem paper star = "images/mem/mem_paper_star.png"
image mem model = "images/mem/mem_model.png"
image mem letter key = "images/mem/mem_letter_key.png"
image mem phone = "images/mem/mem_phone.png"
image mem piano = "images/mem/mem_piano.png"
image mem cup = "images/mem/mem_cup.png"
image mem key = "images/mem/mem_key.png"
image mem ticket = "images/mem/mem_ticket.png"
image mem bouquet = "images/mem/mem_bouquet.png"
image mem screwdriver = "images/mem/mem_screwdriver.png"
image mem cat = "images/mem/mem_cat.png"
image mem book = "images/mem/mem_book.png"
image mem umbrella = "images/mem/mem_umbrella.png"
image mem notebook = "images/mem/mem_notebook.png"
image mem lease = "images/mem/mem_lease.png"
image mem laptop = "images/mem/mem_laptop.png"

# 记忆物件出现：淡入 + 轻微放大（不做持续位移，避免亚像素抖动）
transform mem_appear:
    alpha 0.0 zoom 0.80
    parallel:
        linear 0.7 alpha 1.0
    parallel:
        ease 0.7 zoom 0.82

# 光晕呼吸
transform glow_breathe:
    alpha 0.45
    ease 2.6 alpha 0.62
    ease 2.6 alpha 0.45
    repeat

screen star_map(standalone=False):
    modal True
    zorder 150
    add "bg starry sky"
    add Solid("#050a1499")

    vbox:
        xpos 48
        ypos 36
        spacing 4
        text "星图" size 40 color "#f2ede4" outlines [(3, "#00000088", 0, 0)]
        text "已点亮 [len(persistent.records)] / [len(RECORDS)]" size 18 color "#c9b9a3" outlines [(2, "#00000088", 0, 0)]

    for rec in RECORDS:
        $ owned = rec["id"] in persistent.records
        button:
            xpos rec["x"] - 45
            ypos rec["y"] - 45
            xysize (90, 90)
            background None
            hover_background "#ffffff10"
            action Show("record_detail", rec=rec)
            vbox:
                spacing 0
                xalign 0.5
                if owned:
                    add "star lit" zoom 0.38 xalign 0.5
                    text rec["short"] size 14 color "#e8c7a8" xalign 0.5 outlines [(2, "#00000088", 0, 0)]
                else:
                    add "star dim" zoom 0.28 xalign 0.5

    frame:
        xalign 0.98
        ypos 32
        background "#00000070"
        padding (20, 10)
        textbutton "合上星图" action (Return() if standalone else Hide("star_map")) text_size 18 text_color "#f2ede4" text_hover_color "#e8c7a8"


screen record_detail(rec):
    modal True
    zorder 160
    $ owned = rec["id"] in persistent.records

    add Solid("#040814bb")

    # 点任意处合上
    button:
        xysize (1280, 720)
        background None
        action Hide("record_detail")

    if owned:
        add "glow warm" xalign 0.5 ypos 30 zoom 1.18 at glow_breathe
        add rec["obj"] xalign 0.5 ypos 78 at mem_appear
    else:
        add "glow warm" xalign 0.5 ypos 130 zoom 0.8 alpha 0.22
        add "star dim" xalign 0.5 ypos 230 zoom 1.3

    vbox:
        xalign 0.5
        ypos 26
        spacing 2
        text (rec["title"] if owned else "未点亮的星") size 28 color "#f2ede4" xalign 0.5 outlines [(3, "#00000099", 0, 0)]

    vbox:
        xalign 0.5
        ypos 566
        spacing 10
        text (rec["text"] if owned else "再走走看。有些记忆，要先把路走到那里。") size 20 color "#d8cfc2" xalign 0.5 xmaximum 780 text_align 0.5 outlines [(2, "#00000099", 0, 0)]
        text "点一下，把它放回去" size 13 color "#8a7f74" xalign 0.5


# 调试：直接打开点亮的星图（仅在 --warp 测试时使用）
label test_star_map:
    $ _prev_records = list(persistent.records)
    $ persistent.records = ["funeral", "piano", "model", "keys", "argument", "finale", "end_together", "end_xiaoman"]
    call screen star_map(standalone=True)
    $ persistent.records = _prev_records
    return