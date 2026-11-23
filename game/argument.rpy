# ============================================================
# 第四章 — 争吵
# 拣爱式：可以拿东西，也可以什么都不拿；
# 可以追问，也可以听；说完之后，复盘。
# ============================================================

default a_heat = 0
default a_choices = []
default a_review = ""
default a_broke = False

# 争执温度（三颗小点）
screen argue_meter():
    zorder 100
    $ dots = 1 if a_heat <= 1 else (2 if a_heat <= 3 else 3)
    frame:
        xalign 0.5
        ypos 14
        background "#00000070"
        padding (16, 6)
        hbox:
            spacing 8
            text "争执" size 14 color "#e8c7a8"
            for i in range(3):
                text ("●" if i < dots else "○") size 12 color ("#c96a5a" if i < dots else "#8a7f74")

# 第一选择：桌上有什么可以拿
screen argue_table():
    modal True
    frame:
        xalign 0.5
        yalign 0.88
        background "#00000090"
        padding (26, 16)
        vbox:
            spacing 12
            text "桌上摊着三样东西。" size 18 color "#e8c7a8" xalign 0.5
            hbox:
                spacing 18
                textbutton "租约" action Return("lease") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "他的手机" action Return("phone") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "水杯" action Return("cup") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "什么也不拿" action Return("nothing") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"

# 复盘：像翻开一本笔记本
screen argue_review():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 820
        background "#f2ede4f2"
        padding (44, 34)
        vbox:
            spacing 20
            text "那天晚上，我记下的三句话。" size 26 color "#3a3226"
            for title, delta, echo in a_choices:
                $ dcolor = "#b0453a" if delta > 0 else ("#3f6b52" if delta < 0 else "#6b5d4a")
                $ dtext = ("+%d" % delta) if delta > 0 else ("%d" % delta)
                vbox:
                    spacing 3
                    hbox:
                        spacing 12
                        text title size 21 color "#3a3226"
                        text dtext size 17 color dcolor
                    text echo size 18 color "#6b5d4a"
            if a_review:
                text a_review size 22 color "#3a3226"
            textbutton "合上本子" action Return() text_size 20 xalign 1.0


label argument_scene:
    $ quick_menu = False
    $ bgm("rain")
    $ a_heat = 0
    $ a_choices = []
    $ a_review = ""
    $ a_broke = False
    scene black with warmfade
    call screen chapter_card("第四章", "争吵", "D-7")

    scene bg shop night with paperdissolve
    show shenlan quiet_half at expr_left with dissolve
    show luyao guilty_half at expr_right with dissolve
    "打烊以后，雨一直没有停。"
    "柜台上摊着一张租约。缴费人一栏，是他的名字。"
    "旁边是他的手机。屏幕还亮着，停在一份菜单草稿上。"
    "最后一次修改，是凌晨三点四十七分。"
    if p_branch == "luyao":
        "三天前，他先看见了那封信。"
        "所以他知道，我本来打算走。"
    "我把他叫回来的时候，他连伞都没拿。"
    luyao "……你看见了。"
    "他站在门口，头发上还是雨。"
    if m11_looked:
        "我想起那天凌晨 3:47 的屏幕。付款人那一栏，是他的名字。"
    if m10_told:
        "那天晚上我告诉他店可能要关了。第二天，他没有来。"
    if m7_star:
        "他电脑包的拉链上，还挂着那颗写着「留下」的星。"
    if m4_ask:
        "我一直在想，他每天四点走，到底去了哪。"
    if m11_confront:
        "那天夜里我叫醒了他。我们隔着一台电脑，谁也没有把话说开。"
    if m10_signed:
        "我签了续租。每个月的数字压在那里，像另一张脸。"
    if m2_talk or m3_ask:
        "他早就告诉过我：「今天开始不用去了」，「最近在休息」。我那时候没有听懂。"

    call screen argue_table
    $ r = _return

    if r == "lease":
        $ a_heat += 2
        $ a_choices.append(("先把租约推过去", 2, "你把最疼的那根刺先递了过去。"))
        shenlan "你什么时候签的？"
        luyao "上个月。"
        shenlan "用你的钱？"
        "他没有否认。"
    elif r == "phone":
        $ a_heat += 1
        $ a_choices.append(("先拿起他的手机", 1, "你想问他几点睡，出口却成了另一句话。"))
        "我拿起他的手机。"
        "凌晨三点四十七分，他还在改店里的菜单。"
        shenlan "你几点睡的？"
        luyao "……记不清了。"
    elif r == "cup":
        $ a_heat -= 1
        $ a_choices.append(("先给他倒一杯水", -1, "你先把水递过去，才把问题递过去。"))
        "我起身，给自己倒水，也给他倒了一杯。"
        "他的手很凉。"
        luyao "……谢谢。"
    else:
        $ a_choices.append(("什么也不拿", 0, "你坐在他对面，等他先开口。"))
        "我在他对面坐下，什么也没拿。"
        "雨声填满了我们中间的空隙。"

    show screen argue_meter
    "他先开口了。"
    luyao "钱是我自己的。工作也是我自己的决定。"
    luyao "我没有动店里的钱。"
    shenlan "那是你的全部。"
    luyao "……我知道。"
    luyao "我只是不想让你走。"

    menu:
        "“你为什么不告诉我？”":
            $ a_heat += 1
            $ a_choices.append(("追问他为什么瞒着", 1, "你要的不是解释，是一个你在里面的位置。"))
            shenlan "你为什么不告诉我？"
            luyao "告诉你，你就不会要。"
            shenlan "所以你就替我决定了？"
        "“你把工作也推了？”":
            $ a_heat += 2
            $ a_choices.append(("质问他推掉的工作", 2, "你听见的不是牺牲，是代价。"))
            shenlan "你连工作都推了？"
            luyao "那个 offer 可以等。"
            shenlan "等不了的是我吗？"
            "他张了张嘴，没有声音。"
        "“你继续说，我听。”":
            $ a_heat -= 1
            $ a_choices.append(("听他把话说完", -1, "你没有打断他。他第一次把账算到了自己身上。"))
            "我没有打断他。"
            "他把每个月的账算给我听，像在汇报一个 bug。"
            "算到最后，他自己停住了。"
            luyao "……我不是想让你欠我。"

    "他说，晚上在便利店做兼职。"
    "他说，等店缓过来，再去找工作。"
    "他说，他什么都不需要我做。"
    "他只是不想让我走。"

    menu:
        "“你有没有想过，我想不想留？”":
            $ a_heat += 1
            $ a_choices.append(("问他有没有问过我", 1, "你终于问出了那句最该早些问的话。"))
            shenlan "你有没有想过，我想不想留？"
            luyao "……"
            shenlan "你留下我，是因为店，还是因为我？"
        "“你凭什么替我决定。”":
            $ a_heat += 2
            $ a_choices.append(("把决定权拍回他脸上", 2, "你想夺回自己的人生，却先伤了他。"))
            shenlan "你凭什么替我决定我的人生？"
            luyao "我没有——"
            shenlan "你有。"
        "“我不知道。”":
            $ a_heat -= 1
            $ a_choices.append(("承认自己也不知道", -1, "你没有把刀递出去。你把手摊开了。"))
            shenlan "我不知道。"
            "这是那天晚上，我说的唯一一句真话。"
            luyao "……我也是。"

    if m9_told or m11_looked:
        "门被推开了一条缝。"
        "小满站在门口，没有进来。"
        xiaoman "……我在外面都听见了。"
        if m9_support:
            xiaoman "老板，你说过我可以当店长的。"
        xiaoman "陆哥，你把自己押上去，我拿什么还？"
        "陆遥没有看她。"
        "她把那本记星星的本子放在门口的地上。"
        "然后转身走了，门没有关。"
    else:
        "门外有脚步声停了一下，又走远了。"

    hide screen argue_meter
    if a_heat <= 1:
        jump argument_calm
    elif a_heat <= 3:
        jump argument_stuck
    else:
        jump argument_break


label argument_calm:
    show shenlan hurt_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    "他坐到我旁边，没有再解释。"
    "我们第一次把话说完。"
    luyao "下次……我先问你。"
    shenlan "嗯。"
    "窗外的雨小了一点。"
    $ a_review = "你停下来的时候，他也停下来了。"
    jump argument_review_scene


label argument_stuck:
    show shenlan quiet_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    "我们谁也没有说服谁。"
    "他把手机扣在桌上，像认错，又像不服。"
    "雨还在下。"
    $ a_review = "你们都说了话，但没有一句真正落到对方那里。"
    jump argument_review_scene


label argument_break:
    show shenlan angry_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    shenlan "你走吧。"
    luyao "……"
    "他把钥匙放在桌上。"
    "门铃响了一声。"
    "雨声把他吞掉了。"
    $ a_broke = True
    $ a_review = "那天晚上，你赢了。你也把他推远了。"
    jump argument_review_scene


label argument_review_scene:
    $ unlock_record("argument")
    scene black with warmfade
    "那天晚上，我在本子上记了三句话。"
    call screen argue_review
    $ quick_menu = True
    if a_broke:
        "钥匙还在桌上。"
    else:
        "他还在。"
    jump finale_scene


