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
        "她发消息让我回店里一趟。我以为又有东西坏了，出门时连伞都没拿。"
        voice ("audio/voice/narr_shenlan_7367123106115006670c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7367123106115006670c.ogg")
        "一进门，我就看见了房东开的收据。付款人一栏是我的名字。"
        "柜台上还有我忘拿的手机。我认得那份菜单草稿，手机是我刚才拿来对版用的。"
        "上面显示上次修改是 3:47。"
        if p_branch == "luyao_seen":
            "我前几天看过模型里那封信。到现在也没敢问她，日历上到底圈的是哪一天。"
        if f_asked:
            "第一天我还跟她说，自己是路过。"
        if f_piano == "teach":
            "学琴那天，她一遍遍叫我把手腕放松。我这会儿才发现我一直攥着包带。"
        elif f_piano == "tease":
            "她笑我弹琴像敲代码那天，我们也是打烊以后才开始说话。"
        elif f_piano == "try":
            "我想起学琴那天，她在旁边等我自己把音找出来。那回她肯等我。"
        "我把电脑包放下来，湿了的包带在柜台上印了道水痕。"
        voice "audio/voice/argument_124.ogg"
        luyao "……你看见了。"
        "我往屋里走了一步。她没过来接我的包。"
        if l_awake:
            "上次她半夜回来，我们好歹一起坐到了天亮。这回她一直站在柜台那一边。"
        elif l_lease_told:
            "我早跟她说过欠租的事。她现在才看到具体数目。"
        else:
            "我本来打算等房东那边有了准话再说。现在也用不着挑时间了。"
        if m7_star:
            "包上那颗「留下」蹭到了桌沿，我下意识把它扶了一下。"
        if l_four_told:
            "便利店的事她知道，只是不知道我把工钱攒下来做什么。"
        if m7_phone:
            "阿哲的电话我告诉过她。后来拒掉那份工作，我也只给阿哲回了一条消息。"
        if m2_talk:
            "我头一回和她提起被裁的时候，她问我以后还来不来喝咖啡。"
        if m3_ask:
            "修机器那天，我还跟她说，我最近在休息。"
    else:
        "打烊前房东送了收据来，说之前欠的那笔已经有人付过了。"
        "我盯着付款人那一栏找了半天，才敢认是陆遥的名字。"
        "他手机落在柜台上，屏幕还没灭。我看见上面开着店里的菜单草稿。"
        "他改到凌晨 3:47。手机上标着时间。"
        if p_branch == "luyao":
            "前几天陆遥已经看过我写给小满的信。"
            "他那天说，我至少应该告诉他。今天我要问他的也是这句。"
        if f_asked:
            "第一天我问他怎么找到这儿的，他说路过。后来我就没怎么问过。"
        if f_piano == "teach":
            "我想起让他放松手腕那天。他按错一个音，还抬头等我说话。"
        elif f_piano == "tease":
            "那天在琴边我笑他敲代码。原来他后来真的在这儿敲了一整夜。"
        elif f_piano == "try":
            "学琴那天，我往后让了让，让他自己找第一个音。那会儿倒没这么难开口。"
        "我发了条消息让他回来拿手机。他离店还没多久，一会儿就到了。"
        voice "audio/voice/argument_157.ogg"
        luyao "……你看见了。"
        "他站在门口，袖口往下滴着水。"
        if m11_looked:
            "半夜我在电脑上瞥到过这张收据。那时候我还盼着自己看错了。"
        if m10_told:
            "上次我说店可能要关，他第二天就没来。我以为这事过去了。"
        if m7_star:
            "他往里走的时候，我看见包上还挂着那颗「留下」。"
        if m4_ask:
            "要是上回多问一句，说不定我早就知道他为什么非得四点走。"
        if m11_confront:
            "我上次半夜把他叫醒，也没问出什么。今天倒是连问哪一句都想好了。"
        if m10_signed:
            "我自己签的那份合同还压在抽屉里。下个月该交的，和这张收据是两笔钱。"
        if m2_talk:
            "他跟我提过，公司不要他了。那回我们还聊了句咖啡。"
        if m3_ask:
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
            "我点了下头。"
        else:
            "他点了点头，手还按着纸的另一端。"
    elif r == "phone":
        $ a_heat += 1
        $ a_choices.append(("拿起手机" if pov == "luyao" else "拿起他的手机", "手机一亮，昨晚留在店里的事也瞒不住了。"))
        if pov == "luyao":
            "我把手机往她那边转了转。"
            "草稿下面还连着店铺后台。我手指一碰，就翻出来一长串修改记录。"
        else:
            "我把他的手机拿起来，点开草稿下面的修改记录。"
            "那么多条，往前滑了两下才滑到头。"
        voice "audio/voice/argument_204.ogg"
        shenlan "你几点睡的？"
        voice "audio/voice/argument_205.ogg"
        luyao "……记不清了。"
    elif r == "cup":
        $ a_heat -= 1
        $ a_choices.append(("给她倒水" if pov == "luyao" else "给他倒水", "接水的人没急着说话，先把杯子握在手里。"))
        if pov == "luyao":
            "我起身，给她倒了一杯水。"
            "她接了杯子，没喝，手一直贴着杯壁。"
            voice "audio/voice/argument_212.ogg"
            shenlan "……谢谢。"
        else:
            "我起身，给自己倒水，也给他倒了一杯。"
            "他手上都是雨水，接杯子前先在裤腿上蹭了一下。"
            voice "audio/voice/argument_216.ogg"
            luyao "……谢谢。"
    else:
        $ a_choices.append(("先坐一会儿", "桌上的东西谁也没碰。后来是陆遥先开口。"))
        if pov == "luyao":
            "我在她对面坐下，什么也没拿。"
            "桌上那张收据的边角有点翘，我伸手压了一下。"
        else:
            "我在他对面坐下，什么也没拿。"
            "他盯着那张收据，拉了把椅子坐下来。"

    show screen argue_meter
    if pov == "luyao":
        "我开口的时候，还在压那张纸。"
    else:
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
                "我一时想不到能拿什么话让她放心。"
            "先听她说完":
                $ a_heat -= 1
                $ a_choices.append(("先听她说完", "她把每个月得交的钱都写了下来。"))
                "我本来想接一句。看她摊开那本账，就等她先说完。"
                "她从下个月要交的租金说起，一笔一笔往下划。"
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
                "他张了下嘴，又低头看那张收据。"
            "让他把话说完":
                $ a_heat -= 1
                $ a_choices.append(("听他把话说完", "他给你看了排班，这还是头一回。"))
                "他去拿纸的时候，我帮他把杯子移开了一点。"
                "他在纸背上把钱一笔笔列出来，又给我看手机里的排班。"
                "我才看清他得上几次夜班，才够填上那一行。"
                voice "audio/voice/argument_280.ogg"
                luyao "……我不是想让你欠我。"

    if pov == "luyao":
        "我说我每天下午四点去便利店，夜里回来帮店里改网页。"
        "本来还想说等店缓过来，一切就都好了。"
        "可想想刚才那一张张账单，我没再说下去。"
    else:
        "他说四点以后他在便利店，半夜回来改店里的网页。"
        "我以前见他困得趴在柜台上，还以为只是睡得晚。"
        "听他说完，我才想起来问他，这么晚回店里，到底是在哪儿睡。"
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
                "她说得急，手一松，杯子碰在桌面上响了一下。"
            "承认我也没想好怎么办":
                $ a_heat -= 1
                $ a_choices.append(("承认没想好", "她也说没想好。这回两个人都没急着接话。"))
                voice "audio/voice/argument_310.ogg"
                luyao "我不知道。"
                voice "audio/voice/argument_311.ogg"
                shenlan "……我也是。"
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
                "我说到这儿才敢看她一眼。"
            "只说「我只是想帮你」":
                $ a_choices.append(("只说「我只是想帮你」", "她合上了一半的账本，等你把后面的话说出来。"))
                voice "audio/voice/argument_346.ogg"
                luyao "我只是想帮你。"
                "她把账本合上一半，手还压在封面上。"
                "她在等我说下去。我端起水杯，发现里面是空的。"

    if not l_truth and (m9_told or m11_looked or p_branch == "xiaoman"):
        "门被推开了一点，外面的风先灌进来。"
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
            "我往旁边拉了把椅子给她，她没坐。"
        else:
            "陆遥往旁边拉了把椅子。小满没过来。"
        if m9_told and a_heat <= 1:
            "小满把本子翻到记水电费的那页，指了指最底下那一栏。她已经算过一次了。"
            voice "audio/voice/xiaoman_4c82ab004c97f0cb072d.ogg"
            xiaoman "后间那几张桌子一直空着。明天我拿这个去问问，能不能只租前面。"
        else:
            "她把记纸星的本子放在最近那张桌子上。"
            "等我们抬头的时候，她已经走了，门还半开着。"
    else:
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
        "她挪到我旁边，抽了张纸递过来。我这才想起来擦擦袖口。"
        "我们把摊在柜台上的纸翻回第一页，从头对了一遍。"
    else:
        "他坐到我旁边，我找了几张纸给他擦袖口。"
        "他没急着再去拿手机。我们把柜台上那几张纸翻回第一页，从头对了一遍。"
    voice "audio/voice/argument_387.ogg"
    luyao "下次……我先问你。"
    voice "audio/voice/argument_388.ogg"
    shenlan "嗯。"
    "她把压住收据的杯子拿开，纸上留下了一小圈水印。"
    $ a_review = "散场前，你们一起把账对了一遍。"
    jump argument_review_scene


label argument_stuck:
    show shenlan quiet_half at expr_left with dissolve
    show luyao sad_half at expr_right with dissolve
    "说到最后，桌上的收据还摊在原处。"
    if pov == "luyao":
        "我伸手把手机扣过去，推到离自己远一点的地方。"
    else:
        "他把手机扣过去，推到桌子中间。"
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
        "我摸了摸兜里，把她借我用的那把钥匙放在桌上。"
        "临走的时候我还没想好该说什么。"
        "后来门铃一响，我已经站在外头了。"
    else:
        "他把我借给他的那把钥匙放在桌上。"
        "我看着他走到门口，也没叫他回来。"
        "门一开，外头的雨声一下大了。"
    $ a_broke = True
    $ a_review = "门铃响了一声，桌上还留着一把钥匙。"
    jump argument_review_scene


label argument_review_scene:
    $ unlock_record("argument")
    scene black with warmfade
    "后来回想起来，那晚有几句话我记得特别清楚。"
    call screen argue_review
    $ quick_menu = True
    if a_broke:
        if pov == "luyao":
            "我的钥匙还在桌上。"
        else:
            "钥匙还在桌上。"
    else:
        if pov == "luyao":
            "她还没赶我走，我就留下来收了桌子。"
        else:
            "陆遥还没走，站在桌边收那几只杯子。"
    if pov == "luyao" and l_truth:
        jump ending_told
    jump finale_scene


