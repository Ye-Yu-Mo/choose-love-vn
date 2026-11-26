# ============================================================
# 第四章 — 争吵
# 拣爱式：可以拿东西，也可以什么都不拿；
# 可以追问，也可以听；说完之后，复盘。
# ============================================================

default a_heat = 0
default a_choices = []
default a_review = ""
default a_broke = False
define a_truth_entry = ("说清楚我为什么瞒着她", "你说你其实想接那份工作，也终于说了自己为什么一直等。")

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
                textbutton "房租收据" action Return("lease") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
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
                textbutton "把收据推过去" action Return("lease") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "拿起手机" action Return("phone") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "给她倒杯水" action Return("cup") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "先坐一会儿" action Return("nothing") text_size 22 text_color "#f2ede4" text_hover_color "#e8c7a8"

# 复盘：像翻开一本笔记本
screen argue_review():
    modal True
    $ entries = a_choices
    if l_truth and len(a_choices) == 3:
        $ entries = a_choices + [a_truth_entry]
    button:
        xysize (1280, 720)
        background None
        action Return()
    frame:
        xalign 0.5
        yalign 0.5
        xsize 810
        background "#f2ede4f2"
        padding (42, 30)
        vbox:
            xfill True
            spacing 15
            text "那天晚上" size 26 color "#3a3226"
            # 旧存档的条目在标题和正文之间还有一项分数。
            for entry in entries:
                vbox:
                    spacing 3
                    text entry[0] size 21 color "#3a3226"
                    text entry[-1] size 18 color "#6b5d4a"
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
        voice ("audio/voice/narr_shenlan_d997e708a6afe2b3490c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d997e708a6afe2b3490c.ogg")
        voice ("audio/voice/narr_shenlan_d997e708a6afe2b3490c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d997e708a6afe2b3490c.ogg")
        "她发消息让我回店里一趟。我以为又有东西坏了，出门时连伞都没拿。"
        voice ("audio/voice/narr_shenlan_7367123106115006670c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7367123106115006670c.ogg")
        voice ("audio/voice/narr_shenlan_7367123106115006670c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7367123106115006670c.ogg")
        "一进门，我就看见了房东开的收据。付款人一栏是我的名字。"
        voice ("audio/voice/narr_shenlan_3d04d60ed78ca020f2ec.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3d04d60ed78ca020f2ec.ogg")
        "柜台上还有我忘拿的手机。我认得那份菜单草稿，手机是我刚才拿来对版用的。"
        voice ("audio/voice/narr_shenlan_649e9399960b1d7c819c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_649e9399960b1d7c819c.ogg")
        "上面显示上次修改是 3:47。"
        if p_branch == "luyao_seen":
            voice ("audio/voice/narr_shenlan_6d58ff093fe97ae3dd4f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6d58ff093fe97ae3dd4f.ogg")
            "我前几天看过模型里那封信。到现在也没敢问她，日历上到底圈的是哪一天。"
        if f_asked:
            voice ("audio/voice/narr_shenlan_31161634672b2932d7c5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_31161634672b2932d7c5.ogg")
            "第一天我还跟她说，自己是路过。"
        if f_piano == "teach":
            voice ("audio/voice/narr_shenlan_b26a0c60fafe7bde5849.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b26a0c60fafe7bde5849.ogg")
            "学琴那天，她一遍遍叫我把手腕放松。我这会儿才发现我一直攥着包带。"
        elif f_piano == "tease":
            voice ("audio/voice/narr_shenlan_ec5af3b856c4eab4c985.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ec5af3b856c4eab4c985.ogg")
            "她笑我弹琴像敲代码那天，我们也是打烊以后才开始说话。"
        elif f_piano == "try":
            voice ("audio/voice/narr_shenlan_5424713a9878bb9fb56b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5424713a9878bb9fb56b.ogg")
            "我想起学琴那天，她在旁边等我自己把音找出来。那回她肯等我。"
        voice ("audio/voice/narr_shenlan_740b3cfc5c9238b0c4e1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_740b3cfc5c9238b0c4e1.ogg")
        "我把电脑包放下来，湿了的包带在柜台上印了道水痕。"
        voice "audio/voice/argument_124.ogg"
        luyao "……你看见了。"
        voice ("audio/voice/narr_shenlan_8e66818ae4474e0c7984.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e66818ae4474e0c7984.ogg")
        "我往屋里走了一步。她没过来接我的包。"
        if l_awake:
            voice ("audio/voice/narr_shenlan_3fac530a2ba9a8baceef.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3fac530a2ba9a8baceef.ogg")
            "上次她半夜回来，我们好歹一起坐到了天亮。这回她一直站在柜台那一边。"
        elif l_lease_told:
            voice ("audio/voice/narr_shenlan_3ec165626b8468120f7d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3ec165626b8468120f7d.ogg")
            "我早跟她说过欠租的事。她现在才看到具体数目。"
        else:
            voice ("audio/voice/narr_shenlan_6691066102b5145c8899.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6691066102b5145c8899.ogg")
            "我本来打算等房东那边有了准话再说。现在也用不着挑时间了。"
        if m7_star:
            voice ("audio/voice/narr_shenlan_96ae32a8a7f20404d4d5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_96ae32a8a7f20404d4d5.ogg")
            "包上那颗「留下」蹭到了桌沿，我下意识把它扶了一下。"
        if l_four_told:
            voice ("audio/voice/narr_shenlan_62b7e247e4451bd51a76.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_62b7e247e4451bd51a76.ogg")
            "便利店的事她知道，只是不知道我把工钱攒下来做什么。"
        if m7_phone:
            voice ("audio/voice/narr_shenlan_f9557fd4c5e237d235c0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f9557fd4c5e237d235c0.ogg")
            "阿哲的电话我告诉过她。后来拒掉那份工作，我也只给阿哲回了一条消息。"
        if m2_talk:
            voice ("audio/voice/narr_shenlan_cb3c9ce50597ea392792.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cb3c9ce50597ea392792.ogg")
            "我头一回和她提起被裁的时候，她问我以后还来不来喝咖啡。"
        if m3_ask:
            voice ("audio/voice/narr_shenlan_d531d2282e0a6c23e866.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d531d2282e0a6c23e866.ogg")
            "修机器那天，我还跟她说，我最近在休息。"
    else:
        voice ("audio/voice/narr_shenlan_928217f933439cd4262e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_928217f933439cd4262e.ogg")
        "打烊前房东送了收据来，说之前欠的那笔已经有人付过了。"
        voice ("audio/voice/narr_shenlan_86a22064530dc30c222c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_86a22064530dc30c222c.ogg")
        "我盯着付款人那一栏找了半天，才敢认是陆遥的名字。"
        voice ("audio/voice/narr_shenlan_98676394601b37bb1257.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_98676394601b37bb1257.ogg")
        "他手机落在柜台上，屏幕还没灭。我看见上面开着店里的菜单草稿。"
        voice ("audio/voice/narr_shenlan_a4b6587608d2aaafbf1f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a4b6587608d2aaafbf1f.ogg")
        "他改到凌晨 3:47。手机上标着时间。"
        if p_branch == "luyao":
            voice ("audio/voice/narr_shenlan_9fd39c987fa92c0554ae.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9fd39c987fa92c0554ae.ogg")
            "前几天陆遥已经看过我写给小满的信。"
            voice ("audio/voice/narr_shenlan_e822259dbf0e1ab8d851.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e822259dbf0e1ab8d851.ogg")
            "他那天说，我至少应该告诉他。今天我要问他的也是这句。"
        if f_asked:
            voice ("audio/voice/narr_shenlan_d128489c6ea2e207fe4a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d128489c6ea2e207fe4a.ogg")
            "第一天我问他怎么找到这儿的，他说路过。后来我就没怎么问过。"
        if f_piano == "teach":
            voice ("audio/voice/narr_shenlan_41bd420c0b051b97ed33.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_41bd420c0b051b97ed33.ogg")
            "我想起让他放松手腕那天。他按错一个音，还抬头等我说话。"
        elif f_piano == "tease":
            voice ("audio/voice/narr_shenlan_61a88467b06b2c1297a1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_61a88467b06b2c1297a1.ogg")
            "那天在琴边我笑他敲代码。原来他后来真的在这儿敲了一整夜。"
        elif f_piano == "try":
            voice ("audio/voice/narr_shenlan_4982c67d96f9efb44b70.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4982c67d96f9efb44b70.ogg")
            "学琴那天，我往后让了让，让他自己找第一个音。那会儿倒没这么难开口。"
        voice ("audio/voice/narr_shenlan_d0885f8c08b7ca97bcf3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d0885f8c08b7ca97bcf3.ogg")
        "我发了条消息让他回来拿手机。他离店还没多久，一会儿就到了。"
        voice "audio/voice/argument_157.ogg"
        luyao "……你看见了。"
        voice ("audio/voice/narr_shenlan_31ff752edaf8c508a684.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_31ff752edaf8c508a684.ogg")
        "他站在门口，袖口往下滴着水。"
        if m11_looked:
            voice ("audio/voice/narr_shenlan_4d371e8117e5dd2b5f73.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4d371e8117e5dd2b5f73.ogg")
            "半夜我在电脑上瞥到过这张收据。那时候我还盼着自己看错了。"
        if m10_told:
            voice ("audio/voice/narr_shenlan_b39d248b94153dd4da97.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b39d248b94153dd4da97.ogg")
            "上次我说店可能要关，他第二天就没来。我以为这事过去了。"
        if m7_star:
            voice ("audio/voice/narr_shenlan_96fba1aed85d13819acd.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_96fba1aed85d13819acd.ogg")
            "他往里走的时候，我看见包上还挂着那颗「留下」。"
        if m4_ask:
            voice ("audio/voice/narr_shenlan_349c5539517cc2eb61e9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_349c5539517cc2eb61e9.ogg")
            "要是上回多问一句，说不定我早就知道他为什么非得四点走。"
        if m11_confront:
            voice ("audio/voice/narr_shenlan_c0ac2e76ad4d252ea5d4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c0ac2e76ad4d252ea5d4.ogg")
            "我上次半夜把他叫醒，也没问出什么。今天倒是连问哪一句都想好了。"
        if m10_signed:
            voice ("audio/voice/narr_shenlan_77441697ddafaba2971f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_77441697ddafaba2971f.ogg")
            "我自己签的那份合同还压在抽屉里。下个月该交的，和这张收据是两笔钱。"
        if m2_talk:
            voice ("audio/voice/narr_shenlan_3133d9516f380b23d10f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3133d9516f380b23d10f.ogg")
            "他跟我提过，公司不要他了。那回我们还聊了句咖啡。"
        if m3_ask:
            voice ("audio/voice/narr_shenlan_ea1b46177faea8849517.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ea1b46177faea8849517.ogg")
            "修机器的时候，他说他最近在休息。我那时候就该问问，怎么才算休息。"

    if pov == "luyao":
        call screen argue_table_luyao
    else:
        call screen argue_table
    $ r = _return

    if r == "lease":
        $ a_heat += 2
        $ a_choices.append(("摊开房租收据", "收据放到了桌子中间，两个人都低头看那一栏。"))
        voice "audio/voice/shenlan_b174878cbe08c868fdf2.ogg"
        shenlan "这笔钱你什么时候付的？"
        voice "audio/voice/luyao_14aaec7237c2c242bbb0.ogg"
        luyao "上个月，房东给我开的收据。"
        if pov == "luyao" and l_lease_told:
            voice "audio/voice/argument_188.ogg"
            shenlan "你把钱都垫进去了？"
        else:
            voice "audio/voice/argument_190.ogg"
            shenlan "用你的钱？"
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_9b08710772be6e6c4d86.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9b08710772be6e6c4d86.ogg")
            "我点了下头。"
        else:
            voice ("audio/voice/narr_shenlan_ad15cca730bb8a99c0f4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ad15cca730bb8a99c0f4.ogg")
            "他点了点头，手还按着纸的另一端。"
    elif r == "phone":
        $ a_heat += 1
        $ a_choices.append(("拿起手机" if pov == "luyao" else "拿起他的手机", "手机一亮，昨晚留在店里的事也瞒不住了。"))
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_15f987987fcaac85efa7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_15f987987fcaac85efa7.ogg")
            "我把手机往她那边转了转。"
            voice ("audio/voice/narr_shenlan_87adde4dbd0c217e7616.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_87adde4dbd0c217e7616.ogg")
            "草稿下面还连着店铺后台。我手指一碰，就翻出来一长串修改记录。"
        else:
            voice ("audio/voice/narr_shenlan_dcc868831e96c138955d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dcc868831e96c138955d.ogg")
            "我把他的手机拿起来，点开草稿下面的修改记录。"
            voice ("audio/voice/narr_shenlan_0a8759ecca070ca034ea.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0a8759ecca070ca034ea.ogg")
            "那么多条，往前滑了两下才滑到头。"
        voice "audio/voice/argument_204.ogg"
        shenlan "你几点睡的？"
        voice "audio/voice/argument_205.ogg"
        luyao "……记不清了。"
    elif r == "cup":
        $ a_heat -= 1
        $ a_choices.append(("给她倒水" if pov == "luyao" else "给他倒水", "接水的人没急着说话，先把杯子握在手里。"))
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_7d78ce313039ebe9a60e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7d78ce313039ebe9a60e.ogg")
            "我起身，给她倒了一杯水。"
            voice ("audio/voice/narr_shenlan_0816d3602bad15582c24.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0816d3602bad15582c24.ogg")
            "她接了杯子，没喝，手一直贴着杯壁。"
            voice "audio/voice/argument_212.ogg"
            shenlan "……谢谢。"
        else:
            voice ("audio/voice/narr_shenlan_411d55c1bd2c847418f0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_411d55c1bd2c847418f0.ogg")
            "我起身，给自己倒水，也给他倒了一杯。"
            voice ("audio/voice/narr_shenlan_fd871c7833c8c0521324.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fd871c7833c8c0521324.ogg")
            "他手上都是雨水，接杯子前先在裤腿上蹭了一下。"
            voice "audio/voice/argument_216.ogg"
            luyao "……谢谢。"
    else:
        $ a_choices.append(("先坐一会儿", "桌上的东西谁也没碰。后来是陆遥先开口。"))
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_53be79b0e61570755b50.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_53be79b0e61570755b50.ogg")
            "我在她对面坐下，什么也没拿。"
            voice ("audio/voice/narr_shenlan_918f888e95b7757e4c43.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_918f888e95b7757e4c43.ogg")
            "桌上那张收据的边角有点翘，我伸手压了一下。"
        else:
            voice ("audio/voice/narr_shenlan_c2a6d6943285dc2ed1de.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c2a6d6943285dc2ed1de.ogg")
            "我在他对面坐下，什么也没拿。"
            voice ("audio/voice/narr_shenlan_8bc3b3590882b97b3795.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8bc3b3590882b97b3795.ogg")
            "他盯着那张收据，拉了把椅子坐下来。"

    show screen argue_meter
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_d124770807b686ce9a14.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d124770807b686ce9a14.ogg")
        "我开口的时候，还在压那张纸。"
    else:
        voice ("audio/voice/narr_shenlan_606168a288546ff0a877.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_606168a288546ff0a877.ogg")
        "最后是他先开口的。"
    voice "audio/voice/luyao_9e1b10ad07af7c8feb34.ogg"
    luyao "欠的房租，我用补偿金垫了。那份工作，我也已经回绝了。"
    voice "audio/voice/luyao_a9e239c6ec71cf26f684.ogg"
    luyao "新合同那边，我只问过房东，首期那笔能不能缓几天。"
    voice "audio/voice/shenlan_0d0a280383fcacd7e7a5.ogg"
    shenlan "你以后拿什么交自己的房租？"
    voice "audio/voice/luyao_52dcabcfb9cea89d4d1c.ogg"
    luyao "便利店那边还能排班。"
    voice "audio/voice/argument_235.ogg"
    luyao "我只是不想让你走。"

    if pov == "luyao":
        menu:
            "保证我会留下":
                $ a_heat += 1
                $ a_choices.append(("说我会留下", "她问了一句怎么保证，你没答上来。"))
                voice "audio/voice/argument_242.ogg"
                luyao "我不会走。"
                voice "audio/voice/argument_243.ogg"
                shenlan "你拿什么保证？"
                voice "audio/voice/argument_244.ogg"
                luyao "……我不知道。"
                voice "audio/voice/argument_245.ogg"
                shenlan "所以你就替我决定了？"
            "跟她解释为什么推掉工作":
                $ a_heat += 2
                $ a_choices.append(("说起推掉的工作", "她问起你往后的打算，你还没想过那么远。"))
                voice "audio/voice/luyao_e692571cce5a44f6e239.ogg"
                luyao "我当时就想，工作以后还可以再找。"
                voice "audio/voice/shenlan_6ab40cad24dfa1d1b46f.ogg"
                shenlan "那你自己怎么办？"
                voice ("audio/voice/narr_shenlan_f455ca3050c1d5a07c2b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f455ca3050c1d5a07c2b.ogg")
                "我一时想不到能拿什么话让她放心。"
            "先听她说完":
                $ a_heat -= 1
                $ a_choices.append(("先听她说完", "她把每个月得交的钱都写了下来。"))
                voice ("audio/voice/narr_shenlan_9058232361c6e6f71565.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9058232361c6e6f71565.ogg")
                "我本来想接一句。看她摊开那本账，就等她先说完。"
                voice ("audio/voice/narr_shenlan_3fa5e6580f43dd802abf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3fa5e6580f43dd802abf.ogg")
                "她从下个月要交的租金说起，一笔一笔往下划。"
                voice ("audio/voice/narr_shenlan_9bbff0cc3951ca07fa7b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9bbff0cc3951ca07fa7b.ogg")
                "划到最后两栏，她用笔点了点，说光靠我一个人垫没用。"
                voice "audio/voice/argument_258.ogg"
                luyao "……我不是想让你欠我。"
    else:
        menu:
            "问他为什么不告诉我":
                $ a_heat += 1
                $ a_choices.append(("问他为什么瞒着", "他说，你知道了肯定不会让他垫。"))
                voice "audio/voice/argument_264.ogg"
                shenlan "你为什么不告诉我？"
                voice "audio/voice/argument_265.ogg"
                luyao "告诉你，你就不会要。"
                voice "audio/voice/argument_266.ogg"
                shenlan "所以你就替我决定了？"
            "问他为什么推掉那份工作":
                $ a_heat += 2
                $ a_choices.append(("问他为什么推掉工作", "他说以后还可以再找。你问他这段时间怎么办。"))
                voice "audio/voice/shenlan_16fcd7c503f7724be9b8.ogg"
                shenlan "那份工作，你为什么非得推掉？"
                voice "audio/voice/luyao_e692571cce5a44f6e239.ogg"
                luyao "我当时就想，工作以后还可以再找。"
                voice "audio/voice/shenlan_6ab40cad24dfa1d1b46f.ogg"
                shenlan "那你自己怎么办？"
                voice ("audio/voice/narr_shenlan_859089571ae37d2838a8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_859089571ae37d2838a8.ogg")
                "他张了下嘴，又低头看那张收据。"
            "让他把话说完":
                $ a_heat -= 1
                $ a_choices.append(("听他把话说完", "他给你看了排班，这还是头一回。"))
                voice ("audio/voice/narr_shenlan_8f454f54c68d5fc0a97e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8f454f54c68d5fc0a97e.ogg")
                "他去拿纸的时候，我帮他把杯子移开了一点。"
                voice ("audio/voice/narr_shenlan_cbd1a82730273ed74b6b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cbd1a82730273ed74b6b.ogg")
                "他在纸背上把钱一笔笔列出来，又给我看手机里的排班。"
                voice ("audio/voice/narr_shenlan_5363ad5d26e5bfe94946.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5363ad5d26e5bfe94946.ogg")
                "我才看清他得上几次夜班，才够填上那一行。"
                voice "audio/voice/argument_280.ogg"
                luyao "……我不是想让你欠我。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_30ea6a710a1476c5d3fc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_30ea6a710a1476c5d3fc.ogg")
        "我说我每天下午四点去便利店，夜里回来帮店里改网页。"
        voice ("audio/voice/narr_shenlan_d85b257236150492e684.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d85b257236150492e684.ogg")
        "本来还想说等店缓过来，一切就都好了。"
        voice ("audio/voice/narr_shenlan_057596e7bbdc55ddd394.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_057596e7bbdc55ddd394.ogg")
        "可想想刚才那一张张账单，我没再说下去。"
    else:
        voice ("audio/voice/narr_shenlan_e162168b9536f9e6eb58.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e162168b9536f9e6eb58.ogg")
        "他说四点以后他在便利店，半夜回来改店里的网页。"
        voice ("audio/voice/narr_shenlan_986db49f2b86b18c43b3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_986db49f2b86b18c43b3.ogg")
        "我以前见他困得趴在柜台上，还以为只是睡得晚。"
        voice ("audio/voice/narr_shenlan_c36e1745d7fea6b8a0c7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c36e1745d7fea6b8a0c7.ogg")
        "听他说完，我才想起来问他，这么晚回店里，到底是在哪儿睡。"
        voice ("audio/voice/narr_shenlan_de9f39fb23573f4fea02.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_de9f39fb23573f4fea02.ogg")
        "他低头往窗边那张椅子看了一眼。"

    if pov == "luyao":
        menu:
            "问她到底想不想留下":
                $ a_heat += 1
                $ a_choices.append(("问她的打算", "她还没答，你就忍不住又问了一句。"))
                voice "audio/voice/luyao_2464ce7e2cf0261a7505.ogg"
                luyao "你自己呢？你还想把店开下去吗？"
                voice "audio/voice/argument_299.ogg"
                shenlan "……"
                voice "audio/voice/luyao_692f80d8f8d73686259d.ogg"
                luyao "你倒是说句话。我这么做，到底有没有帮到你？"
            "坚持我会自己想办法凑钱":
                $ a_heat += 2
                $ a_choices.append(("说我会再凑钱", "你接着说房租，她问的是你自己。"))
                voice "audio/voice/luyao_efcb2149086b6660e591.ogg"
                luyao "剩下那笔钱，我再想办法。"
                voice "audio/voice/shenlan_42b1edc341d7b701607e.ogg"
                shenlan "我问的是你打算怎么办，没问你还能拿多少钱出来。"
                voice ("audio/voice/narr_shenlan_fa8d8c69acaa22cfc160.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fa8d8c69acaa22cfc160.ogg")
                "她说得急，手一松，杯子碰在桌面上响了一下。"
            "承认我也没想好怎么办":
                $ a_heat -= 1
                $ a_choices.append(("承认没想好", "她也说没想好。这回两个人都没急着接话。"))
                voice "audio/voice/argument_310.ogg"
                luyao "我不知道。"
                voice "audio/voice/argument_311.ogg"
                shenlan "……我也是。"
                voice ("audio/voice/narr_shenlan_7bdb99baa3b10b501d10.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7bdb99baa3b10b501d10.ogg")
                "她捧着杯子，慢慢坐了下来。"
    else:
        menu:
            "问他有没有想过我愿不愿意留下":
                $ a_heat += 1
                $ a_choices.append(("问他有没有想过我的打算", "他没说话，你等了一会儿。"))
                voice "audio/voice/argument_318.ogg"
                shenlan "你有没有想过，我想不想留？"
                voice "audio/voice/argument_319.ogg"
                luyao "……"
                voice "audio/voice/shenlan_d566cad907946d2f9417.ogg"
                shenlan "你跑去跟房东谈之前，怎么不先问问我？"
            "质问他凭什么替我决定":
                $ a_heat += 2
                $ a_choices.append(("问他凭什么替我决定", "他刚开口解释，你就打断了他。"))
                voice "audio/voice/shenlan_0dd09c3ddba149086c9c.ogg"
                shenlan "房东的电话你能打，我就在店里，你怎么一句都不跟我说？"
                voice "audio/voice/argument_325.ogg"
                luyao "我没有——"
                voice "audio/voice/argument_326.ogg"
                shenlan "你有。"
            "承认我也没想好":
                $ a_heat -= 1
                $ a_choices.append(("承认没想好", "他也说没想好。你这次听见他说完了。"))
                voice "audio/voice/argument_330.ogg"
                shenlan "我不知道。"
                voice ("audio/voice/narr_shenlan_906d0aaf19a4435484c6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_906d0aaf19a4435484c6.ogg")
                "我在心里想了好几遍才说出口。"
                voice "audio/voice/argument_332.ogg"
                luyao "……我也是。"

    if pov == "luyao" and a_heat <= 3:
        menu:
            "说清楚我为什么瞒着她":
                $ l_truth = True
                $ a_heat -= 1
                $ a_choices.append(a_truth_entry)
                voice "audio/voice/luyao_7de6b981294c0008aaa1.ogg"
                luyao "那份工作是我自己推的，可我没说我其实挺想去。"
                voice "audio/voice/luyao_24812d571c9c5c6d01f1.ogg"
                luyao "有两晚我在窗边那把椅子上睡。醒过来早了，就起来改店里的网页。"
                voice "audio/voice/luyao_db31723af45251cb0001.ogg"
                luyao "我不敢告诉你。你知道了，就更有理由不要我管。"
                voice "audio/voice/argument_342.ogg"
                shenlan "……你为什么不早说？"
                voice "audio/voice/luyao_20de8bde40f358956a61.ogg"
                luyao "我想等我把钱凑够了再说。后来才知道，怎么凑都不够。"
                voice ("audio/voice/narr_shenlan_d02cde23fb62fbb63bc3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d02cde23fb62fbb63bc3.ogg")
                "我说到这儿才敢看她一眼。"
            "只说「我只是想帮你」":
                $ a_choices.append(("只说「我只是想帮你」", "她合上了一半的账本，等你把后面的话说出来。"))
                voice "audio/voice/argument_346.ogg"
                luyao "我只是想帮你。"
                voice ("audio/voice/narr_shenlan_60f83b4e6537a2d0116e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_60f83b4e6537a2d0116e.ogg")
                "她把账本合上一半，手还压在封面上。"
                voice ("audio/voice/narr_shenlan_b47f6db202cd3bbf1d38.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b47f6db202cd3bbf1d38.ogg")
                "她在等我说下去。我端起水杯，发现里面是空的。"

    if not l_truth and (m9_told or m11_looked or p_branch == "xiaoman"):
        voice ("audio/voice/narr_shenlan_706cda3010e1921c424d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_706cda3010e1921c424d.ogg")
        "门被推开了一点，外面的风先灌进来。"
        voice ("audio/voice/narr_shenlan_4d83f39b3bf28fce0f5a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4d83f39b3bf28fce0f5a.ogg")
        "小满就站在门缝外面，手还扶着把手。"
        voice "audio/voice/argument_353.ogg"
        xiaoman "……我在外面都听见了。"
        if m9_support:
            if pov == "luyao":
                voice "audio/voice/xiaoman_fb70e0cd362b67902914.ogg"
                xiaoman "陆哥，你那天说我能当店长。现在还算吗？"
            else:
                voice "audio/voice/xiaoman_fc95857a3c207511ed0f.ogg"
                xiaoman "老板，我那天跟你说想当店长。你还记得吗？"
        voice "audio/voice/xiaoman_0c0bc5f6fd4e1270c70a.ogg"
        xiaoman "你们商量了半天，怎么一个都没叫我？"
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_6b38f9e4f1a4e1db76d2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6b38f9e4f1a4e1db76d2.ogg")
            "我往旁边拉了把椅子给她，她没坐。"
        else:
            voice ("audio/voice/narr_shenlan_96bd66d8c72ea2599011.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_96bd66d8c72ea2599011.ogg")
            "陆遥往旁边拉了把椅子。小满没过来。"
        if m9_told and a_heat <= 1:
            voice ("audio/voice/narr_shenlan_88c612eb48aa2dd9ea39.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_88c612eb48aa2dd9ea39.ogg")
            "小满把本子翻到记水电费的那页，指了指最底下那一栏。她已经算过一次了。"
            voice "audio/voice/xiaoman_4c82ab004c97f0cb072d.ogg"
            xiaoman "后间那几张桌子一直空着。明天我拿这个去问问，能不能只租前面。"
        else:
            voice ("audio/voice/narr_shenlan_2cda96599ca8d4266e90.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2cda96599ca8d4266e90.ogg")
            "她把记纸星的本子放在最近那张桌子上。"
            voice ("audio/voice/narr_shenlan_b11e82c537e21bd17b51.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b11e82c537e21bd17b51.ogg")
            "等我们抬头的时候，她已经走了，门还半开着。"
    else:
        voice ("audio/voice/narr_shenlan_d0e06b95638461bed3f4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d0e06b95638461bed3f4.ogg")
        "门外的脚步停了一下，又走远了。"

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
        voice ("audio/voice/narr_shenlan_7ffe71594afe1c36a0b8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7ffe71594afe1c36a0b8.ogg")
        "她挪到我旁边，抽了张纸递过来。我这才想起来擦擦袖口。"
        voice ("audio/voice/narr_shenlan_171ed3c4661d035a8821.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_171ed3c4661d035a8821.ogg")
        "我们把摊在柜台上的纸翻回第一页，从头对了一遍。"
    else:
        voice ("audio/voice/narr_shenlan_d7f7d9a7bda76da0d9d4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d7f7d9a7bda76da0d9d4.ogg")
        "他坐到我旁边，我找了几张纸给他擦袖口。"
        voice ("audio/voice/narr_shenlan_05d69c3a2f28e8d23f62.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_05d69c3a2f28e8d23f62.ogg")
        "他没急着再去拿手机。我们把柜台上那几张纸翻回第一页，从头对了一遍。"
    voice "audio/voice/argument_387.ogg"
    luyao "下次……我先问你。"
    voice "audio/voice/argument_388.ogg"
    shenlan "嗯。"
    voice ("audio/voice/narr_shenlan_deaa2bbaceea6d6b7b9b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_deaa2bbaceea6d6b7b9b.ogg")
    "她把压住收据的杯子拿开，纸上留下了一小圈水印。"
    $ a_review = "散场前，你们一起把账对了一遍。"
    jump argument_review_scene


label argument_stuck:
    show shenlan quiet_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_21467f91eda3107f6f18.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_21467f91eda3107f6f18.ogg")
    "说到最后，桌上的收据还摊在原处。"
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_38a02a78dea4def4119e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_38a02a78dea4def4119e.ogg")
        "我伸手把手机扣过去，推到离自己远一点的地方。"
    else:
        voice ("audio/voice/narr_shenlan_0e51132e651e6e7e7bac.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0e51132e651e6e7e7bac.ogg")
        "他把手机扣过去，推到桌子中间。"
    voice ("audio/voice/narr_shenlan_cf210453452fee8f6cf2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cf210453452fee8f6cf2.ogg")
    "过了一会儿，我们才各自起身收东西。"
    $ a_review = "账本摊了一晚上，最后一页的数字还没合上。"
    jump argument_review_scene


label argument_break:
    show shenlan angry_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    voice "audio/voice/argument_413.ogg"
    shenlan "你走吧。"
    voice "audio/voice/argument_414.ogg"
    luyao "……"
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_04d4939cb0a0dd056091.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_04d4939cb0a0dd056091.ogg")
        "我摸了摸兜里，把她借我用的那把钥匙放在桌上。"
        voice ("audio/voice/narr_shenlan_a5ebd9f48bf8362507bf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a5ebd9f48bf8362507bf.ogg")
        "临走的时候我还没想好该说什么。"
        voice ("audio/voice/narr_shenlan_74233346eb232337fd2b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_74233346eb232337fd2b.ogg")
        "后来门铃一响，我已经站在外头了。"
    else:
        voice ("audio/voice/narr_shenlan_5222ea86e5ab1280b34a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5222ea86e5ab1280b34a.ogg")
        "他把我借给他的那把钥匙放在桌上。"
        voice ("audio/voice/narr_shenlan_c64ed19981437a33e382.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c64ed19981437a33e382.ogg")
        "我看着他走到门口，也没叫他回来。"
        voice ("audio/voice/narr_shenlan_ba2a6c0a96ac355c423a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ba2a6c0a96ac355c423a.ogg")
        "门一开，外头的雨声一下大了。"
    $ a_broke = True
    $ a_review = "门铃响了一声，桌上还留着一把钥匙。"
    jump argument_review_scene


label argument_review_scene:
    $ unlock_record("argument")
    scene black with warmfade
    voice ("audio/voice/narr_shenlan_f57ad8d81ea527cc2a5f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f57ad8d81ea527cc2a5f.ogg")
    "后来回想起来，那晚有几句话我记得特别清楚。"
    call screen argue_review
    $ quick_menu = True
    if a_broke:
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_caea24dfae7657eb39dc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_caea24dfae7657eb39dc.ogg")
            "我的钥匙还在桌上。"
        else:
            voice ("audio/voice/narr_shenlan_1086c9a4e2178c31a506.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1086c9a4e2178c31a506.ogg")
            "钥匙还在桌上。"
    else:
        if pov == "luyao":
            voice ("audio/voice/narr_shenlan_984f39d98e901cb7ebb6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_984f39d98e901cb7ebb6.ogg")
            "她还没赶我走，我就留下来收了桌子。"
        else:
            voice ("audio/voice/narr_shenlan_f9e89c0fdf66fb8451ef.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f9e89c0fdf66fb8451ef.ogg")
            "陆遥还没走，站在桌边收那几只杯子。"
    if pov == "luyao" and l_truth:
        jump ending_told
    jump finale_scene


