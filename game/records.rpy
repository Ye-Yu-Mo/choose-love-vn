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
         "text": "小满在桌上摆了座小墓地。她说二十二岁的自己太乖了，想给那样的自己办场葬礼。"},
        {"id": "first_star", "title": "一杯咖啡，一颗星", "short": "第一颗星", "x": 150, "y": 330, "obj": "mem paper star",
         "text": "他第二天又来了，坐在窗边。那之后，十八块的美式就成了他的老样子。"},
        {"id": "card_reader", "title": "刷卡机", "short": "刷卡机", "x": 100, "y": 470, "obj": "mem screwdriver",
         "text": "刷卡机坏了，客人排到门口。他蹲下来指给我看，底下那两根线该拔哪一根。"},
        {"id": "shop_cat", "title": "两个做没用东西的人", "short": "年糕", "x": 280, "y": 540, "obj": "mem cat",
         "text": "打烊后，我在后间捏泥人。一只三花猫从纸箱后探出头，脖子上挂着小满写的牌子，叫年糕。"},
        {"id": "book_margin", "title": "书页边", "short": "书页边", "x": 360, "y": 210, "obj": "mem book",
         "text": "他还回来的星图册上多了几行铅笔字。书里夹着一朵干花，往下看，还能看出被划掉的「留下来」。"},
        {"id": "door_light", "title": "门口的灯", "short": "门口的灯", "x": 520, "y": 260, "obj": "mem paper star",
         "text": "陆遥扶着梯子把松了的线接回去。招牌一亮，门口的水洼也亮了。"},
        {"id": "umbrella", "title": "雨里的伞", "short": "伞", "x": 450, "y": 470, "obj": "mem umbrella",
         "text": "他撑着伞送我回去。走到楼下，我才发现他有半边袖子已经湿透了。"},
        {"id": "lease", "title": "租约", "short": "租约", "x": 620, "y": 380, "obj": "mem lease",
         "text": "房东拿来一份新合同。报价是每月一万八，十五号之前要给个答复。"},
        {"id": "truth_347", "title": "凌晨 3:47", "short": "3:47", "x": 700, "y": 480, "obj": "mem laptop",
         "text": "凌晨 3:47，我回来拿东西，看见他还趴在柜台上，电脑没关。"},
        {"id": "notebook", "title": "小满的本子", "short": "本子", "x": 560, "y": 540, "obj": "mem notebook",
         "text": "小满的本子记了小半本。和妈妈通完电话以后，她问我，如果有一天我不想开了，她能不能当店长。"},
        {"id": "piano", "title": "满天星", "short": "满天星", "x": 390, "y": 330, "obj": "mem paper star",
         "text": "陆遥那天只学会开头一小段。后来他才知道，那首曲子是我写的，叫《满天星》。"},
        {"id": "model", "title": "封好的底座", "short": "底座", "x": 700, "y": 300, "obj": "mem model",
         "text": "我把信和备用钥匙藏进底座。封底的时候胶水挤多了，再想打开，抽屉就拉不动了。"},
        {"id": "keys", "title": "抽屉里的钥匙", "short": "钥匙", "x": 780, "y": 220, "obj": "mem letter key",
         "text": "备用钥匙搁在绒布上，旁边是写给小满的信。"},
        {"id": "argument", "title": "争吵", "short": "争吵", "x": 800, "y": 360, "obj": "mem phone",
         "text": "房东开来的收据上写着陆遥的名字。那天打烊以后，我们把它摊在柜台上说了很久。"},
        {"id": "finale", "title": "合上的琴盖", "short": "琴盖", "x": 900, "y": 270, "obj": "mem piano",
         "text": "原定关店的前一晚，琴盖合着。小满擦着同一只杯子，忽然问我怎么交代起了这么多事。"},
        {"id": "end_together", "title": "结局 — 一起开", "short": "一起开", "x": 1010, "y": 190, "obj": "mem cup",
         "text": "我把琴盖掀开试了几个音。窗边那位常客难得点了杯最贵的。"},
        {"id": "end_xiaoman", "title": "结局 — 朋友一个人开", "short": "一个人开", "x": 1090, "y": 330, "obj": "mem key",
         "text": "小满把账本摊在柜台上，自己想好要接到哪一步，才来拿钥匙。"},
        {"id": "end_depart", "title": "结局 — 她和他走", "short": "和她走", "x": 980, "y": 430, "obj": "mem ticket",
         "text": "陆遥在车站等我。我在大屏上挑了一趟还有两个空位的车。"},
        {"id": "end_alone", "title": "结局 — 没有回头", "short": "没有回头", "x": 1120, "y": 470, "obj": "mem paper star",
         "text": "我一个人买了张车票。小满收到钥匙的时候，车已经快开了。"},
        {"id": "end_funeral", "title": "结局 — 完成葬礼", "short": "完成葬礼", "x": 900, "y": 540, "obj": "mem bouquet",
         "text": "第四天，小满开了门，陆遥带了一束满天星。后来他们清空店里，把钥匙交给了房东。"},
        {"id": "end_white", "title": "结局 — 白夜", "short": "白夜", "x": 1150, "y": 190, "obj": "mem cup",
         "text": "店照旧开门。新合同上的钱，陆遥还在用夜班工钱慢慢填。"},
        {"id": "end_told", "title": "结局 — 如果那天我说了", "short": "说出口", "x": 830, "y": 120, "obj": "mem letter key",
         "text": "三个人把账摊开，想办法把店开得小一点。重开那天，小满在门口的小黑板上写了「营业中」。"},
    ]

    RECORD_BY_ID = {r["id"]: r for r in RECORDS}

    # 二周目「他没说的」视图；id / 星位 / 收集进度都不变
    RECORD_ALT = {
        "funeral": "我推门时，有个女孩在摆一座手工小墓地。我后来才知道，那天她是给自己办葬礼。",
        "first_star": "我看完一整张菜单，还是点了十八块的美式。后来每天四点收电脑，赶去便利店换班。",
        "card_reader": "手是搬货时蹭破的，露出包的那张纸是面试邀约。她一看我，我就低头装作还没收完工具。",
        "shop_cat": "我把转让告示摘下来，往包里一塞。她没叫我贴回去，后来那几道折痕都泛白了。",
        "book_margin": "我在页边写过「留下来」，写完又划掉。她拿书的时候，我瞥见柜台上还有几张催款单。",
        "door_light": "修好招牌那晚，阿哲问我接不接那份 offer。我站在街对面接完电话，她还扶着门等我。",
        "umbrella": "我嘴上说顺路，家其实在店的另一头。先前两晚，我都睡在店里那把靠窗的椅子上。",
        "lease": "我用裁员拿到的补偿垫了她之前欠的租金。房东开收据时，问我跟小沈是什么关系。我说，我在她那儿喝咖啡。",
        "truth_347": "最后一次提交是 3:46。她推门进来时，我趴着，没敢抬头。",
        "notebook": "我跟小满说找到工作了。那份通知还在我包里，我连答复都没给人家。",
        "piano": "最后那个音我早记住了。按错的时候，她还会陪我再弹一遍。",
        "model": "我回来拿充电器，找到了模型底下那个抽屉。沈岚在信里说，她要是哪天不在了，店就交给小满。",
        "keys": "钥匙搁在信封旁。我把信折好放了回去，头一下没能把抽屉推到底。",
        "argument": "她叫我回去拿手机。那晚柜台上除了手机，还有张写着我名字的收据。",
        "finale": "我在门外听见小满在问她话。进去以后，看见柜台上留了封信。",
        "end_together": "小满给我端来菜单上最贵的那杯。沈岚走到窗边，我把新公司的录用通知往她那边推了推。",
        "end_xiaoman": "我提议请小满来谈谈。她翻开账本算了半天，想清楚了才伸手拿钥匙。",
        "end_depart": "她到车站就叫我一起去看车次。还剩两个空位，她伸手指了指屏幕，说就这班。",
        "end_alone": "她说车快开了。我听见电话那头有广播，没听清是哪一站。",
        "end_funeral": "那天我带了束满天星过去，小满从柜台上拿了个空杯子，叫我去接点水。",
        "end_white": "店开下去了。每次给房东转完账，我都在手机上设一个下次转账的提醒。",
        "end_told": "小满翻了新的一页，把我们报的数记下来。后来重挂营业牌那晚，她等我一起锁门。",
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
    $ owned_count = len([i for i in persistent.records if i in RECORD_BY_ID])

    vbox:
        xpos 48
        ypos 36
        spacing 4
        text "星图" size 40 color "#f2ede4" outlines [(3, "#00000088", 0, 0)]
        text "已点亮 [owned_count] / [len(RECORDS)]" size 18 color "#c9b9a3" outlines [(2, "#00000088", 0, 0)]

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

    add Solid("#040814ed")
    key "game_menu" action Hide("record_detail")

    # 点任意处合上
    button:
        xysize (1280, 720)
        background None
        action Hide("record_detail")

    fixed:
        ypos 76
        xysize (1280, 442)
        add "glow warm" xalign 0.5 yalign 0.5 zoom 0.9 at glow_breathe
        if owned:
            add rec["obj"] xalign 0.5 yalign 0.5 xysize (530, 530) fit "contain" at mem_appear
        else:
            add "star dim" xalign 0.5 yalign 0.5 zoom 1.3

    vbox:
        xalign 0.5
        ypos 26
        spacing 2
        text (rec["title"] if owned else "未点亮的星") size 28 color "#f2ede4" xalign 0.5 outlines [(3, "#00000099", 0, 0)]

    frame:
        xalign 0.5
        yalign 0.96
        xsize 826
        background Solid("#161c2c")
        padding (32, 16)
        vbox:
            xalign 0.5
            spacing 8
            if owned and alt_view:
                text "他没说的" size 15 color "#d3b097" xalign 0.5
            text (body if owned else "走到对应的剧情后，这颗星就会亮起来。") size 21 color "#f2ede4" xalign 0.5 xmaximum 762 text_align 0.5
            textbutton "关闭" action Hide("record_detail") xalign 0.5 text_size 17 text_color "#e8c7a8" text_hover_color "#ffffff"


# 调试：直接打开点亮的星图（仅在 --warp 测试时使用）
label test_star_map:
    $ _prev_records = list(persistent.records)
    $ persistent.records = ["funeral", "piano", "model", "keys", "argument", "finale", "end_together", "end_xiaoman"]
    call screen star_map(standalone=True)
    $ persistent.records = _prev_records
    return
