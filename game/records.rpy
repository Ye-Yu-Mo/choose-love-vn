# ============================================================
# 星图 · 记录收集
# 点亮过的记忆会变成夜空里的一颗星，
# 点开星星，记忆的物件浮在夜空里，而不是一张卡片。
# ============================================================

default persistent.records = []
default persistent.star_view = "her"

init python:
    RECORDS = [
        {"id": "funeral", "title": "模型葬礼", "short": "葬礼", "x": 230, "y": 430, "obj": "mem rabbit",
         "text": "小满给自己办了一场葬礼。她说，二十二岁的她太乖了，想把她埋掉。"},
        {"id": "first_star", "title": "一杯咖啡，一颗星", "short": "第一颗星", "x": 150, "y": 330, "obj": "mem paper star",
         "text": "他点了最便宜的美式，不加糖。我在碟子边放了一颗写着「撑住」的纸星。他把它放进了口袋。"},
        {"id": "card_reader", "title": "刷卡机", "short": "刷卡机", "x": 100, "y": 470, "obj": "mem screwdriver",
         "text": "刷卡机坏了。他蹲下去，把线拔了又插回去。「程序员还修这个？」「都是修东西。」"},
        {"id": "shop_cat", "title": "两个做没用东西的人", "short": "年糕", "x": 280, "y": 540, "obj": "mem cat",
         "text": "打烊后，我捏泥人，他坐在旁边看。一只三花猫从纸箱后面探出头，牌子上写着「年糕」。"},
        {"id": "book_margin", "title": "书页边", "short": "书页边", "x": 360, "y": 210, "obj": "mem book",
         "text": "他把书还回来时，页边多了一行铅笔字。书里夹着一朵压干的满天星，还有一行被划掉的「留下来」。"},
        {"id": "door_light", "title": "门口的灯", "short": "门口的灯", "x": 520, "y": 260, "obj": "mem paper star",
         "text": "他修好了店招的灯。我给了他一颗写着「留下」的星，他挂在了电脑包上。我们谁也没有说破。"},
        {"id": "umbrella", "title": "雨里的伞", "short": "伞", "x": 450, "y": 470, "obj": "mem umbrella",
         "text": "他撑着伞送我回家，伞一直往我这边偏。到楼下，他站了很久，只说了一句「你早点睡」。"},
        {"id": "lease", "title": "租约", "short": "租约", "x": 620, "y": 380, "obj": "mem lease",
         "text": "房东说楼要卖了，租金按市价，下个月十五号之前给准话。我把报价单和欠款单叠在一起，压在柜台最里面。"},
        {"id": "truth_347", "title": "凌晨 3:47", "short": "3:47", "x": 700, "y": 480, "obj": "mem laptop",
         "text": "他趴在柜台上睡着了，电脑亮着 3:47。支付后台、提交记录、offer、租约收据——付款人那一栏是他的名字。"},
        {"id": "notebook", "title": "小满的本子", "short": "本子", "x": 560, "y": 540, "obj": "mem notebook",
         "text": "「今天送出去 17 个星星。」她记了小半本。挂掉妈妈的电话以后，她说：「如果有一天你不想开了，我可以当店长。」"},
        {"id": "piano", "title": "满天星", "short": "满天星", "x": 390, "y": 330, "obj": "mem paper star",
         "text": "那首曲子是她自己写的，叫《满天星》。他学会的第一句旋律，后来才知道名字。"},
        {"id": "model", "title": "封好的底座", "short": "底座", "x": 700, "y": 300, "obj": "mem model",
         "text": "底座比看上去厚。小满说，有些东西不是越用力越开。"},
        {"id": "keys", "title": "抽屉里的钥匙", "short": "钥匙", "x": 780, "y": 220, "obj": "mem letter key",
         "text": "抽屉里是店的钥匙，和一封写给小满的信。她把店留下了，把自己带走了。"},
        {"id": "argument", "title": "争吵", "short": "争吵", "x": 800, "y": 360, "obj": "mem phone",
         "text": "他用自己的全部，换她多留一天。那天晚上，我们把最难说的话都说了。"},
        {"id": "finale", "title": "合上的琴盖", "short": "琴盖", "x": 900, "y": 270, "obj": "mem piano",
         "text": "最后一天，店里没有客人。小满把同一只杯子擦了三遍。钢琴盖合着。"},
        {"id": "end_together", "title": "结局 — 一起开", "short": "一起开", "x": 1010, "y": 190, "obj": "mem cup",
         "text": "有些星星，要两个人一起抬头，才看得见。"},
        {"id": "end_xiaoman", "title": "结局 — 朋友一个人开", "short": "一个人开", "x": 1090, "y": 330, "obj": "mem key",
         "text": "店还亮着。她替你留了一盏灯。"},
        {"id": "end_depart", "title": "结局 — 她和他走", "short": "和她走", "x": 980, "y": 430, "obj": "mem ticket",
         "text": "这一次，她不是逃跑，是出发。"},
        {"id": "end_alone", "title": "结局 — 没有回头", "short": "没有回头", "x": 1120, "y": 470, "obj": "mem paper star",
         "text": "她走得很干脆，像从来没有来过。"},
        {"id": "end_funeral", "title": "结局 — 完成葬礼", "short": "完成葬礼", "x": 900, "y": 540, "obj": "mem bouquet",
         "text": "满天星开在她的墓碑前。这一次，是别人替她抬头。"},
        {"id": "end_white", "title": "结局 — 白夜", "short": "白夜", "x": 1150, "y": 190, "obj": "mem cup",
         "text": "店保住了，债在他身上。灯还亮着，可有些东西从那天晚上起就没有再平过。"},
        {"id": "end_told", "title": "结局 — 如果那天我说了", "short": "说出口", "x": 830, "y": 120, "obj": "mem letter key",
         "text": "那天他把赔偿金、offer、夜班一次说完。店小了，但我们都在。"},
    ]

    RECORD_BY_ID = {r["id"]: r for r in RECORDS}

    # 二周目「他没说的」视图；id / 星位 / 收集进度都不变
    RECORD_ALT = {
        "funeral": "我推门进去的时候，看见一个女孩在给自己办葬礼。她抬起头，眼睛很亮，亮得有点用力。",
        "first_star": "我点了最便宜的美式，因为钱要留着。她在碟子边放了一颗写着「撑住」的星。那天之后，我每天四点走，去便利店换班。",
        "card_reader": "手背上的伤是昨天搬货划的。包里那角纸，是我还没签的 offer。她笑的时候，我没敢多看。",
        "shop_cat": "她每天进门都会先看那块「转让」牌。我把它摘下来，是不想让她再看见。四点我得去换班，一小时多十二块。",
        "book_margin": "我在页边写了「留下来」，又划掉。书下面压着她的欠款单。我看见了，没有问。",
        "door_light": "灯亮的时候，她在灯下看我。电话是阿哲打来的，我说再想想。包上那颗星，让我第一次觉得可以不用想。",
        "umbrella": "我只带了一把伞，往她那边偏。我在店里睡了两晚，不敢上去。",
        "lease": "房东的办公室在隔壁街。我用赔偿金付了欠租。他问我跟她什么关系，我说，我是她店里的客人。",
        "truth_347": "三点四十我就醒了。她回来过，我听见了。",
        "notebook": "我骗小满说找到了工作。我问房东最近来过没有，是在算还能替她付多少。",
        "piano": "最后一个音我是故意按错的。我想让她再教一次。",
        "model": "我拨开土，打开抽屉。信上写着：如果我不在了，店交给你。她真的要走。",
        "keys": "抽屉里是店的钥匙，和一封写给她的信。我把信放回去，手一直在抖。",
        "argument": "我用自己的全部换她多留一天。她问「你为什么不告诉我」。因为告诉了她，她就走了。",
        "finale": "最后一天，我拿着信站在门外。雨停了。",
        "end_together": "她留下了。这一次，我先问她愿不愿意让我留。",
        "end_xiaoman": "她把钥匙交给小满。我没有拦她，只是把伞留在了门口。",
        "end_depart": "她跟我走了。这一次，她没有逃，是出发。",
        "end_alone": "她一个人走的。我在车站等到最后一班车开走。",
        "end_funeral": "我没能把她留下。那天之后，店里空了三天。",
        "end_white": "她留下了。可账还在我身上，我们都假装没有看见。",
        "end_told": "那天我把所有的事都说了。她没有走。店小了，但我们第一次站在同一边。",
    }

    def set_star_view(view):
        persistent.star_view = view
        renpy.restart_interaction()

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

    if persistent.cleared_pov:
        hbox:
            xalign 0.5
            ypos 42
            spacing 10
            textbutton "她看到的" action Function(set_star_view, "her") text_size 17 text_color ("#e8c7a8" if persistent.star_view == "her" else "#8a7f74") text_hover_color "#f2ede4"
            text "|" size 16 color "#5a5248"
            textbutton "他没说的" action Function(set_star_view, "him") text_size 17 text_color ("#e8c7a8" if persistent.star_view == "him" else "#8a7f74") text_hover_color "#f2ede4"

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
    $ alt_view = persistent.cleared_pov and persistent.star_view == "him"
    $ body = RECORD_ALT.get(rec["id"], rec["text"]) if alt_view else rec["text"]

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
        if owned and alt_view:
            text "他没说的" size 13 color "#8a7f74" xalign 0.5
        text (body if owned else "再走走看。有些记忆，要先把路走到那里。") size 20 color "#d8cfc2" xalign 0.5 xmaximum 780 text_align 0.5 outlines [(2, "#00000099", 0, 0)]
        text "点一下，把它放回去" size 13 color "#8a7f74" xalign 0.5


# 调试：直接打开点亮的星图（仅在 --warp 测试时使用）
label test_star_map:
    $ _prev_records = list(persistent.records)
    $ persistent.records = ["funeral", "piano", "model", "keys", "argument", "finale", "end_together", "end_xiaoman"]
    call screen star_map(standalone=True)
    $ persistent.records = _prev_records
    return