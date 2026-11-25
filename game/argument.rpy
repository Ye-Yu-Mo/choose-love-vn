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
            text "桌上摊着几样东西。" size 18 color "#e8c7a8" xalign 0.5
            hbox:
                spacing 18
                textbutton "租约" action Return("lease") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "他的手机" action Return("phone") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "水杯" action Return("cup") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "什么也不拿" action Return("nothing") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"

# 二周目：桌面选择（陆遥的视角）
screen argue_table_luyao():
    modal True
    frame:
        xalign 0.5
        yalign 0.88
        background "#00000090"
        padding (26, 16)
        vbox:
            spacing 12
            text "桌上摊着几样东西。" size 18 color "#e8c7a8" xalign 0.5
            hbox:
                spacing 18
                textbutton "把租约推过去" action Return("lease") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "拿起手机" action Return("phone") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "给她倒杯水" action Return("cup") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "什么也不做" action Return("nothing") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"

# 复盘：像翻开一本笔记本
screen argue_review():
    modal True
    button:
        xysize (1280, 720)
        background None
        action Return()
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 820
        background "#f2ede4f2"
        padding (44, 34)
        vbox:
            spacing 20
            text ("那天晚上，她记下的三个选择。" if pov == "luyao" else "那天晚上，我做的三个选择。") size 26 color "#3a3226"
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
            textbutton "合上本子" action Return() text_size 20 text_color "#3a2c1e" text_hover_color "#8a4a20" xalign 1.0


label argument_scene:
    $ quick_menu = False
    $ bgm("rain")
    $ a_heat = 0
    $ a_choices = []
    $ a_review = ""
    $ a_broke = False
    scene black with warmfade
    call screen chapter_card("第四章", "争吵", "距关店 7 天")

    scene bg shop night with paperdissolve
    show fx lamp night
    show shenlan quiet_half at expr_left with dissolve
    show luyao guilty_half at expr_right with dissolve
    if pov == "luyao":
        "打烊以后，雨一直没有停。"
        "柜台上摊着一张租约。缴费人一栏，是我的名字。"
        "旁边是我的手机。屏幕还亮着，停在一份菜单草稿上。"
        "最后一次修改，是凌晨三点四十七分。"
        if p_branch == "luyao_seen":
            "三天前，我先打开了模型。我知道她打算走。"
        if f_asked:
            "我第一次来的时候，说自己只是「路过」。她没有拆穿。"
        if f_piano == "teach":
            "我想起她教我时，说手腕放松一点。"
        elif f_piano == "tease":
            "我想起她说我在敲代码。"
        elif f_piano == "try":
            "我想起她退后半步，让我自己按对。"
        "她把我叫回来。我连伞都没拿。"
        voice "audio/voice/argument_124.ogg"
        luyao "……你看见了。"
        "我站在门口，头发上还是雨。"
        if l_awake:
            "那天夜里她看见我醒着。我们坐到天亮，谁也没有把话说透。"
        elif l_lease_told:
            "她早就知道我付了租约。所以今晚，她没有问钱从哪来。"
        else:
            "她应该还不知道。在她眼里，我大概只是每天来喝咖啡。"
        if m7_star:
            "我电脑包的拉链上，还挂着那颗写着「留下」的星。"
        if l_four_told:
            "她知道我四点去便利店。"
        if m2_talk:
            "我早就告诉过她：「从昨天开始，不用去了」。"
        if m3_ask:
            "我早就告诉过她：「最近在休息」。"
    else:
        "打烊以后，雨一直没有停。"
        "柜台上摊着一张租约。缴费人一栏，是他的名字。"
        "旁边是他的手机。屏幕还亮着，停在一份菜单草稿上。"
        "最后一次修改，是凌晨三点四十七分。"
        if p_branch == "luyao":
            "三天前，他先看见了那封信。"
            "所以他知道，我本来打算走。"
        if f_asked:
            "他第一次来的时候，说自己只是「路过」。"
        if f_piano == "teach":
            "我想起我教他时，说手腕放松一点。"
        elif f_piano == "tease":
            "我想起自己说他在敲代码。"
        elif f_piano == "try":
            "我想起自己退后半步，让他自己按对。"
        "我把他叫回来的时候，他连伞都没拿。"
        voice "audio/voice/argument_157.ogg"
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
        if m2_talk:
            "他早就告诉过我：「从昨天开始，不用去了」。"
        if m3_ask:
            "他早就告诉过我：「最近在休息」。"

    if pov == "luyao":
        call screen argue_table_luyao
    else:
        call screen argue_table
    $ r = _return

    if r == "lease":
        $ a_heat += 2
        $ a_choices.append(("把租约推过去" if pov == "luyao" else "先把租约推过去", 2, "你把最疼的那根刺先递了过去。"))
        voice "audio/voice/argument_185.ogg"
        shenlan "你什么时候签的？"
        voice "audio/voice/argument_186.ogg"
        luyao "上个月。"
        if pov == "luyao" and l_lease_told:
            voice "audio/voice/argument_188.ogg"
            shenlan "你把钱都垫进去了？"
        else:
            voice "audio/voice/argument_190.ogg"
            shenlan "用你的钱？"
        if pov == "luyao":
            "我没有否认。"
        else:
            "他没有否认。"
    elif r == "phone":
        $ a_heat += 1
        $ a_choices.append(("拿起手机" if pov == "luyao" else "先拿起他的手机", 1, "你想说「我没睡」，出口却成了另一句话。"))
        if pov == "luyao":
            "我把手机翻过来，屏幕还停在 3:47。"
            "店铺后台的提交记录一条一条往下排。"
        else:
            "我拿起他的手机。"
            "凌晨三点四十七分，他还在改店里的菜单。"
        voice "audio/voice/argument_204.ogg"
        shenlan "你几点睡的？"
        voice "audio/voice/argument_205.ogg"
        luyao "……记不清了。"
    elif r == "cup":
        $ a_heat -= 1
        $ a_choices.append(("给她倒了一杯水" if pov == "luyao" else "先给他倒一杯水", -1, "你先把水递过去，才把问题递过去。"))
        if pov == "luyao":
            "我起身，给她倒了一杯水。"
            "她的手很凉。"
            voice "audio/voice/argument_212.ogg"
            shenlan "……谢谢。"
        else:
            "我起身，给自己倒水，也给他倒了一杯。"
            "他的手很凉。"
            voice "audio/voice/argument_216.ogg"
            luyao "……谢谢。"
    else:
        $ a_choices.append(("什么也不做" if pov == "luyao" else "什么也不拿", 0, "你坐在对面，等她先开口。"))
        if pov == "luyao":
            "我在她对面坐下，什么也没拿。"
            "雨声很大。我们隔着桌子坐了一会儿。"
        else:
            "我在他对面坐下，什么也没拿。"
            "雨声很大。我们隔着桌子坐了一会儿。"

    show screen argue_meter
    if pov == "luyao":
        "我先开口了。"
    else:
        "他先开口了。"
    voice "audio/voice/argument_231.ogg"
    luyao "钱是我自己的。工作也是我自己的决定。"
    voice "audio/voice/argument_232.ogg"
    luyao "我没有动店里的钱。"
    voice "audio/voice/argument_233.ogg"
    shenlan "那是你的全部。"
    voice "audio/voice/argument_234.ogg"
    luyao "……我知道。"
    voice "audio/voice/argument_235.ogg"
    luyao "我只是不想让你走。"

    if pov == "luyao":
        menu:
            "说「我不会走」。":
                $ a_heat += 1
                $ a_choices.append(("说「我不会走」", 1, "你把最硬的那句话先说了出去。"))
                voice "audio/voice/argument_242.ogg"
                luyao "我不会走。"
                voice "audio/voice/argument_243.ogg"
                shenlan "你拿什么保证？"
                voice "audio/voice/argument_244.ogg"
                luyao "……我不知道。"
                voice "audio/voice/argument_245.ogg"
                shenlan "所以你就替我决定了？"
            "先解释那个 offer。":
                $ a_heat += 2
                $ a_choices.append(("先解释 offer", 2, "你听见的不是牺牲，是代价。"))
                voice "audio/voice/argument_249.ogg"
                luyao "那个 offer 可以等。"
                voice "audio/voice/argument_250.ogg"
                shenlan "等不了的是我吗？"
                "我张了张嘴，没有声音。"
            "先听她说完。":
                $ a_heat -= 1
                $ a_choices.append(("先听她说完", -1, "你没有打断她。她第一次把账算到了自己身上。"))
                "我没有打断她。"
                "她把每个月的账算给我听，像在汇报一个 bug。"
                "算到最后，她自己停住了。"
                voice "audio/voice/argument_258.ogg"
                luyao "……我不是想让你欠我。"
    else:
        menu:
            "“你为什么不告诉我？”":
                $ a_heat += 1
                $ a_choices.append(("追问他为什么瞒着", 1, "你要的不是解释，是一个你在里面的位置。"))
                voice "audio/voice/argument_264.ogg"
                shenlan "你为什么不告诉我？"
                voice "audio/voice/argument_265.ogg"
                luyao "告诉你，你就不会要。"
                voice "audio/voice/argument_266.ogg"
                shenlan "所以你就替我决定了？"
            "“你把工作也推了？”":
                $ a_heat += 2
                $ a_choices.append(("质问他推掉的工作", 2, "你听见的不是牺牲，是代价。"))
                voice "audio/voice/argument_270.ogg"
                shenlan "你连工作都推了？"
                voice "audio/voice/argument_271.ogg"
                luyao "那个 offer 可以等。"
                voice "audio/voice/argument_272.ogg"
                shenlan "等不了的是我吗？"
                "他张了张嘴，没有声音。"
            "“你继续说，我听。”":
                $ a_heat -= 1
                $ a_choices.append(("听他把话说完", -1, "你没有打断他。他第一次把账算到了自己身上。"))
                "我没有打断他。"
                "他把每个月的账算给我听，像在汇报一个 bug。"
                "算到最后，他自己停住了。"
                voice "audio/voice/argument_280.ogg"
                luyao "……我不是想让你欠我。"

    if pov == "luyao":
        "我说，晚上在便利店做兼职。"
        "我说，等店缓过来，再去找工作。"
        "我说，你不用替我做什么。"
        "我就是不想让你走。"
    else:
        "他说，晚上在便利店做兼职。"
        "他说，等店缓过来，再去找工作。"
        "他说，他什么都不需要我做。"
        "他只是不想让我走。"

    if pov == "luyao":
        menu:
            "问她愿不愿意留下。":
                $ a_heat += 1
                $ a_choices.append(("问她愿不愿意留下", 1, "你终于问出了那句最该早些问的话。"))
                voice "audio/voice/argument_298.ogg"
                luyao "你有没有想过，你愿不愿意留？"
                voice "audio/voice/argument_299.ogg"
                shenlan "……"
                voice "audio/voice/argument_300.ogg"
                luyao "你留下，是因为店，还是因为我？"
            "说「我会把钱还上」。":
                $ a_heat += 2
                $ a_choices.append(("说「我会把钱还上」", 2, "你想把关系算清，却先把她推远。"))
                voice "audio/voice/argument_304.ogg"
                luyao "钱我会还上。"
                voice "audio/voice/argument_305.ogg"
                shenlan "我不是在跟你要钱。"
                "她说完，自己先愣住了。"
            "承认不知道。":
                $ a_heat -= 1
                $ a_choices.append(("承认不知道", -1, "你没有把刀递出去。你把手摊开了。"))
                voice "audio/voice/argument_310.ogg"
                luyao "我不知道。"
                voice "audio/voice/argument_311.ogg"
                shenlan "……我也是。"
                "这是那天晚上，她第一次没有绕开。"
    else:
        menu:
            "“你有没有想过，我想不想留？”":
                $ a_heat += 1
                $ a_choices.append(("问他有没有问过我", 1, "你终于问出了那句最该早些问的话。"))
                voice "audio/voice/argument_318.ogg"
                shenlan "你有没有想过，我想不想留？"
                voice "audio/voice/argument_319.ogg"
                luyao "……"
                voice "audio/voice/argument_320.ogg"
                shenlan "你留下我，是因为店，还是因为我？"
            "“你凭什么替我决定。”":
                $ a_heat += 2
                $ a_choices.append(("把决定权拍回他脸上", 2, "你想夺回自己的人生，却先伤了他。"))
                voice "audio/voice/argument_324.ogg"
                shenlan "你凭什么替我决定我的人生？"
                voice "audio/voice/argument_325.ogg"
                luyao "我没有——"
                voice "audio/voice/argument_326.ogg"
                shenlan "你有。"
            "“我不知道。”":
                $ a_heat -= 1
                $ a_choices.append(("承认自己也不知道", -1, "你没有把刀递出去。你把手摊开了。"))
                voice "audio/voice/argument_330.ogg"
                shenlan "我不知道。"
                "这是那天晚上，我说的唯一一句真话。"
                voice "audio/voice/argument_332.ogg"
                luyao "……我也是。"

    if pov == "luyao" and a_heat <= 3:
        menu:
            "说真话。":
                $ l_truth = True
                $ a_heat -= 1
                voice "audio/voice/argument_339.ogg"
                luyao "租约是我付的。offer 我也推了。"
                voice "audio/voice/argument_340.ogg"
                luyao "我每天晚上在这里改菜单，白天去便利店。"
                voice "audio/voice/argument_341.ogg"
                luyao "我不是想让你欠我。我是怕你走。"
                voice "audio/voice/argument_342.ogg"
                shenlan "……你为什么不早说？"
                voice "audio/voice/argument_343.ogg"
                luyao "因为说了，你就走了。"
                "说完，我把视线移开。"
            "用「我只是想帮你」挡。":
                voice "audio/voice/argument_346.ogg"
                luyao "我只是想帮你。"
                "她没有说话。"
                "我知道这句话挡不住什么。"

    if m9_told or m11_looked or l_truth or p_branch == "xiaoman":
        "门被推开了一条缝。"
        "小满站在门口，没有进来。"
        voice "audio/voice/argument_353.ogg"
        xiaoman "……我在外面都听见了。"
        if m9_support:
            if pov == "luyao":
                voice "audio/voice/argument_356.ogg"
                xiaoman "陆哥，你说过我可以当店长的。"
            else:
                voice "audio/voice/argument_358.ogg"
                xiaoman "老板，你说过我可以当店长的。"
        voice "audio/voice/argument_359.ogg"
        xiaoman "陆哥，你把自己押上去，我拿什么还？"
        if pov == "luyao":
            "我没有看她。"
        else:
            "他没有看她。"
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
    if pov == "luyao":
        "她坐到我旁边，没有再解释。"
        "我们第一次把话说完。"
    else:
        "他坐到我旁边，没有再解释。"
        "我们第一次把话说完。"
    voice "audio/voice/argument_387.ogg"
    luyao "下次……我先问你。"
    voice "audio/voice/argument_388.ogg"
    shenlan "嗯。"
    "窗外的雨小了一点。"
    if pov == "luyao":
        $ a_review = "你停下来的时候，她也停下来了。"
    else:
        $ a_review = "你停下来的时候，他也停下来了。"
    jump argument_review_scene


label argument_stuck:
    show shenlan quiet_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    "我们谁也没有说服谁。"
    if pov == "luyao":
        "我把手机扣在桌上，屏幕朝下。先不看了。"
    else:
        "他把手机扣在桌上，屏幕朝下。没再说话。"
    "雨还在下。"
    $ a_review = "你们都说了话，但没有一句真正落到对方那里。"
    jump argument_review_scene


label argument_break:
    show shenlan angry_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    voice "audio/voice/argument_413.ogg"
    shenlan "你走吧。"
    voice "audio/voice/argument_414.ogg"
    luyao "……"
    if pov == "luyao":
        "我把钥匙放在桌上。"
        "门铃响了一声。"
        "我推门出去，雨落在肩上。"
    else:
        "他把钥匙放在桌上。"
        "门铃响了一声。"
        "他推门出去，雨落在肩上。"
    $ a_broke = True
    if pov == "luyao":
        $ a_review = "那天晚上，你赢了。你也把她推远了。"
    else:
        $ a_review = "那天晚上，你赢了。你也把他推远了。"
    jump argument_review_scene


label argument_review_scene:
    $ unlock_record("argument")
    scene black with warmfade
    if pov == "luyao":
        "那天晚上，她在本子上记了三个选择。"
    else:
        "那天晚上，我在本子上记了三个选择。"
    call screen argue_review
    $ quick_menu = True
    if a_broke:
        if pov == "luyao":
            "我的钥匙还在桌上。"
        else:
            "钥匙还在桌上。"
    else:
        if pov == "luyao":
            "我还在。"
        else:
            "他还在。"
    if pov == "luyao" and l_truth:
        jump ending_told
    jump finale_scene


