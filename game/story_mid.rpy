# ============================================================
# 中段故事 · 相遇（记录 2–4）
# 记录 2：一杯咖啡，一颗星
# ============================================================

default m2_star = False
default m2_talk = False
default m3_fix = False
default m3_ask = False
default m4_feed = False
default m4_ask = False
default m6_write = False
default m6_ask = False
default m7_star = False
default m7_phone = False
default m8_invite = False
default m8_hand = False
default m10_signed = False
default m10_told = False
default m11_looked = False
default m11_confront = False
default m9_told = False
default m9_support = False

label story_days_early:
    jump scene_first_star


label scene_first_star:
    $ bgm("rain")
    scene black with warmfade
    call screen time_card("第二天", "记录 2 — 一杯咖啡，一颗星")

    scene bg shop day with paperdissolve
    show fx lamp day
    if pov == "luyao":
        show luyao sad_half at expr_right with dissolve
        "第二天我又去点了杯十八块的美式。便利店下午四点换班，在这儿等，比在出租屋里看时间容易一点。"
    else:
        "第二天，雨还没停。"
        "我刚把灯打开，昨天那个男生就来了，还是坐窗边。"
        show luyao sad_half at expr_right with dissolve
        "我给他拿水的时候，扫到他电脑上开着一封邮件。"
        show screen doc_overlay("prop layoff mail") with dissolve
        "标题是「调整」，发件人是人事部。"
        hide screen doc_overlay with dissolve
        "他把窗口关了。我也就没往下看。"
        "他还是点美式，说不用加糖。"
        show screen doc_overlay("prop menu board") with dissolve
        "那是菜单上最便宜的一杯，十八块。"
        hide screen doc_overlay with dissolve
        "我端咖啡的时候，手边正好有小满折的一罐纸星。"
        "平时点咖啡就能挑一颗，每颗上面都写着字。"
        "最上面那颗是我写的，上面就俩字，「撑住」。"

    if pov == "luyao":
        menu:
            "从罐子里挑一颗星":
                $ m2_star = True
                "她见我在看罐子，就拿起来让我挑。最上面一颗写着「撑住」，我伸手拿了那颗。"
            "只喝咖啡":
                "她把杯子放下来，我把电脑往里挪了挪。"
    else:
        menu:
            "送他一颗写着「撑住」的星":
                $ m2_star = True
                "我把那颗星放在他的碟子旁边。他本来在看电脑，低头时才发现。"
            "只端咖啡过去":
                "我把杯子放下，收走了托盘。"

    if m2_star:
        show cg coffee star with dissolve
        "碟子小，纸星搁在边上，差一点就滑下去。"
        hide cg coffee star with dissolve

    if pov == "shenlan":
        "他把视线从电脑上挪开了。"
        voice "audio/voice/story_mid_93.ogg"
        luyao "……谢谢。"
        if m2_star:
            "他小心地把星拈起来，放进了外套口袋。"

    if pov == "luyao":
        menu:
            "告诉她我被裁了":
                $ m2_talk = True
                voice "audio/voice/luyao_8f76001c5b3d719753e6.ogg"
                luyao "我昨天被裁了。"
                voice "audio/voice/shenlan_8c8621756a82c05cf0ac.ogg"
                shenlan "那以后还来喝咖啡吗？"
                "我原本准备回答一串关于工作的事，嘴里却只说出了「明天也来」。"
            "继续喝咖啡":
                "我端起杯子喝了一口，烫了舌头。"
    else:
        menu:
            "问他是不是遇到什么事了":
                $ m2_talk = True
                voice "audio/voice/story_mid_126.ogg"
                shenlan "……工作的事？"
                voice "audio/voice/story_mid_127.ogg"
                luyao "嗯。"
                voice "audio/voice/story_mid_128.ogg"
                luyao "从昨天开始，不用去了。"
                "他用勺子拨了拨杯柄，没抬头。"
                voice "audio/voice/shenlan_8c8621756a82c05cf0ac.ogg"
                shenlan "那以后还来喝咖啡吗？"
                voice "audio/voice/luyao_8a8f4a6eb33a816d425f.ogg"
                luyao "来吧。明天也有空。"
                "我把水杯往他那边推了推。"
            "不开口问":
                "还有一罐糖要添，我端着托盘回了柜台。"

    if pov == "luyao":
        if m2_star:
            "去换班前，我把「撑住」那颗放进了钱包，和便利店的工牌挨在一起。"
        else:
            "到四点，我在店门外戴上便利店的工牌。她背对着门，正在替下一桌磨豆子。"
    else:
        "那天他还是坐到了打烊。后来几乎每天都来，只是四点一到就收电脑。"
        if m2_star:
            "我往碟子边放的纸星，他每次都会拿走。"
        else:
            "有一回小满让他自己挑颗星。再后来，他想拿哪颗就自己伸手了。"

    $ unlock_record("first_star")
    if pov == "shenlan":
        scene black with warmfade
        "后来陆遥一进门，小满就去拿装美式的那个杯子。"
        "有时候他还没把电脑掏出来，她已经把咖啡端过去了。"
        if m2_star:
            "星星放哪儿还是我来挑，我有点想看看他会不会哪天忘了拿。"
        else:
            "小满后来干脆把罐子挪到靠外的一角，让他自己挑。"
    jump scene_card_reader


label scene_card_reader:
    scene black with warmfade
    call screen time_card("几天后", "记录 3 — 刷卡机")

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    if pov == "luyao":
        "那天柜台前排到了门口。我听见刷卡机响，已经下意识绕过去看接线口了。"
    else:
        "排在最前面的客人刷了三回，刷卡机光响，屏幕上那行字怎么也消不掉。"
        voice "audio/voice/story_mid_189.ogg"
        shenlan "……等一下，马上好。"
        voice "audio/voice/story_mid_190.ogg"
        xiaoman "老板，你按那个红色的——"
        voice "audio/voice/story_mid_191.ogg"
        shenlan "哪个红色？"
        "小满从旁边探过身来，连按了两下。排头的客人把卡收了回去。"
        show xiaoman pout_half at expr_right with dissolve
        voice "audio/voice/story_mid_194.ogg"
        xiaoman "……不是我。"
        "我还在桌下摸电源，窗边那位已经走到跟前了。"

    show luyao awkward_half at expr_left with dissolve
    voice "audio/voice/story_mid_201.ogg"
    luyao "我看看。"
    if pov == "luyao":
        "以前办公室里哪台机器不响了也会有人喊我。等我蹲下去，才发现自己这几天一直在等这句话。"
    else:
        "他蹲下来，把机器翻给我看。"
        "底下挤着两根线，我一时也分不清。"

    if pov == "luyao":
        menu:
            "让我来修":
                $ m3_fix = True
                "沈岚让开一个位置，我把网线重新插了一遍，再去找重启键。"
            "让她动手，我在旁边看":
                "她接过机器，手伸向外面那根线。我用指尖在另一头点了点。"
                voice "audio/voice/story_mid_221.ogg"
                luyao "这根。"
    else:
        menu:
            "让他修":
                $ m3_fix = True
                voice "audio/voice/story_mid_228.ogg"
                xiaoman "老板，你就让他修嘛。"
                "我往旁边让了让，他拔下网线，又插回去试了试。"
                "他低头在那儿找按键，耳朵悄悄红了。"
            "自己修":
                "我说不用，自己来。"
                "我把机器翻过来，伸手去拔外面那根线。"
                "他伸手在另一头点了点。"
                voice "audio/voice/story_mid_235.ogg"
                luyao "这根。"
                "我换了根线，这回拔对了。"

    if pov == "luyao":
        "小票打出来以后，她问我做什么的。我还是张口就答「程序员」。"
        "我把翘起来的创可贴按紧了些。包里那张面试通知还露着角，我想等真有消息再跟她讲。"
    else:
        "等机器重启，小票打出来了。队伍最前面那位客人先松了口气。"
        voice "audio/voice/story_mid_239.ogg"
        shenlan "……好了？"
        voice "audio/voice/story_mid_240.ogg"
        luyao "好了。"
        voice "audio/voice/story_mid_241.ogg"
        xiaoman "哇。"
        voice "audio/voice/story_mid_242.ogg"
        shenlan "你是做什么的？"
        voice "audio/voice/story_mid_243.ogg"
        luyao "程序员。"
        voice "audio/voice/story_mid_244.ogg"
        shenlan "程序员还修这个？"
        voice "audio/voice/story_mid_245.ogg"
        luyao "都是修东西。"
        "他答得挺快，说完倒不看我了。"
        "我没忍住，笑了一声。"
        show luyao warm_half at expr_left with dissolve
        "他抬头看见，又赶紧低下去找工具。"
        "他手背上贴了块创可贴，卷起来那一角都快掉了。"
        "往包里塞螺丝刀的时候，他带出来半张折好的纸。"

    if pov == "luyao":
        menu:
            "聊聊以前的工作":
                $ m3_ask = True
                voice "audio/voice/story_mid_267.ogg"
                shenlan "你以前……在哪家公司？"
                voice "audio/voice/story_mid_270.ogg"
                luyao "最近在休息。"
                "我说完就拉上了包。她看了一眼，去替我添水。"
            "接着收工具":
                "我把那张纸塞回去，拎着包回窗边坐下。"
    else:
        menu:
            "问问他以前在哪儿工作":
                $ m3_ask = True
                voice "audio/voice/story_mid_281.ogg"
                shenlan "你以前……在哪家公司？"
                voice "audio/voice/luyao_3d87ac9a4f06aa37e200.ogg"
                luyao "那家公司你可能没听过。"
                "他把工具收回去，没马上往下说。"
                voice "audio/voice/story_mid_284.ogg"
                luyao "最近在休息。"
                "他把拉链拉上。我就在心里划掉了后面那句「在哪儿上班」。"
                "我也没有再问。"
            "回去忙店里的事":
                "我没有问。"
                "他拎起工具包，回窗边坐下。"
                "那张纸还露着一角，碰到椅子背也没掉。"

    if pov == "luyao":
        "等客人走完，小满才想起来问我的名字。也是那时候，我知道老板叫沈岚。"
    else:
        "等客人都走了，小满给我们换了两杯水，顺便问了句怎么称呼。"
        "他说叫他陆遥就行。小满转过来，连我的名字也顺便报了。"
        "他临走又点了一杯美式，说要带走。"
        "我把杯盖按好，往杯子旁边放了颗星。"
        if m3_fix:
            "他顺手把星和螺丝刀一起塞进包里。"
        else:
            "他把星拿起来看了看，单独放进一个小兜里。"
    $ unlock_record("card_reader")

    if pov == "shenlan":
        scene black with warmfade
        "那台机器后来又坏了两回。"
        "头一回我重启了一遍，居然就好了。"
        "再坏我就等陆遥来，问他要不要干脆换根线。"
    jump scene_useless_things

label scene_useless_things:
    $ bgm("night")
    scene black with warmfade
    call screen time_card("又一个打烊的晚上", "记录 4 — 两个做没用东西的人")

    scene bg back room with paperdissolve
    show fx lamp back
    show luyao quiet_half at expr_right with dissolve
    if pov == "luyao":
        "打烊后，我帮沈岚压住捏泥人的报纸。创可贴粘在纸边上，差点揭下来。那是昨晚收货时，被便利店的纸箱蹭破的。"
        "我猜她捏的是小满。泥人围裙上有个歪扣子，跟小满那个松了线的挺像。"
    else:
        "打烊以后，我在后间铺了张报纸，接着捏那个没捏完的泥人。"
        "他就坐在我旁边，帮我把老是卷起来的报纸压着。"
        "架上是小满缝的兔子，有一只耳朵比另一只短。"
        "墙上也有她剪的纸星，胶带翘起来了，她总说下回一起补。"
        "她今天走得早，猫粮倒是提前装好了，袋口还夹着夹子。"
        voice "audio/voice/story_mid_340.ogg"
        luyao "你做的这些，有人买吗？"
        voice "audio/voice/story_mid_341.ogg"
        shenlan "没有。"
        voice "audio/voice/story_mid_342.ogg"
        luyao "那你为什么还做？"
        voice "audio/voice/story_mid_343.ogg"
        shenlan "……那你写的代码，有人用吗？"
        voice "audio/voice/story_mid_344.ogg"
        luyao "以前有。现在没了。"
        show luyao warm_half at expr_right with dissolve
        "我们俩都笑了。"
        "笑完再看，泥人的胳膊已经一长一短了。"
        "门口的纸箱动了一下。"
        "一只三花猫把脑袋探了出来。"
    show mem cat at cat_sit with dissolve
    if pov == "luyao":
        "年糕从纸箱里出来了。它先去蹭沈岚的脚，再探头闻我的手。"
        menu:
            "把手伸过去一起喂":
                $ m4_feed = True
                "她摊开手，我也凑过去接了几粒。"
                "年糕两边都闻了闻，这才开始吃，胡须蹭得我手痒。"
            "接过猫粮自己喂":
                "我接过猫粮蹲在纸箱边，等到腿麻，年糕才肯吃第一粒。"
    else:
        "它戴着个小牌子，上面是小满写的「年糕」。"
        voice "audio/voice/story_mid_354.ogg"
        luyao "……它叫年糕？"
        voice "audio/voice/story_mid_355.ogg"
        shenlan "小满取的。"
        voice "audio/voice/story_mid_356.ogg"
        luyao "挺合适的。"
        "它等我们看完，才一步一步蹭过来。"
        menu:
            "一起喂年糕":
                $ m4_feed = True
                "我倒出一点猫粮，又分了几粒给他。"
                "年糕在我们手心里挑来挑去，最后连碎的也舔干净了。"
            "把猫粮递给他":
                "我把猫粮递给他。"
                "他在纸箱旁蹲着，摊着只手，等得倒挺有耐心。"
                "年糕闻了半天，总算吃了一粒。"
                "我看他动了动嘴角，连声音都没出。"

    if pov == "luyao":
        "玻璃门上的告示又在响。她这几天一开门就要看它一眼，我伸手把它摘了。"
        voice "audio/voice/story_mid_391.ogg"
        shenlan "……你干嘛？"
        voice "audio/voice/story_mid_392.ogg"
        luyao "风大。"
        "我把告示折好塞进包里，转让两个字朝里。"
        $ sign_removed = True
    else:
        "年糕吃完，跳上窗台，团成一团。"
        show screen doc_overlay("prop transfer sign") with dissolve
        "玻璃门上那张转让告示有一角松了，开门时蹭到了门框。"
        hide screen doc_overlay with dissolve
        "他起来把门掩好。"
        "我以为他要把松掉的那角按回去，谁知他把整张纸都摘了。"
        voice "audio/voice/story_mid_400.ogg"
        shenlan "……你干嘛？"
        voice "audio/voice/story_mid_401.ogg"
        luyao "风大。"
        "他把纸折了两折，往电脑包里一塞。"
        $ sign_removed = True
        "我没让他贴回去。"
    scene black with warmfade
    call screen time_card("隔天下午")
    scene bg shop day with paperdissolve
    show luyao quiet_half at expr_right with dissolve
    if pov == "luyao":
        menu:
            "告诉她四点要去换班":
                $ l_four_told = True
                voice "audio/voice/story_mid_410.ogg"
                shenlan "你每天四点走……是有事吗？"
                voice "audio/voice/story_mid_411.ogg"
                luyao "四点便利店换班。晚班一小时多十二块。"
                voice "audio/voice/story_mid_413.ogg"
                shenlan "……你很缺钱？"
                voice "audio/voice/story_mid_414.ogg"
                luyao "嗯。"
                "我刚答完，便利店的店长就发来消息，问明晚还能不能顶班。"
            "只说有点事":
                voice "audio/voice/story_mid_417.ogg"
                shenlan "你每天四点走……是有事吗？"
                voice "audio/voice/story_mid_419.ogg"
                luyao "有点事。"
                "店长刚问我明晚能不能顶班。我还没回消息，先把手机揣了起来。"
    else:
        menu:
            "问他四点以后去哪儿":
                $ m4_ask = True
                voice "audio/voice/story_mid_427.ogg"
                shenlan "你每天四点走……是有事吗？"
                "他把包带往肩上提了提。"
                voice "audio/voice/story_mid_429.ogg"
                luyao "有点事。"
                "再问一句就真成查岗了。我只好说，明天见。"
            "不问他的事":
                "四点一到，他就拿上了包。"
                "他都碰到门把了，还回头朝我看了一眼。"
                "最后就说了声「明天见」。"

    if pov == "shenlan":
        "他走了以后，我从小满贴纸星剩下的纸里挑了一张，给泥人剪了条围巾。"
        "捏的到底是谁，我还没想好。"
        "年糕跳下来蹭我的脚，我这才想起来猫碗该添水了。"
    $ unlock_record("shop_cat")

    if pov == "shenlan":
        scene black with warmfade
        "后来门上剩下一小块胶印，我擦了几次，总有一点擦不干净。"
    jump piano_scene


label story_days_middle:
    jump scene_book_margin


label scene_book_margin:
    if pov == "luyao":
        jump luyao_pov_book
    $ bgm("night")
    scene black with warmfade
    call screen time_card("又过了一阵子", "记录 6 — 书页边")

    scene bg shop night with paperdissolve
    show fx lamp night
    show luyao quiet_half at expr_right with dissolve
    "他每天下午就在窗边那一小块地方坐着，一开电脑就是几个小时。"
    "有一天，我从柜台下面翻了本旧星图册出来。"
    voice "audio/voice/shenlan_a29b87ac82a056dbeca9.ogg"
    shenlan "你要不要歇会儿？我这儿有本书。"
    voice "audio/voice/story_mid_481.ogg"
    luyao "……这是给我的？"
    voice "audio/voice/story_mid_482.ogg"
    shenlan "借你的。看完还我。"
    "他接过去翻了几页，手指停在猎户座那张图上。"

    "第二天下午，他把书搁到柜台上，指给我看猎户座那一页。"
    "页边多了一行铅笔字：「你柜台上那三颗星，排得跟猎户座的腰带一样。」"
    "我抬头数了数。第四颗滚到罐子后面了，得伸手才够得着。"

    menu:
        "在页边回他一句":
            $ m6_write = True
            "我拿铅笔在底下添了一行：「你漏数一颗。在罐子后面。」"
            "铅笔印按得有点重。我拿橡皮在上面比画了一下，最后还是没擦。"
        "合上书，把它放回柜台":
            "我合上书，让它在柜台上待了一天。"

    "第二天他又来借，下午就还了。"
    "我翻到同一页，他果然又往下写了一行。"

    if m6_write:
        "「那第四颗算哪儿的？」"
        "我本来在擦桌子，看完转身就去把那颗掉队的星先往前摆了一点。"
    else:
        "「今天我数过了，真有四颗。」"
        "他大概是趁我不注意去看过了。"

    "书翻到一半，掉出一朵压干的满天星。"
    "我托着花梗，小心地把它放回了原处。"
    "就在那页的右下角，有几个字被铅笔划掉了。"
    menu:
        "问他划掉了什么":
            $ m6_ask = True
            "我转过书，让他看看右下角。"
            voice "audio/voice/story_mid_554.ogg"
            shenlan "这行划掉的是什么？"
            show luyao awkward_half at expr_right with dissolve
            voice "audio/voice/story_mid_556.ogg"
            luyao "……写错了。"
            "他拿手指去盖的时候，我已经看清了。写的是「留下来」。"
        "合上书，不问他":
            "我没问，合上书之前又看了一眼。"
            "那几道横线底下，还能看出是「留下来」。"

    "打烊后，我把书留在柜台上，底下压着几张还没付的账单。"



    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    "第二天小满看见书，问我能不能借她翻翻。"
    "还回来时，她在最后一页画了颗星，五个角画得长短不一。"
    voice "audio/voice/story_mid_589.ogg"
    xiaoman "老板，这书挺好看的。"
    "我把书塞回柜台底下，下回谁想看都能拿。"
    $ unlock_record("book_margin")

    scene black with warmfade
    "后来我把收据夹进了书里，反而比放在抽屉时好找。"
    jump scene_door_light


label scene_door_light:
    $ bgm("rain")
    scene black with warmfade
    call screen time_card("入秋以后", "记录 7 — 门口的灯")

    scene bg street rain with paperdissolve
    show fx rain slow
    show luyao quiet_half at expr_right with dissolve
    if pov == "luyao":
        "招牌的线松了。我踩上梯子把它接回去，一低头，看见沈岚两只手都扶在梯子上，等我下来。"
    else:
        "入了秋，下午刚过五点，街对面就看不清人脸了。"
        "对面几家店都亮了灯，我这边的招牌还黑着。"
        "他走到门外，仰头看招牌，半天没进来。"
        voice "audio/voice/story_mid_614.ogg"
        luyao "有梯子吗？"
        voice "audio/voice/story_mid_615.ogg"
        shenlan "……你要修？"
        voice "audio/voice/story_mid_616.ogg"
        luyao "试试。"
        "我把后间的梯子搬出来。"
        "他踩到最上头两级，把松了的线重新接上。"
        "我在下面扶梯子，看他外套肩头的颜色一点点变深。"
        "我们往后站了站。招牌终于亮了，门口的水洼也跟着亮起来。"
        voice "audio/voice/story_mid_626.ogg"
        shenlan "……好了。"
    show luyao warm_half at expr_right with dissolve
    if pov == "shenlan":
        voice "audio/voice/story_mid_628.ogg"
        luyao "好了。"

    if pov == "luyao":
        "她有颗纸星要给我，拇指正好盖住了字。"
    else:
        "我摸出预先放在围裙口袋里的一颗纸星。"
        "上面是我写的「留下」。"
        "那两个字不知道怎么开口，倒是早就写好了。"

    if pov == "luyao":
        menu:
            "伸手接过来":
                $ m7_star = True
                "我接过来，把星转了个面。她写的是「留下」。我顺手把那根细绳系在了电脑包上。"
            "先去收梯子":
                "我转身把梯子合上。再看她的时候，她手已经放回口袋了。"
    else:
        menu:
            "把星送给他":
                $ m7_star = True
                "我把星递过去。"
                voice "audio/voice/story_mid_656.ogg"
                shenlan "给你。"
                voice "audio/voice/story_mid_657.ogg"
                luyao "……这上面写的什么？"
                voice "audio/voice/story_mid_658.ogg"
                shenlan "你自己看。"
                "他把纸星转了个面，这才看见那两个字。"
                "我以为他又要塞进口袋，他却用上面那根绳系在了包上。"
            "把星放回口袋":
                "我握着星把手缩了回去。"
                "他正忙着收梯子，没看见。"

    if pov == "luyao":
        "电话是阿哲打来的。我过了马路才接。他说，那边连下个月的工位都给我留好了。"
        "我盯着对面刚亮起来的招牌，还是请他再给我几天。沈岚就扶着门，在等我回去。"
        if m7_star:
            "拉链上那颗星被我攥了一路，幸好还没淋透。"
    else:
        "他刚下来，手机就响了。"
        "他看了一眼来电，过了马路才接。"
        "他伞也没拿，我只好扶着门等他。"
        "回来时他甩了下头，水都甩到门把手上了。"

    if pov == "luyao":
        menu:
            "告诉她阿哲在等我答复":
                $ m7_phone = True
                voice "audio/voice/luyao_daf6491bd00744001aaf.ogg"
                luyao "是阿哲。有份工作，他在等我回话。"
                voice "audio/voice/shenlan_84040f9eae8f9fd936a1.ogg"
                shenlan "那你有空先回吧。我来收梯子。"
            "收好手机，不提这通电话":
                "我把手机调成静音，塞回兜里。"
    else:
        menu:
            "问他刚才是谁打来的":
                $ m7_phone = True
                voice "audio/voice/story_mid_703.ogg"
                shenlan "谁的电话？"
                voice "audio/voice/story_mid_704.ogg"
                luyao "……工作的事。"
                voice "audio/voice/story_mid_705.ogg"
                shenlan "这么晚？"
                voice "audio/voice/story_mid_706.ogg"
                luyao "嗯。"
                "我从柜台上够了几张纸巾，递给他擦头发。"
            "先回店里":
                "我往旁边让了让，等他进来再关门。"

    if pov == "luyao":
        "小满在窗边开了串灯。那晚回去，我又点开阿哲的消息，屏幕亮到自己熄了，我还是没回。"
    else:
        scene bg shop night with paperdissolve
        show fx lamp night
        show xiaoman neutral_bust at expr_right with dissolve
        "我一进门，发现小满正踩着凳子往窗边挂灯。"
        voice "audio/voice/story_mid_718.ogg"
        xiaoman "老板，你看。"
        "暖黄色的小灯从柜台一直挂到窗边。"
        voice "audio/voice/xiaoman_7acb0d79e7c4a7338f41.ogg"
        xiaoman "老板，晚上就开这串吧，外头也能看见。"
        "她还有一截线没挂好，说完又找了块胶带。"
        scene black with warmfade
        "天一黑我就开店招，有时候连小满那串灯也一起开。"
        if m7_star:
            "陆遥拉开电脑包，那颗星就会跟着晃一下。"
        else:
            "洗围裙之前，我摸出口袋里那颗没送出去的星，放回柜台抽屉。"
    $ unlock_record("door_light")
    jump scene_umbrella


label scene_umbrella:
    scene black with warmfade
    call screen time_card("那之后", "记录 8 — 雨里的伞")

    scene bg street rain with paperdissolve
    show fx rain slow
    show luyao warm_half at expr_right with dissolve
    if pov == "luyao":
        "我说顺路，要送她回去。其实我前两晚都在店里睡，连钥匙还在我兜里。"
        "走到第一个路口，我把伞往她那边偏了偏，袖子立刻就湿了。"
    else:
        "那天打烊的时候，雨大到站在檐下也会被溅到。"
        "我锁门的时候，陆遥已经撑着伞在台阶下等了。"
        voice "audio/voice/story_mid_752.ogg"
        shenlan "你还没走？"
        voice "audio/voice/story_mid_753.ogg"
        luyao "顺路。"
        "他说顺路，可他平常都是往另一头走的。"
        "我把钥匙收好，站到他的伞下面。"
        "走到路口等灯，我才发现他把伞几乎全偏到了我这边。"
        "他右边袖子都湿透了，还举着伞不动。"

    if pov == "luyao":
        menu:
            "伸手碰一碰她":
                $ m8_hand = True
                "我碰了碰她的手背。她把手指张开，等我握上去。"
            "把手留在口袋里":
                "她让我把伞往自己这边挪挪。我从兜里腾出手，扶住被风吹歪的伞柄。"
    else:
        menu:
            "握住他的手":
                $ m8_hand = True
                "我把手从兜里抽出来，轻轻碰了碰他的手背。"
                "他把伞换到另一只手，把空出来的手递给我。"
                "过了马路，他才想起来把伞往自己那头挪一点。"
            "把手留在口袋里":
                "我缩在伞下面，让他把伞往回挪一点。"
                "他低头看了看袖子，往回挪了一点点。"
                "到了下一个路口，伞又偏回来了。"

    if pov == "luyao":
        "到了她家楼下，我收了伞。店里还有半杯咖啡，也许喝完就有力气爬回出租屋了。"
    else:
        "走到那栋楼下面的时候，雨总算小了些。"
        "他把伞收在台阶下面。我走上两级，才发现他没跟上来。"
        "楼道灯隔着一盏亮一盏，非得走近了才知道哪盏是坏的。"

    if pov == "luyao":
        menu:
            "提议再坐一会儿":
                $ m8_invite = True
                "我问她能不能上去坐会儿。她看了眼楼道。"
                voice "audio/voice/story_mid_802.ogg"
                shenlan "……下次吧。"
                "她嘱咐我回去早点睡。我应得很快，忘了她还不知道我这几晚睡在哪儿。"
            "说晚安。":
                "我跟她说了晚安。等楼上亮了灯，我才转身，踩着刚才的脚印往店里走。"
        $ unlock_record("umbrella")
        jump story_days_late
    else:
        menu:
            "问他要不要上来坐坐":
                $ m8_invite = True
                voice "audio/voice/story_mid_816.ogg"
                shenlan "要不要上来坐一会儿？"
                "他抬头看了看楼上。"
                voice "audio/voice/story_mid_818.ogg"
                luyao "……下次吧。"
                "他又说，让我早点睡。"
                "我往他这边迈了一级台阶，最后还是只说了句「好」。"
            "说晚安。":
                "我说：「谢谢你送我。」"
                voice "audio/voice/story_mid_823.ogg"
                luyao "顺路。"
                "他这回答得比刚才还快。"
                "我也没忍住，笑着跟他说了声晚安。"
                "后来我开灯的时候，从窗户看见他才撑伞往回走。"

    scene black with dissolve
    if pov == "luyao":
        "后来有段时间，我每天下午都来，还是点最便宜的美式。"
        "她有时会多拿一颗星，放在我碟子边，一下午也不收走。"
        "打烊早的时候，她会叫我过去弹给她听。"
        "我前面都弹得好好的，偏偏到最后一下就按错。"
        "她也不拆穿，往边上挪挪，两个人再弹一遍。"
    else:
        "后来有段时间，下午一到，窗边总有人。"
        "他还是一来就点美式。"
        "有时我会多拿一颗星，也不给他，就在他那个碟子边放一下午。"
        "有几回打烊早，我就叫他过来弹给我听。"
        "他前面都弹得好好的，偏偏到最后一下就按错。"
        "我也不拆穿他，往边上挪挪，两个人再弹一遍。"
    scene cg piano lesson with dissolve
    scene bg back room with dissolve
    "那本星图册谁也不带回家了，翻完就塞回柜台下面。"
    if pov == "luyao":
        "快到四点时，年糕就跳上窗台。等我出了门才跳下来。"
    else:
        "快到四点时，年糕就跳上窗台。等他出了门才跳下来。"
    "小满在墙上又贴了一排星，踩着凳子才贴得到。"

    scene bg shop day with paperdissolve
    show xiaoman neutral_bust at expr_right with dissolve
    "隔天下午，小满擦着擦着杯子，突然凑了过来。"
    voice "audio/voice/story_mid_866.ogg"
    xiaoman "老板，昨晚谁送你回来的？"
    voice "audio/voice/shenlan_d0ac7bc45c8acc901894.ogg"
    shenlan "他正好顺路。"
    voice "audio/voice/story_mid_868.ogg"
    xiaoman "哦——"
    "她拖着调子应了一声，回头就去拿陆遥常用的那只杯子。"
    $ unlock_record("umbrella")

    scene black with warmfade
    "后来那把伞就放在门边，谁赶上下雨谁拿。"
    "黑柄上那圈胶带是后来缠的，它折过一回。"
    "拿的时候得避开那圈胶带，缠的人没把毛边按平。"
    jump story_days_late


label story_days_late:
    jump scene_notebook


label scene_lease:
    if pov == "luyao":
        jump luyao_pov_landlord
    scene black with warmfade
    call screen time_card("还有二十天", "记录 10 — 租约")

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman worried_half at expr_right with dissolve
    "房东挑了个没客人的时候来。"
    show landlord neutral_half at expr_left with dissolve
    "他站在柜台前，从牛皮纸袋里往外抽文件。"
    "小满倒了杯水给他，端着托盘退到后间。门还开着。"
    "他从里面抽出来一份续租合同，推到我面前。"
    show screen doc_overlay("prop lease doc") with dissolve
    "我先去看每月租金。"
    hide screen doc_overlay with dissolve
    voice "audio/voice/story_mid_904.ogg"
    landlord "楼要卖了。新房东要重新签，租金按市价。"
    voice "audio/voice/story_mid_905.ogg"
    shenlan "……多少？"
    "房东在我面前用手指点了点那个数字。"
    "我按着底下那行小字算了算，押两个月，还得先付三个月。"
    "就算只算头一笔，账上也凑不出来。"

    voice "audio/voice/story_mid_910.ogg"
    landlord "我也不想涨。可新房东按合同来，我也没办法。"
    voice "audio/voice/story_mid_911.ogg"
    shenlan "……期限呢？"
    voice "audio/voice/story_mid_912.ogg"
    landlord "下个月十五号之前。签了，就按新价；不签，十五号之后腾房。"
    "他把纸往我手边又推了一点。"
    voice "audio/voice/story_mid_914.ogg"
    landlord "小沈，你这店开了几年了？"
    voice "audio/voice/story_mid_915.ogg"
    shenlan "三年。"
    voice "audio/voice/story_mid_916.ogg"
    landlord "嗯。"
    "他把剩下的话咽了回去，低头喝了口水。"

    menu:
        "先签下续租合同":
            $ m10_signed = True
            "我把合同拉过来，把名字签在了最底下。"
            "签完我又看了眼金额，笔盖扣了两次才扣上。"
            "房东收起一份，把另一份留给了我。"
            voice "audio/voice/story_mid_925.ogg"
            landlord "十五号之前把第一笔打过来就行。"
            "我点头。"
        "先把合同留下，再想想":
            "我把笔放了回去，说还要再想想。"
            voice "audio/voice/story_mid_929.ogg"
            landlord "行。十五号之前给我个准话。"
            "他把文件袋往胳膊下一夹。"
            hide landlord with dissolve
            "合同还在柜台上，他走了我也没去收。"

    scene bg shop night with paperdissolve
    show fx lamp night
    show xiaoman worried_half at expr_right with dissolve
    "打烊以后，我把续租合同和几张没付的账单叠起来往抽屉里塞。"
    "纸太多了。关抽屉时，还有一角露在外头。"
    "小满就站在后间门口，好像有话要说。"
    voice "audio/voice/story_mid_940.ogg"
    xiaoman "老板。"
    voice "audio/voice/story_mid_941.ogg"
    shenlan "嗯？"
    voice "audio/voice/story_mid_942.ogg"
    xiaoman "……没事。"
    "她给我换了杯温水，这才去擦桌子。"

    menu:
        "告诉陆遥店可能要关":
            $ m10_told = True
            "我点开陆遥的头像，发了一句「店可能要关了」。"
            "他几乎是立刻回过来：「我马上过来。」"
            "那天晚上他果然又来了，到了店里也没往窗边坐。"
            voice "audio/voice/story_mid_952.ogg"
            luyao "差多少？"
            voice "audio/voice/story_mid_953.ogg"
            shenlan "……不用你管。"
            voice "audio/voice/story_mid_954.ogg"
            luyao "我问差多少。"
            "我把手搭在抽屉的拉手上，没拉开。"
            "他站了一会儿，见我不说话就走了。"
            "第二天，他没有来。"
        "先不告诉他":
            "我把手机放回柜台，没发那条消息。"
            "第二天下午，他还是照常来点了杯美式。"
            "电脑刚开，他又把它合上了。"
            voice "audio/voice/story_mid_962.ogg"
            luyao "房东最近来过吗？"
            voice "audio/voice/story_mid_963.ogg"
            shenlan "……怎么突然问这个？"
            voice "audio/voice/story_mid_964.ogg"
            luyao "随便问问。"
            "他去端那杯咖啡，搅拌棒外面的纸还没拆。"

    $ unlock_record("lease")
    scene black with warmfade
    "那张合同后来一直在抽屉里搁着。"
    "每次够别的东西，我都得先把它往旁边拨一拨。"
    jump scene_three_am


label scene_three_am:
    if pov == "luyao":
        jump luyao_pov_347
    scene black with warmfade
    call screen time_card("那天夜里", "记录 11 — 凌晨 3:47")

    scene cg 347 with paperdissolve
    "那天关门之后，我才想起来有东西落在店里。"
    "再回来已经过了三点。"
    if m10_told:
        "他白天没来，倒是夜里来了。"
    "我拿钥匙去开门，手刚碰到门把，门就开了。"
    "他趴在柜台边，枕着自己的胳膊。"
    "电脑屏幕没关，上面还开着店里的网页。"
    "我站到他身后，看见右下角写着 3:47。"

    menu:
        "看一眼屏幕上有什么":
            $ m11_looked = True
            "我扶着屏幕，把它往自己这边转了一点。"
            show screen doc_overlay("prop screen 347") with dissolve
            "原来他一直在修店里的支付后台。"
            "最后一条修改是 3:46，就在我过来前一分钟。"
            "旁边还开着几个文件，最上面一份是房东开的收据。"
            "付款人写的是陆遥。"
            hide screen doc_overlay with dissolve
            "我站了一会儿，把屏幕轻轻转了回去。"
        "把外套给他盖上":
            "我脱了外套，从背后搭在他肩上。"
            "他动了动胳膊，往里埋了埋脸。"

    "他睡着的时候眉头还是皱着的。"
    "手边那杯美式早凉了，还剩一半。"

    menu:
        "叫他起来":
            $ m11_confront = True
            "我隔着柜台碰了碰他的肩膀。"
            "他一醒，下意识就伸手去合电脑。"
            voice "audio/voice/story_mid_1017.ogg"
            luyao "……你怎么在这？"
            voice "audio/voice/story_mid_1018.ogg"
            shenlan "这是我想问的。"
            "他看着已经合起来的电脑，有一会儿没说话。"
            "我以为他要解释，等了好一会儿也没有。"
            "我给他倒了杯温水，在柜台另一头坐下。"
        "让他再睡一会儿":
            "我拉了张椅子过来，在旁边坐到快天亮。"
            "他醒来时，伸手先去够鼠标。"

    scene bg shop day with paperdissolve
    scene bg shop day with paperdissolve
    show fx lamp day
    "天亮了，他揉了揉眼睛，说还是想喝美式。"
    if not m11_looked:
        voice "audio/voice/story_mid_1031.ogg"
        luyao "昨晚……谢谢你。"
        voice "audio/voice/story_mid_1032.ogg"
        shenlan "谢什么？"
        voice "audio/voice/story_mid_1033.ogg"
        luyao "……外套。"
    "他端起杯子，喝得比平时快了些。"
    "那台电脑后来被他收回包里，我没去问。"
    if m11_confront:
        "从早上到走，他都没再把电脑拿出来。"
        "临走到了门口，他回头站了一会儿。"
        "最后还是只说了句「明天见」。"
    else:
        "下午四点，他收好电脑就走了。"

    $ unlock_record("truth_347")
    scene black with warmfade
    "我后来核对店里的账，偶尔会点开后台。"
    "看到那条 3:46 的修改记录，我就知道是谁改的。"
    jump puzzle_scene


label scene_notebook:
    if pov == "luyao":
        jump luyao_pov_notebook
    $ bgm("night")
    scene black with warmfade
    call screen time_card("还有二十五天", "记录 9 — 小满的本子")

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    "那天下午不怎么忙，小满把本子摊在柜台上。"
    "她写两笔就要停一下，伸手拨一拨罐子里的星。"
    voice "audio/voice/story_mid_1064.ogg"
    shenlan "在写什么？"
    voice "audio/voice/story_mid_1065.ogg"
    xiaoman "秘密。"
    "她啪地合上了本子，过了会儿又把它推到我面前。"
    "最上面写着「今天送出去 17 颗星」。"
    "她在底下又添了句：「第四个客人想多要一颗。给了。」"
    "翻过去，前面小半本都是这么记的。"
    show screen doc_overlay("prop notebook page") with dissolve
    hide screen doc_overlay with dissolve

    "手机振了两下，小满低头去看是谁。"
    voice "audio/voice/story_mid_1076.ogg"
    xiaoman "……我妈。"
    "她把本子往我手里一塞，去了后间。"
    "门没带上，我还能听见她说话。"

    voice "audio/voice/story_mid_1080.ogg"
    xiaoman "……嗯，在上班。"
    voice "audio/voice/story_mid_1081.ogg"
    xiaoman "不是玩，是工作。"
    voice "audio/voice/story_mid_1082.ogg"
    xiaoman "……我知道。"
    voice "audio/voice/story_mid_1083.ogg"
    xiaoman "妈，我会想的。"
    "挂了电话以后，后间又安静了好一会儿。"

    show xiaoman worried_half at expr_right with dissolve
    "她走出来的时候，眼睛有点红。"
    voice "audio/voice/story_mid_1088.ogg"
    xiaoman "我妈说，让我回老家考编。"
    voice "audio/voice/story_mid_1089.ogg"
    shenlan "……你怎么说？"
    voice "audio/voice/story_mid_1090.ogg"
    xiaoman "我说我再干一年。"
    "她把本子接过去，翻到没写过的那一页。"
    voice "audio/voice/story_mid_1092.ogg"
    xiaoman "老板，我是不是很没出息？"

    menu:
        "告诉她，她一直干得很好":
            $ m9_support = True
            voice "audio/voice/story_mid_1097.ogg"
            shenlan "不会。你比我认真。"
            "她抬头看了我一眼。"
            voice "audio/voice/story_mid_1099.ogg"
            xiaoman "……真的？"
            voice "audio/voice/story_mid_1100.ogg"
            shenlan "本子都记了小半本了。"
            "她笑了一下，抬手的工夫用袖口擦了擦眼睛。"
        "劝她也考虑一下回老家":
            voice "audio/voice/story_mid_1103.ogg"
            shenlan "你妈说得也有道理。"
            "她垂下眼，把刚翻开的本子合上了。"
            voice "audio/voice/story_mid_1105.ogg"
            xiaoman "……嗯。"

    voice "audio/voice/story_mid_1108.ogg"
    xiaoman "老板。"
    voice "audio/voice/story_mid_1109.ogg"
    shenlan "嗯？"
    voice "audio/voice/story_mid_1110.ogg"
    xiaoman "如果有一天你不想开了，我可以当店长。"
    "她把本子捏得有点紧，纸角都弯了。"
    "我手里还拿着杯子。那句「好啊」到嘴边了，又没说出来。"

    menu:
        "告诉她续租可能有问题":
            $ m9_told = True
            voice "audio/voice/story_mid_1117.ogg"
            shenlan "……店可能要关了。"
            "她把本子放了下来。"
            voice "audio/voice/story_mid_1119.ogg"
            xiaoman "什么时候的事？"
            voice "audio/voice/story_mid_1120.ogg"
            shenlan "下个月十五号之前。"
            if m9_support:
                voice "audio/voice/xiaoman_063a03081e163a76be3d.ogg"
                xiaoman "你刚才还说我比你认真。我还以为……"
            else:
                "她按着本子，慢慢坐了下去。我想起刚才劝她回老家那句话，这回才听出有多重。"
            "我拿起壶，才发现刚才那只杯子已经满了。"
            voice "audio/voice/xiaoman_7a12ba3b03aa1353982a.ogg"
            xiaoman "那我还能看看店里的账吗？我想知道还差多少。"
            "我给她腾了点地方，把账本从柜台下面拿出来。她翻开自己的本子，一项一项地对。"
        "先不告诉她":
            "我想了想，还是跟她说了声「好啊」。"
            "她把本子抱起来，腾出手去收桌上的杯子。"

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    show luyao quiet_half at expr_left with dissolve
    "陆遥傍晚才来。"
    "小满给他送咖啡，放下杯子才问：「陆哥，听说你找到工作了？」"
    voice "audio/voice/story_mid_1136.ogg"
    luyao "……嗯。找到了。"
    "他没抬头，拇指贴着杯把蹭来蹭去。"
    voice "audio/voice/story_mid_1138.ogg"
    xiaoman "那挺好的。"
    "她收起托盘，回去擦柜台了。"
    "陆遥等她走远，才压着声音叫了我一声。"
    voice "audio/voice/story_mid_1141.ogg"
    luyao "房东最近来过吗？"
    "我转头去看他。"
    voice "audio/voice/story_mid_1143.ogg"
    luyao "……随便问问。"

    $ unlock_record("notebook")
    scene black with warmfade
    "那天打烊，我发现小满把本子落在柜台上了。"
    "封面上那颗星的最后一笔画歪了，她用蓝笔给它补了个角。"
    jump scene_lease


label luyao_pov_book:
    $ bgm("night")
    scene black with warmfade
    call screen time_card("又过了一阵子", "记录 6 — 书页边")

    scene bg shop night with paperdissolve
    show fx lamp night
    show luyao quiet_half at expr_right with dissolve
    "她看我一直盯着电脑，就从柜台底下拿了本旧星图册给我。"
    "猎户座的图我一眼就认出来了。刚好柜台上也有三颗纸星排在一起，我就在旁边写了句："
    "「你柜台上那三颗星，排得跟猎户座的腰带一样。」"
    "第二天，我把书还她，指给她看的是那一页。"

    menu:
        "再借来看看她写了什么":
            $ m6_write = True
            "隔天我又把书借过来。她在底下添了一行：「你漏数一颗。在罐子后面。」"
            "我把罐子往前挪了一点，后头还真有一颗。"
        "不提页边的字，照常借书":
            "隔天我去借书，谁都没提那行字。"
            "不过我一进门就又数了一遍，这回数出了四颗。"

    "下午我把书还给她，照例指了指那一页。"
    if m6_write:
        "这回我写的是：「那第四颗算哪儿的？」"
        "她忙着擦桌子，看完倒先去挪柜台上的星。"
    else:
        "她没回我，我又添了一句。"
        "「今天我数过了，真有四颗。」"

    "我之前翻得急，掉出来一朵干花。仔细一看，是满天星。"
    "怕把花瓣碰碎，我把它夹回了书里。"
    "那一页的右下角，我还写过三个字。"
    "「留下来」。写完没几秒，我就拿铅笔划掉了。"

    menu:
        "让她看看夹花的那页":
            $ m6_ask = True
            "我把书翻开，给她看那朵花，她的目光却落到了右下角。"
            voice "audio/voice/story_mid_1191.ogg"
            shenlan "这行划掉的是什么？"
            show luyao awkward_half at expr_right with dissolve
            voice "audio/voice/story_mid_1193.ogg"
            luyao "……写错了。"
            "我伸手去盖，动作还是慢了一点。"
            "她没追问，我也没把手挪开。"
        "先把那页合上":
            "我把星图册合上，照原样放回柜台。"
            "那几道线划得太轻。不知道她翻到那儿会不会看清。"

    "打烊后，她把书往旁边挪了挪，底下露出几张催缴的账单。"
    "她低头去理那些纸，我就去收杯子。"

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    "第二天小满借了书，还回来时，最后一页多了颗角有长有短的星。"
    voice "audio/voice/story_mid_1208.ogg"
    xiaoman "老板，这书挺好看的。"
    "沈岚把书放回柜台底下。"
    $ unlock_record("book_margin")

    scene black with warmfade
    "后来我再借书，翻两页就会掉出一张她夹进去的收据。"
    jump scene_door_light


# ============================================================
# 二周目 · 陆遥视角 · 记录 9–11
# 这三场他不在沈岚的现场，用单独的标签，不复制一周目分支
# ============================================================

label luyao_pov_notebook:
    $ bgm("night")
    scene black with warmfade
    call screen time_card("还有二十五天", "记录 9 — 小满的本子")

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    show luyao quiet_half at expr_left with dissolve
    "傍晚我进来的时候，小满正趴在柜台上写东西。"
    "她一见是我，先把本子扣上，又朝我招手，让我过去看看。"
    "最上面写着「今天送出去 17 颗星」。"
    "底下她又添了一句：「第四个客人想多要一颗。给了。」"
    "她翻给我看的时候，我才发现都快记了半本。"
    show screen doc_overlay("prop notebook page") with dissolve
    hide screen doc_overlay with dissolve

    "后间门没关严，我听见她妈妈说：「你不能一辈子在咖啡店。」"
    "小满只说了句「妈，我会想的」。"
    "挂了电话她也没出来。过了一会儿，里头才有动静。"

    show xiaoman worried_half at expr_right with dissolve
    "她出来的时候，眼睛有点红。"
    "她先把沈岚手边那杯凉水换了，才给我送咖啡。"
    voice "audio/voice/story_mid_1249.ogg"
    xiaoman "陆哥，如果有一天老板不想开了，我可以当店长。"
    "她说得很快，手却还揪着本子的一角。"

    menu:
        "说「你可以」。":
            $ m9_support = True
            "我说：「我觉得你行。」她想了想，才笑出来。"
        "告诉她店可能要关。":
            $ m9_told = True
            "我说：「我看见一张续租单，店可能开不下去。」她半天没接话。"
            voice "audio/voice/xiaoman_e219c7ed9456431abf2f.ogg"
            xiaoman "那我去问问老板，能不能给我也看看账。水电费我手上有。"
            "她抱着本子去了柜台后面。沈岚听完，让了半张桌子给她。"
        "说「别把自己搭进去」。":
            "她听我说完，把本子合上了：「我就是问问。」"

    voice "audio/voice/story_mid_1263.ogg"
    xiaoman "陆哥，听说你找到工作了？"
    voice "audio/voice/story_mid_1264.ogg"
    luyao "……嗯。找到了。"
    "我答得太快了，自己都愣了一下。"
    "录用通知还在包里，我一直没回人家。"
    show screen doc_overlay("prop offer letter") with dissolve
    "上面的工资够我再付几个月房租。入职日期也快到了。"
    hide screen doc_overlay with dissolve
    voice "audio/voice/story_mid_1271.ogg"
    xiaoman "那挺好的。"
    "她端着空托盘回了柜台。"
    "沈岚朝我看过来，我假装忙着喝咖啡。"
    voice "audio/voice/story_mid_1275.ogg"
    luyao "房东最近来过吗？"
    voice "audio/voice/story_mid_1276.ogg"
    shenlan "……怎么突然问这个？"
    voice "audio/voice/story_mid_1277.ogg"
    luyao "随便问问。"
    "我大概知道自己还能拿出多少，可差多少，总得先问到数。"

    $ unlock_record("notebook")
    scene black with warmfade
    "那天走之前，我看见小满把本子落在柜台上了。"
    "封面那颗星画歪了一角，她还用蓝笔描了一遍。"
    jump scene_lease


label luyao_pov_landlord:
    scene black with warmfade
    call screen time_card("还有二十天", "记录 10 — 租约")

    "房东在隔壁街办公，我绕过一排招牌才找到门。"
    "我把裁员拿到的补偿转给他，先垫上店里欠的租金。"
    "显示转账成功后，我看了眼余额，只剩我自己的房租和一点生活费。"
    "他收了钱，抬头问：「你跟小沈是什么关系？」"
    "我说：「我在她那儿喝咖啡。」"
    "他看了我一眼，拿了张收据给我。"
    voice "audio/voice/story_mid_1298.ogg"
    landlord "十五号之前把第一笔打过来就行。"
    "我把收据折起来。新租约的首期还没着落，我只说我会想办法。"
    "出了办公室，雨已经下起来了。"

    menu:
        "发消息告诉她":
            $ l_lease_told = True
            "我站在屋檐下给她发消息：「店里之前欠的那笔房租，我先垫了。」"
            "隔了很久，她才回：「你哪来的钱？」"
            "我打了几个字又删掉，没回那句。"
        "先把收据收起来":
            "我打开她的聊天框，打了几个字。"
            "临走又一个个删掉了。"
            "收据跟纸星一起放进钱包，那里平常不会有人翻。"

    scene bg street rain with paperdissolve
    show fx rain slow
    "回去时我绕到店对面，往里看了一眼。"
    "店招亮着，小满挂在窗边的那串灯也亮着。"
    "包里还放着那张我摘下来的转让告示。我摸了摸拉链，没进去。"
    $ unlock_record("lease")
    scene black with warmfade
    jump scene_three_am


label luyao_pov_347:
    scene black with warmfade
    call screen time_card("那天夜里", "记录 11 — 凌晨 3:47")

    scene bg shop night with paperdissolve
    show fx lamp night
    "门响的时候，我刚把支付页面的修改提交上去。"
    "沈岚上次说过，她有东西会顺手塞在柜台底下。我猜这回也是回来找东西的。"
    "我趴在柜台上没动，电脑屏幕还亮着。"
    "右下角跳到了 3:47。刚才那条修改是 3:46。"
    "脚步声到我旁边就停了。"
    "她拿了件外套，轻轻搭在我肩上。"
    "我听见她吸了一下鼻子，紧跟着又吸了一下。"
    "我本来想告诉她，我还醒着。"
    "一睁眼，我就得解释为什么凌晨还留在店里。"
    if l_lease_told:
        "房租的消息她已经看过了，关于我在店里过夜这件事，我还没提。"
    else:
        "到这会儿，她连我垫了租金都还不知道。"

    menu:
        "睁开眼":
            $ l_awake = True
            "我动了动胳膊，抬起头。"
            voice "audio/voice/story_mid_1350.ogg"
            luyao "……我没睡。"
            "她还抓着外套没松手。"
            voice "audio/voice/story_mid_1352.ogg"
            shenlan "你什么时候醒的？"
            voice "audio/voice/story_mid_1353.ogg"
            luyao "你进门的时候。"
            "电脑亮光照得她眯了下眼。我这才看见她眼睛是红的。"
            voice "audio/voice/story_mid_1355.ogg"
            luyao "别哭。"
            "她拉开旁边那把椅子，慢慢坐了下来。"
            "我把电脑合上。我们就这么坐到天亮。"
        "继续装睡":
            "我闭着眼，等她先走。"
            "她又站了一会儿，才拿了东西出去。"
            "听见门扣上，我才抬头。"
            "屏幕上还是 3:47。"

    scene bg shop day with paperdissolve
    show fx lamp day
    "天亮以后，她照旧给我倒了一杯美式，还问我杯子用不用先温一下。"
    voice "audio/voice/story_mid_1368.ogg"
    luyao "昨晚……谢谢你。"
    voice "audio/voice/story_mid_1369.ogg"
    shenlan "谢什么？"
    voice "audio/voice/story_mid_1370.ogg"
    luyao "……外套。"
    "她低头继续擦杯子，擦完才把外套从我椅背上拿回去。"
    $ unlock_record("truth_347")
    scene black with warmfade
    jump puzzle_scene
