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
        voice ("audio/voice/narr_shenlan_e41d368c7b3a40fce6ad.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e41d368c7b3a40fce6ad.ogg")
        "第二天我又去点了杯十八块的美式。便利店下午四点换班，在这儿等，比在出租屋里看时间容易一点。"
    else:
        voice ("audio/voice/narr_shenlan_435a077d79b2857dc14b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_435a077d79b2857dc14b.ogg")
        "第二天，雨还没停。"
        voice ("audio/voice/narr_shenlan_b539d221e177728250ca.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b539d221e177728250ca.ogg")
        "我刚把灯打开，昨天那个男生就来了，还是坐窗边。"
        show luyao sad_half at expr_right with dissolve
        voice ("audio/voice/narr_shenlan_baf7be7a061a54256a8d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_baf7be7a061a54256a8d.ogg")
        "我给他拿水的时候，扫到他电脑上开着一封邮件。"
        show screen doc_overlay("prop layoff mail") with dissolve
        voice ("audio/voice/narr_shenlan_c87d9dbe4d035dd6ec7f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c87d9dbe4d035dd6ec7f.ogg")
        "标题是「调整」，发件人是人事部。"
        hide screen doc_overlay with dissolve
        voice ("audio/voice/narr_shenlan_6ea65c99a56daa5bd337.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6ea65c99a56daa5bd337.ogg")
        "他把窗口关了。我也就没往下看。"
        voice ("audio/voice/narr_shenlan_50acd81ff0e8ff117ccf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_50acd81ff0e8ff117ccf.ogg")
        "他还是点美式，说不用加糖。"
        show screen doc_overlay("prop menu board") with dissolve
        voice ("audio/voice/narr_shenlan_de505c29c25463d0cf6d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_de505c29c25463d0cf6d.ogg")
        "那是菜单上最便宜的一杯，十八块。"
        hide screen doc_overlay with dissolve
        voice ("audio/voice/narr_shenlan_f590d0c709cca548a5bb.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f590d0c709cca548a5bb.ogg")
        "我端咖啡的时候，手边正好有小满折的一罐纸星。"
        voice ("audio/voice/narr_shenlan_f75e7ecd7ecaa3f86e55.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f75e7ecd7ecaa3f86e55.ogg")
        "平时点咖啡就能挑一颗，每颗上面都写着字。"
        voice ("audio/voice/narr_shenlan_40c5eb9475960fb166c8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_40c5eb9475960fb166c8.ogg")
        "最上面那颗是我写的，上面就俩字，「撑住」。"

    if pov == "luyao":
        menu:
            "从罐子里挑一颗星":
                $ m2_star = True
                voice ("audio/voice/narr_shenlan_878494c794b4158b21ec.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_878494c794b4158b21ec.ogg")
                "她见我在看罐子，就拿起来让我挑。最上面一颗写着「撑住」，我伸手拿了那颗。"
            "只喝咖啡":
                voice ("audio/voice/narr_shenlan_ec73f354ff28ef50e092.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ec73f354ff28ef50e092.ogg")
                "她把杯子放下来，我把电脑往里挪了挪。"
    else:
        menu:
            "送他一颗写着「撑住」的星":
                $ m2_star = True
                voice ("audio/voice/narr_shenlan_4702e36cf28d49717b74.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4702e36cf28d49717b74.ogg")
                "我把那颗星放在他的碟子旁边。他本来在看电脑，低头时才发现。"
            "只端咖啡过去":
                voice ("audio/voice/narr_shenlan_54959d61ed231825822a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_54959d61ed231825822a.ogg")
                "我把杯子放下，收走了托盘。"

    if m2_star:
        show cg coffee star with dissolve
        voice ("audio/voice/narr_shenlan_ab14b8d5249eef4e60bf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ab14b8d5249eef4e60bf.ogg")
        "碟子小，纸星搁在边上，差一点就滑下去。"
        hide cg coffee star with dissolve

    if pov == "shenlan":
        voice ("audio/voice/narr_shenlan_c02156b73032fefbcc29.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c02156b73032fefbcc29.ogg")
        "他把视线从电脑上挪开了。"
        voice "audio/voice/story_mid_93.ogg"
        luyao "……谢谢。"
        if m2_star:
            voice ("audio/voice/narr_shenlan_c794874239fdd89bd6e5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c794874239fdd89bd6e5.ogg")
            "他小心地把星拈起来，放进了外套口袋。"

    if pov == "luyao":
        menu:
            "告诉她我被裁了":
                $ m2_talk = True
                voice "audio/voice/luyao_8f76001c5b3d719753e6.ogg"
                luyao "我昨天被裁了。"
                voice "audio/voice/shenlan_8c8621756a82c05cf0ac.ogg"
                shenlan "那以后还来喝咖啡吗？"
                voice ("audio/voice/narr_shenlan_a619d96bdc7b2788f072.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a619d96bdc7b2788f072.ogg")
                "我原本准备回答一串关于工作的事，嘴里却只说出了「明天也来」。"
            "继续喝咖啡":
                voice ("audio/voice/narr_shenlan_e96c934a80adcb20fb08.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e96c934a80adcb20fb08.ogg")
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
                voice ("audio/voice/narr_shenlan_ad6eaeaf2a5fe6f2ea96.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ad6eaeaf2a5fe6f2ea96.ogg")
                "他用勺子拨了拨杯柄，没抬头。"
                voice "audio/voice/shenlan_8c8621756a82c05cf0ac.ogg"
                shenlan "那以后还来喝咖啡吗？"
                voice "audio/voice/luyao_8a8f4a6eb33a816d425f.ogg"
                luyao "来吧。明天也有空。"
                voice ("audio/voice/narr_shenlan_69d5b57cd4cdbe907854.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_69d5b57cd4cdbe907854.ogg")
                "我把水杯往他那边推了推。"
            "不开口问":
                voice ("audio/voice/narr_shenlan_36ddc2773ae3906906ab.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_36ddc2773ae3906906ab.ogg")
                "还有一罐糖要添，我端着托盘回了柜台。"

    if pov == "luyao":
        if m2_star:
            voice ("audio/voice/narr_shenlan_d17907944a0e7e504d4b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d17907944a0e7e504d4b.ogg")
            "去换班前，我把「撑住」那颗放进了钱包，和便利店的工牌挨在一起。"
        else:
            voice ("audio/voice/narr_shenlan_f756b8c010ed0af2f56f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f756b8c010ed0af2f56f.ogg")
            "到四点，我在店门外戴上便利店的工牌。她背对着门，正在替下一桌磨豆子。"
    else:
        voice ("audio/voice/narr_shenlan_2d6e1db95046326cadd2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2d6e1db95046326cadd2.ogg")
        "那天他还是坐到了打烊。后来几乎每天都来，只是四点一到就收电脑。"
        if m2_star:
            voice ("audio/voice/narr_shenlan_769dc76f49b27752b3f2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_769dc76f49b27752b3f2.ogg")
            "我往碟子边放的纸星，他每次都会拿走。"
        else:
            voice ("audio/voice/narr_shenlan_b43b32dac29bea896598.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b43b32dac29bea896598.ogg")
            "有一回小满让他自己挑颗星。再后来，他想拿哪颗就自己伸手了。"

    $ unlock_record("first_star")
    if pov == "shenlan":
        scene black with warmfade
        voice ("audio/voice/narr_shenlan_97fd2d68aab567cf726f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_97fd2d68aab567cf726f.ogg")
        "后来陆遥一进门，小满就去拿装美式的那个杯子。"
        voice ("audio/voice/narr_shenlan_355bd8ff3adc5521a769.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_355bd8ff3adc5521a769.ogg")
        "有时候他还没把电脑掏出来，她已经把咖啡端过去了。"
        if m2_star:
            voice ("audio/voice/narr_shenlan_db9dc38b00a98faea455.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_db9dc38b00a98faea455.ogg")
            "星星放哪儿还是我来挑，我有点想看看他会不会哪天忘了拿。"
        else:
            voice ("audio/voice/narr_shenlan_9f0c0d5b6e895a240f2f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9f0c0d5b6e895a240f2f.ogg")
            "小满后来干脆把罐子挪到靠外的一角，让他自己挑。"
    jump scene_card_reader


label scene_card_reader:
    scene black with warmfade
    call screen time_card("几天后", "记录 3 — 刷卡机")

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_dcce968168f2c24be292.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dcce968168f2c24be292.ogg")
        "那天柜台前排到了门口。我听见刷卡机响，已经下意识绕过去看接线口了。"
    else:
        voice ("audio/voice/narr_shenlan_8dd944c4ebad9389006b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8dd944c4ebad9389006b.ogg")
        "排在最前面的客人刷了三回，刷卡机光响，屏幕上那行字怎么也消不掉。"
        voice "audio/voice/story_mid_189.ogg"
        shenlan "……等一下，马上好。"
        voice "audio/voice/story_mid_190.ogg"
        xiaoman "老板，你按那个红色的——"
        voice "audio/voice/story_mid_191.ogg"
        shenlan "哪个红色？"
        voice ("audio/voice/narr_shenlan_31666e2a3336a2009115.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_31666e2a3336a2009115.ogg")
        "小满从旁边探过身来，连按了两下。排头的客人把卡收了回去。"
        show xiaoman pout_half at expr_right with dissolve
        voice "audio/voice/story_mid_194.ogg"
        xiaoman "……不是我。"
        voice ("audio/voice/narr_shenlan_90b23c883a237c980878.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_90b23c883a237c980878.ogg")
        "我还在桌下摸电源，窗边那位已经走到跟前了。"

    show luyao awkward_half at expr_left with dissolve
    voice "audio/voice/story_mid_201.ogg"
    luyao "我看看。"
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_e4ebeb3c6756b5710cab.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e4ebeb3c6756b5710cab.ogg")
        "以前办公室里哪台机器不响了也会有人喊我。等我蹲下去，才发现自己这几天一直在等这句话。"
    else:
        voice ("audio/voice/narr_shenlan_41df909f5c8e11a2238b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_41df909f5c8e11a2238b.ogg")
        "他蹲下来，把机器翻给我看。"
        voice ("audio/voice/narr_shenlan_39678f591862f1a66cf3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_39678f591862f1a66cf3.ogg")
        "底下挤着两根线，我一时也分不清。"

    if pov == "luyao":
        menu:
            "让我来修":
                $ m3_fix = True
                voice ("audio/voice/narr_shenlan_116bb6292fb9b873676d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_116bb6292fb9b873676d.ogg")
                "沈岚让开一个位置，我把网线重新插了一遍，再去找重启键。"
            "让她动手，我在旁边看":
                voice ("audio/voice/narr_shenlan_0f49274b0b68ac627192.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0f49274b0b68ac627192.ogg")
                "她接过机器，手伸向外面那根线。我用指尖在另一头点了点。"
                voice "audio/voice/story_mid_221.ogg"
                luyao "这根。"
    else:
        menu:
            "让他修":
                $ m3_fix = True
                voice "audio/voice/story_mid_228.ogg"
                xiaoman "老板，你就让他修嘛。"
                voice ("audio/voice/narr_shenlan_5a2ce238d8b8d9e5c895.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5a2ce238d8b8d9e5c895.ogg")
                "我往旁边让了让，他拔下网线，又插回去试了试。"
                voice ("audio/voice/narr_shenlan_1d82c6fce5ba70094946.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1d82c6fce5ba70094946.ogg")
                "他低头在那儿找按键，耳朵悄悄红了。"
            "自己修":
                voice ("audio/voice/narr_shenlan_6c9f8ffb59a5e73d7281.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6c9f8ffb59a5e73d7281.ogg")
                "我说不用，自己来。"
                voice ("audio/voice/narr_shenlan_c3210cb213d8051cdaed.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c3210cb213d8051cdaed.ogg")
                "我把机器翻过来，伸手去拔外面那根线。"
                voice ("audio/voice/narr_shenlan_79e5fa10a65b99ca6a0a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_79e5fa10a65b99ca6a0a.ogg")
                "他伸手在另一头点了点。"
                voice "audio/voice/story_mid_235.ogg"
                luyao "这根。"
                voice ("audio/voice/narr_shenlan_ee24e16ed737142bd43f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ee24e16ed737142bd43f.ogg")
                "我换了根线，这回拔对了。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_9fae03e1c1324a231857.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9fae03e1c1324a231857.ogg")
        "小票打出来以后，她问我做什么的。我还是张口就答「程序员」。"
        voice ("audio/voice/narr_shenlan_f52a905c2d006b518a8f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f52a905c2d006b518a8f.ogg")
        "我把翘起来的创可贴按紧了些。包里那张面试通知还露着角，我想等真有消息再跟她讲。"
    else:
        voice ("audio/voice/narr_shenlan_66d59a75be30743dd125.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_66d59a75be30743dd125.ogg")
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
        voice ("audio/voice/narr_shenlan_4321976da3abe5716c15.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4321976da3abe5716c15.ogg")
        "他答得挺快，说完倒不看我了。"
        voice ("audio/voice/narr_shenlan_38b979802fa0ae14a5f4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_38b979802fa0ae14a5f4.ogg")
        "我没忍住，笑了一声。"
        show luyao warm_half at expr_left with dissolve
        voice ("audio/voice/narr_shenlan_e3f7b69973f208d1513c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e3f7b69973f208d1513c.ogg")
        "他抬头看见，又赶紧低下去找工具。"
        voice ("audio/voice/narr_shenlan_cd7acbcd24b5bee3c0e9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cd7acbcd24b5bee3c0e9.ogg")
        "他手背上贴了块创可贴，卷起来那一角都快掉了。"
        voice ("audio/voice/narr_shenlan_fb476b01b38d84a729f5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fb476b01b38d84a729f5.ogg")
        "往包里塞螺丝刀的时候，他带出来半张折好的纸。"

    if pov == "luyao":
        menu:
            "聊聊以前的工作":
                $ m3_ask = True
                voice "audio/voice/story_mid_267.ogg"
                shenlan "你以前……在哪家公司？"
                voice "audio/voice/story_mid_270.ogg"
                luyao "最近在休息。"
                voice ("audio/voice/narr_shenlan_add5963f94101f782702.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_add5963f94101f782702.ogg")
                "我说完就拉上了包。她看了一眼，去替我添水。"
            "接着收工具":
                voice ("audio/voice/narr_shenlan_1a40993a8055746f2db7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1a40993a8055746f2db7.ogg")
                "我把那张纸塞回去，拎着包回窗边坐下。"
    else:
        menu:
            "问问他以前在哪儿工作":
                $ m3_ask = True
                voice "audio/voice/story_mid_281.ogg"
                shenlan "你以前……在哪家公司？"
                voice "audio/voice/luyao_3d87ac9a4f06aa37e200.ogg"
                luyao "那家公司你可能没听过。"
                voice ("audio/voice/narr_shenlan_d2c23774135232a3ccb4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d2c23774135232a3ccb4.ogg")
                "他把工具收回去，没马上往下说。"
                voice "audio/voice/story_mid_284.ogg"
                luyao "最近在休息。"
                voice ("audio/voice/narr_shenlan_99030ab0bce830600d26.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_99030ab0bce830600d26.ogg")
                "他把拉链拉上。我就在心里划掉了后面那句「在哪儿上班」。"
                voice ("audio/voice/narr_shenlan_9e31afca104913bed279.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9e31afca104913bed279.ogg")
                "我也没有再问。"
            "回去忙店里的事":
                voice ("audio/voice/narr_shenlan_a9956d46d3f586746714.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a9956d46d3f586746714.ogg")
                "我没有问。"
                voice ("audio/voice/narr_shenlan_ae95eb48603b13716bc2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ae95eb48603b13716bc2.ogg")
                "他拎起工具包，回窗边坐下。"
                voice ("audio/voice/narr_shenlan_01957c5e030f0f885dad.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_01957c5e030f0f885dad.ogg")
                "那张纸还露着一角，碰到椅子背也没掉。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_615c761bdde2ce2bf072.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_615c761bdde2ce2bf072.ogg")
        "等客人走完，小满才想起来问我的名字。也是那时候，我知道老板叫沈岚。"
    else:
        voice ("audio/voice/narr_shenlan_be5c8772d2da42b1c619.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_be5c8772d2da42b1c619.ogg")
        "等客人都走了，小满给我们换了两杯水，顺便问了句怎么称呼。"
        voice ("audio/voice/narr_shenlan_788344ae00d546e897fe.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_788344ae00d546e897fe.ogg")
        "他说叫他陆遥就行。小满转过来，连我的名字也顺便报了。"
        voice ("audio/voice/narr_shenlan_247df00653cefbe2e570.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_247df00653cefbe2e570.ogg")
        "他临走又点了一杯美式，说要带走。"
        voice ("audio/voice/narr_shenlan_d93ce2b0d11574bc2e8e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d93ce2b0d11574bc2e8e.ogg")
        "我把杯盖按好，往杯子旁边放了颗星。"
        if m3_fix:
            voice ("audio/voice/narr_shenlan_adbec96dd06050f0ebdc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_adbec96dd06050f0ebdc.ogg")
            "他顺手把星和螺丝刀一起塞进包里。"
        else:
            voice ("audio/voice/narr_shenlan_976a10f3b6d25ef320f1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_976a10f3b6d25ef320f1.ogg")
            "他把星拿起来看了看，单独放进一个小兜里。"
    $ unlock_record("card_reader")

    if pov == "shenlan":
        scene black with warmfade
        voice ("audio/voice/narr_shenlan_616a11449bc52a938708.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_616a11449bc52a938708.ogg")
        "那台机器后来又坏了两回。"
        voice ("audio/voice/narr_shenlan_85468957470f715ac9d2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_85468957470f715ac9d2.ogg")
        "头一回我重启了一遍，居然就好了。"
        voice ("audio/voice/narr_shenlan_0401dfe3bbf863f7ac15.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0401dfe3bbf863f7ac15.ogg")
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
        voice ("audio/voice/narr_shenlan_f39a9111afe696fc1103.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f39a9111afe696fc1103.ogg")
        "打烊后，我帮沈岚压住捏泥人的报纸。创可贴粘在纸边上，差点揭下来。那是昨晚收货时，被便利店的纸箱蹭破的。"
        voice ("audio/voice/narr_shenlan_9add6b53ac0bb654484a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9add6b53ac0bb654484a.ogg")
        "我猜她捏的是小满。泥人围裙上有个歪扣子，跟小满那个松了线的挺像。"
    else:
        voice ("audio/voice/narr_shenlan_10b599af7fe485a26916.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_10b599af7fe485a26916.ogg")
        "打烊以后，我在后间铺了张报纸，接着捏那个没捏完的泥人。"
        voice ("audio/voice/narr_shenlan_121e5c3925ccafe33be9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_121e5c3925ccafe33be9.ogg")
        "他就坐在我旁边，帮我把老是卷起来的报纸压着。"
        voice ("audio/voice/narr_shenlan_e821716f5ebca92f74f7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e821716f5ebca92f74f7.ogg")
        "架上是小满缝的兔子，有一只耳朵比另一只短。"
        voice ("audio/voice/narr_shenlan_12b17e8e9c8a5c85b650.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_12b17e8e9c8a5c85b650.ogg")
        "墙上也有她剪的纸星，胶带翘起来了，她总说下回一起补。"
        voice ("audio/voice/narr_shenlan_953bd7e76299fab996c1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_953bd7e76299fab996c1.ogg")
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
        voice ("audio/voice/narr_shenlan_6971d4512980303a52bd.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6971d4512980303a52bd.ogg")
        "我们俩都笑了。"
        voice ("audio/voice/narr_shenlan_6714ac3131ddc8cca3ca.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6714ac3131ddc8cca3ca.ogg")
        "笑完再看，泥人的胳膊已经一长一短了。"
        voice ("audio/voice/narr_shenlan_1211a11d9273c2b588ac.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1211a11d9273c2b588ac.ogg")
        "门口的纸箱动了一下。"
        voice ("audio/voice/narr_shenlan_9f81d28183553763bb60.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9f81d28183553763bb60.ogg")
        "一只三花猫把脑袋探了出来。"
    show mem cat at cat_sit with dissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_9103fc8f7c9d58e67bb7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9103fc8f7c9d58e67bb7.ogg")
        "年糕从纸箱里出来了。它先去蹭沈岚的脚，再探头闻我的手。"
        menu:
            "把手伸过去一起喂":
                $ m4_feed = True
                voice ("audio/voice/narr_shenlan_67f41de80d52741dd129.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_67f41de80d52741dd129.ogg")
                "她摊开手，我也凑过去接了几粒。"
                voice ("audio/voice/narr_shenlan_1b07a2bb8fc3a17ffe16.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1b07a2bb8fc3a17ffe16.ogg")
                "年糕两边都闻了闻，这才开始吃，胡须蹭得我手痒。"
            "接过猫粮自己喂":
                voice ("audio/voice/narr_shenlan_b2684f31198193d78a94.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b2684f31198193d78a94.ogg")
                "我接过猫粮蹲在纸箱边，等到腿麻，年糕才肯吃第一粒。"
    else:
        voice ("audio/voice/narr_shenlan_47a92c2f4cf09ea27790.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_47a92c2f4cf09ea27790.ogg")
        "它戴着个小牌子，上面是小满写的「年糕」。"
        voice "audio/voice/story_mid_354.ogg"
        luyao "……它叫年糕？"
        voice "audio/voice/story_mid_355.ogg"
        shenlan "小满取的。"
        voice "audio/voice/story_mid_356.ogg"
        luyao "挺合适的。"
        voice ("audio/voice/narr_shenlan_7002dbcfa817bf8da074.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7002dbcfa817bf8da074.ogg")
        "它等我们看完，才一步一步蹭过来。"
        menu:
            "一起喂年糕":
                $ m4_feed = True
                voice ("audio/voice/narr_shenlan_4b62ed1919a18f300c94.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4b62ed1919a18f300c94.ogg")
                "我倒出一点猫粮，又分了几粒给他。"
                voice ("audio/voice/narr_shenlan_e8fb07301ca59abf2085.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e8fb07301ca59abf2085.ogg")
                "年糕在我们手心里挑来挑去，最后连碎的也舔干净了。"
            "把猫粮递给他":
                voice ("audio/voice/narr_shenlan_d80e2252d1f70fffe1c1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d80e2252d1f70fffe1c1.ogg")
                "我把猫粮递给他。"
                voice ("audio/voice/narr_shenlan_df6c32ae9e8fb6848152.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_df6c32ae9e8fb6848152.ogg")
                "他在纸箱旁蹲着，摊着只手，等得倒挺有耐心。"
                voice ("audio/voice/narr_shenlan_7722c46924da827cbd92.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7722c46924da827cbd92.ogg")
                "年糕闻了半天，总算吃了一粒。"
                voice ("audio/voice/narr_shenlan_dbcb13b9824b868dc49e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dbcb13b9824b868dc49e.ogg")
                "我看他动了动嘴角，连声音都没出。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_fc461ea063d0001d5424.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fc461ea063d0001d5424.ogg")
        "玻璃门上的告示又在响。她这几天一开门就要看它一眼，我伸手把它摘了。"
        voice "audio/voice/story_mid_391.ogg"
        shenlan "……你干嘛？"
        voice "audio/voice/story_mid_392.ogg"
        luyao "风大。"
        voice ("audio/voice/narr_shenlan_0b4751602532990ebee9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0b4751602532990ebee9.ogg")
        "我把告示折好塞进包里，转让两个字朝里。"
        $ sign_removed = True
    else:
        voice ("audio/voice/narr_shenlan_9223482a9bcaa84cfa09.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9223482a9bcaa84cfa09.ogg")
        "年糕吃完，跳上窗台，团成一团。"
        show screen doc_overlay("prop transfer sign") with dissolve
        voice ("audio/voice/narr_shenlan_e5aa8f8aed5f9344e0d8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e5aa8f8aed5f9344e0d8.ogg")
        "玻璃门上那张转让告示有一角松了，开门时蹭到了门框。"
        hide screen doc_overlay with dissolve
        voice ("audio/voice/narr_shenlan_12349d80e03ba37bfa5f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_12349d80e03ba37bfa5f.ogg")
        "他起来把门掩好。"
        voice ("audio/voice/narr_shenlan_d8570a50950682835f85.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d8570a50950682835f85.ogg")
        "我以为他要把松掉的那角按回去，谁知他把整张纸都摘了。"
        voice "audio/voice/story_mid_400.ogg"
        shenlan "……你干嘛？"
        voice "audio/voice/story_mid_401.ogg"
        luyao "风大。"
        voice ("audio/voice/narr_shenlan_2ddeb1b647cf6d446d5b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2ddeb1b647cf6d446d5b.ogg")
        "他把纸折了两折，往电脑包里一塞。"
        $ sign_removed = True
        voice ("audio/voice/narr_shenlan_276961ca4d9ab33e368b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_276961ca4d9ab33e368b.ogg")
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
                voice ("audio/voice/narr_shenlan_d8e0544378e3c0450032.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d8e0544378e3c0450032.ogg")
                "我刚答完，便利店的店长就发来消息，问明晚还能不能顶班。"
            "只说有点事":
                voice "audio/voice/story_mid_417.ogg"
                shenlan "你每天四点走……是有事吗？"
                voice "audio/voice/story_mid_419.ogg"
                luyao "有点事。"
                voice ("audio/voice/narr_shenlan_54e652aa0c0979014876.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_54e652aa0c0979014876.ogg")
                "店长刚问我明晚能不能顶班。我还没回消息，先把手机揣了起来。"
    else:
        menu:
            "问他四点以后去哪儿":
                $ m4_ask = True
                voice "audio/voice/story_mid_427.ogg"
                shenlan "你每天四点走……是有事吗？"
                voice ("audio/voice/narr_shenlan_cfd0d31b7438efc233e5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cfd0d31b7438efc233e5.ogg")
                "他把包带往肩上提了提。"
                voice "audio/voice/story_mid_429.ogg"
                luyao "有点事。"
                voice ("audio/voice/narr_shenlan_d65b911a069e4d799a06.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d65b911a069e4d799a06.ogg")
                "再问一句就真成查岗了。我只好说，明天见。"
            "不问他的事":
                voice ("audio/voice/narr_shenlan_f33f39549a197e0c2521.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f33f39549a197e0c2521.ogg")
                "四点一到，他就拿上了包。"
                voice ("audio/voice/narr_shenlan_145e94190359a3a8625e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_145e94190359a3a8625e.ogg")
                "他都碰到门把了，还回头朝我看了一眼。"
                voice ("audio/voice/narr_shenlan_8d6fbd4b8333f45d335a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8d6fbd4b8333f45d335a.ogg")
                "最后就说了声「明天见」。"

    if pov == "shenlan":
        voice ("audio/voice/narr_shenlan_61f43afa6fe127fcd954.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_61f43afa6fe127fcd954.ogg")
        "他走了以后，我从小满贴纸星剩下的纸里挑了一张，给泥人剪了条围巾。"
        voice ("audio/voice/narr_shenlan_c675950428a339c27627.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c675950428a339c27627.ogg")
        "捏的到底是谁，我还没想好。"
        voice ("audio/voice/narr_shenlan_4c7daad0ded0771abea5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4c7daad0ded0771abea5.ogg")
        "年糕跳下来蹭我的脚，我这才想起来猫碗该添水了。"
    $ unlock_record("shop_cat")

    if pov == "shenlan":
        scene black with warmfade
        voice ("audio/voice/narr_shenlan_c2ca0c313dd79f9ff1e7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c2ca0c313dd79f9ff1e7.ogg")
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
    voice ("audio/voice/narr_shenlan_0772b68eaeff071e2b45.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0772b68eaeff071e2b45.ogg")
    "他每天下午就在窗边那一小块地方坐着，一开电脑就是几个小时。"
    voice ("audio/voice/narr_shenlan_996b3de07d4073291552.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_996b3de07d4073291552.ogg")
    "有一天，我从柜台下面翻了本旧星图册出来。"
    voice "audio/voice/shenlan_a29b87ac82a056dbeca9.ogg"
    shenlan "你要不要歇会儿？我这儿有本书。"
    voice "audio/voice/story_mid_481.ogg"
    luyao "……这是给我的？"
    voice "audio/voice/story_mid_482.ogg"
    shenlan "借你的。看完还我。"
    voice ("audio/voice/narr_shenlan_87084625e4027ef8ab19.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_87084625e4027ef8ab19.ogg")
    "他接过去翻了几页，手指停在猎户座那张图上。"

    voice ("audio/voice/narr_shenlan_0f73302a55e529582f5b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0f73302a55e529582f5b.ogg")
    "第二天下午，他把书搁到柜台上，指给我看猎户座那一页。"
    voice ("audio/voice/narr_shenlan_ba609caa9b506d85d1a9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ba609caa9b506d85d1a9.ogg")
    "页边多了一行铅笔字：「你柜台上那三颗星，排得跟猎户座的腰带一样。」"
    voice ("audio/voice/narr_shenlan_97d7b59e3103b53bc69c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_97d7b59e3103b53bc69c.ogg")
    "我抬头数了数。第四颗滚到罐子后面了，得伸手才够得着。"

    menu:
        "在页边回他一句":
            $ m6_write = True
            voice ("audio/voice/narr_shenlan_7cc1e87701015931646c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7cc1e87701015931646c.ogg")
            "我拿铅笔在底下添了一行：「你漏数一颗。在罐子后面。」"
            voice ("audio/voice/narr_shenlan_736470f0338f7130cc6c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_736470f0338f7130cc6c.ogg")
            "铅笔印按得有点重。我拿橡皮在上面比画了一下，最后还是没擦。"
        "合上书，把它放回柜台":
            voice ("audio/voice/narr_shenlan_21f3137e305836d71d03.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_21f3137e305836d71d03.ogg")
            "我合上书，让它在柜台上待了一天。"

    voice ("audio/voice/narr_shenlan_94cc14ee126b56ece8f7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_94cc14ee126b56ece8f7.ogg")
    "第二天他又来借，下午就还了。"
    voice ("audio/voice/narr_shenlan_32052d29df6b09d0f02a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_32052d29df6b09d0f02a.ogg")
    "我翻到同一页，他果然又往下写了一行。"

    if m6_write:
        voice ("audio/voice/narr_shenlan_d0e10fcac0435d34c544.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d0e10fcac0435d34c544.ogg")
        "「那第四颗算哪儿的？」"
        voice ("audio/voice/narr_shenlan_5ca3fd85f58c746ff6c1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5ca3fd85f58c746ff6c1.ogg")
        "我本来在擦桌子，看完转身就去把那颗掉队的星先往前摆了一点。"
    else:
        voice ("audio/voice/narr_shenlan_1f1a2a0e51062f55e14b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1f1a2a0e51062f55e14b.ogg")
        "「今天我数过了，真有四颗。」"
        voice ("audio/voice/narr_shenlan_4c9f36850be20037ac42.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4c9f36850be20037ac42.ogg")
        "他大概是趁我不注意去看过了。"

    voice ("audio/voice/narr_shenlan_172fc354a8fac3c47c59.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_172fc354a8fac3c47c59.ogg")
    "书翻到一半，掉出一朵压干的满天星。"
    voice ("audio/voice/narr_shenlan_be8ee979a00efecae309.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_be8ee979a00efecae309.ogg")
    "我托着花梗，小心地把它放回了原处。"
    voice ("audio/voice/narr_shenlan_dd4d84f651d38593396d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dd4d84f651d38593396d.ogg")
    "就在那页的右下角，有几个字被铅笔划掉了。"
    menu:
        "问他划掉了什么":
            $ m6_ask = True
            voice ("audio/voice/narr_shenlan_05547a398422174ff4f7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_05547a398422174ff4f7.ogg")
            "我转过书，让他看看右下角。"
            voice "audio/voice/story_mid_554.ogg"
            shenlan "这行划掉的是什么？"
            show luyao awkward_half at expr_right with dissolve
            voice "audio/voice/story_mid_556.ogg"
            luyao "……写错了。"
            voice ("audio/voice/narr_shenlan_d8d1b0827f1c88d7cb38.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d8d1b0827f1c88d7cb38.ogg")
            "他拿手指去盖的时候，我已经看清了。写的是「留下来」。"
        "合上书，不问他":
            voice ("audio/voice/narr_shenlan_1832253520056246af8f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1832253520056246af8f.ogg")
            "我没问，合上书之前又看了一眼。"
            voice ("audio/voice/narr_shenlan_3e42d4ce33a05510de85.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3e42d4ce33a05510de85.ogg")
            "那几道横线底下，还能看出是「留下来」。"

    voice ("audio/voice/narr_shenlan_d13e442b077c26f9a999.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d13e442b077c26f9a999.ogg")
    "打烊后，我把书留在柜台上，底下压着几张还没付的账单。"



    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_e64730c32ae73f9593e8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e64730c32ae73f9593e8.ogg")
    "第二天小满看见书，问我能不能借她翻翻。"
    voice ("audio/voice/narr_shenlan_6457a6b1cedf72b878f6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6457a6b1cedf72b878f6.ogg")
    "还回来时，她在最后一页画了颗星，五个角画得长短不一。"
    voice "audio/voice/story_mid_589.ogg"
    xiaoman "老板，这书挺好看的。"
    voice ("audio/voice/narr_shenlan_36958f41cab189e78393.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_36958f41cab189e78393.ogg")
    "我把书塞回柜台底下，下回谁想看都能拿。"
    $ unlock_record("book_margin")

    scene black with warmfade
    voice ("audio/voice/narr_shenlan_11b406b246809adfa07e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_11b406b246809adfa07e.ogg")
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
        voice ("audio/voice/narr_shenlan_a2657a5f635cf514b0d2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a2657a5f635cf514b0d2.ogg")
        "招牌的线松了。我踩上梯子把它接回去，一低头，看见沈岚两只手都扶在梯子上，等我下来。"
    else:
        voice ("audio/voice/narr_shenlan_c3483e4de2f97770caef.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c3483e4de2f97770caef.ogg")
        "入了秋，下午刚过五点，街对面就看不清人脸了。"
        voice ("audio/voice/narr_shenlan_6bdb06df1a8c30aada6c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6bdb06df1a8c30aada6c.ogg")
        "对面几家店都亮了灯，我这边的招牌还黑着。"
        voice ("audio/voice/narr_shenlan_48b4fc7b5b63e238e2c6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_48b4fc7b5b63e238e2c6.ogg")
        "他走到门外，仰头看招牌，半天没进来。"
        voice "audio/voice/story_mid_614.ogg"
        luyao "有梯子吗？"
        voice "audio/voice/story_mid_615.ogg"
        shenlan "……你要修？"
        voice "audio/voice/story_mid_616.ogg"
        luyao "试试。"
        voice ("audio/voice/narr_shenlan_e2cc28049dead2371aa3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e2cc28049dead2371aa3.ogg")
        "我把后间的梯子搬出来。"
        voice ("audio/voice/narr_shenlan_a661f442dd33683b621b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a661f442dd33683b621b.ogg")
        "他踩到最上头两级，把松了的线重新接上。"
        voice ("audio/voice/narr_shenlan_39f44380821cbbb857ad.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_39f44380821cbbb857ad.ogg")
        "我在下面扶梯子，看他外套肩头的颜色一点点变深。"
        voice ("audio/voice/narr_shenlan_31fcb23fbb35c8871b50.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_31fcb23fbb35c8871b50.ogg")
        "我们往后站了站。招牌终于亮了，门口的水洼也跟着亮起来。"
        voice "audio/voice/story_mid_626.ogg"
        shenlan "……好了。"
    show luyao warm_half at expr_right with dissolve
    if pov == "shenlan":
        voice "audio/voice/story_mid_628.ogg"
        luyao "好了。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_a7c51c81be9f0307d1f3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a7c51c81be9f0307d1f3.ogg")
        "她有颗纸星要给我，拇指正好盖住了字。"
    else:
        voice ("audio/voice/narr_shenlan_a2a6fc7759a375aa0f6d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a2a6fc7759a375aa0f6d.ogg")
        "我摸出预先放在围裙口袋里的一颗纸星。"
        voice ("audio/voice/narr_shenlan_e168f8df682c8e5d9cf0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e168f8df682c8e5d9cf0.ogg")
        "上面是我写的「留下」。"
        voice ("audio/voice/narr_shenlan_998112f0576ed1f26150.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_998112f0576ed1f26150.ogg")
        "那两个字不知道怎么开口，倒是早就写好了。"

    if pov == "luyao":
        menu:
            "伸手接过来":
                $ m7_star = True
                voice ("audio/voice/narr_shenlan_2c4f4498c34a74f7180a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2c4f4498c34a74f7180a.ogg")
                "我接过来，把星转了个面。她写的是「留下」。我顺手把那根细绳系在了电脑包上。"
            "先去收梯子":
                voice ("audio/voice/narr_shenlan_1d3024f6d12afe073fc5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1d3024f6d12afe073fc5.ogg")
                "我转身把梯子合上。再看她的时候，她手已经放回口袋了。"
    else:
        menu:
            "把星送给他":
                $ m7_star = True
                voice ("audio/voice/narr_shenlan_db0470c79bed6a01f19b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_db0470c79bed6a01f19b.ogg")
                "我把星递过去。"
                voice "audio/voice/story_mid_656.ogg"
                shenlan "给你。"
                voice "audio/voice/story_mid_657.ogg"
                luyao "……这上面写的什么？"
                voice "audio/voice/story_mid_658.ogg"
                shenlan "你自己看。"
                voice ("audio/voice/narr_shenlan_d328f94586db581bb584.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d328f94586db581bb584.ogg")
                "他把纸星转了个面，这才看见那两个字。"
                voice ("audio/voice/narr_shenlan_e48881fdc78bbb5b5476.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e48881fdc78bbb5b5476.ogg")
                "我以为他又要塞进口袋，他却用上面那根绳系在了包上。"
            "把星放回口袋":
                voice ("audio/voice/narr_shenlan_d4eeb4db1f6434a0cd92.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d4eeb4db1f6434a0cd92.ogg")
                "我握着星把手缩了回去。"
                voice ("audio/voice/narr_shenlan_7d133b52321b57919807.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7d133b52321b57919807.ogg")
                "他正忙着收梯子，没看见。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_3ae2c0de723de0120b4d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3ae2c0de723de0120b4d.ogg")
        "电话是阿哲打来的。我过了马路才接。他说，那边连下个月的工位都给我留好了。"
        voice ("audio/voice/narr_shenlan_e9351f3b5270b960b146.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e9351f3b5270b960b146.ogg")
        "我盯着对面刚亮起来的招牌，还是请他再给我几天。沈岚就扶着门，在等我回去。"
        if m7_star:
            voice ("audio/voice/narr_shenlan_97cd97c5f4b6dece005e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_97cd97c5f4b6dece005e.ogg")
            "拉链上那颗星被我攥了一路，幸好还没淋透。"
    else:
        voice ("audio/voice/narr_shenlan_1c1b9aa471b1a4d4b6b4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1c1b9aa471b1a4d4b6b4.ogg")
        "他刚下来，手机就响了。"
        voice ("audio/voice/narr_shenlan_1dbf31fdf215be4e51bc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1dbf31fdf215be4e51bc.ogg")
        "他看了一眼来电，过了马路才接。"
        voice ("audio/voice/narr_shenlan_2e3729de0efefd089588.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2e3729de0efefd089588.ogg")
        "他伞也没拿，我只好扶着门等他。"
        voice ("audio/voice/narr_shenlan_10ea0996d7907e5777ba.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_10ea0996d7907e5777ba.ogg")
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
                voice ("audio/voice/narr_shenlan_aa22da95597063412879.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_aa22da95597063412879.ogg")
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
                voice ("audio/voice/narr_shenlan_8f3e03a4afbf37fc0c16.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8f3e03a4afbf37fc0c16.ogg")
                "我从柜台上够了几张纸巾，递给他擦头发。"
            "先回店里":
                voice ("audio/voice/narr_shenlan_818ec4af343984da12b5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_818ec4af343984da12b5.ogg")
                "我往旁边让了让，等他进来再关门。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_c4a98efdb327b3d5abcf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c4a98efdb327b3d5abcf.ogg")
        "小满在窗边开了串灯。那晚回去，我又点开阿哲的消息，屏幕亮到自己熄了，我还是没回。"
    else:
        scene bg shop night with paperdissolve
        show fx lamp night
        show xiaoman neutral_bust at expr_right with dissolve
        voice ("audio/voice/narr_shenlan_af6735fa572860812d32.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_af6735fa572860812d32.ogg")
        "我一进门，发现小满正踩着凳子往窗边挂灯。"
        voice "audio/voice/story_mid_718.ogg"
        xiaoman "老板，你看。"
        voice ("audio/voice/narr_shenlan_f062f10f53383fd7f170.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f062f10f53383fd7f170.ogg")
        "暖黄色的小灯从柜台一直挂到窗边。"
        voice "audio/voice/xiaoman_7acb0d79e7c4a7338f41.ogg"
        xiaoman "老板，晚上就开这串吧，外头也能看见。"
        voice ("audio/voice/narr_shenlan_e8f38671d5899fcf03c6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e8f38671d5899fcf03c6.ogg")
        "她还有一截线没挂好，说完又找了块胶带。"
        scene black with warmfade
        voice ("audio/voice/narr_shenlan_2fa924078e7ec9db6a36.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2fa924078e7ec9db6a36.ogg")
        "天一黑我就开店招，有时候连小满那串灯也一起开。"
        if m7_star:
            voice ("audio/voice/narr_shenlan_bd4a217cede388fba544.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bd4a217cede388fba544.ogg")
            "陆遥拉开电脑包，那颗星就会跟着晃一下。"
        else:
            voice ("audio/voice/narr_shenlan_c4e4ae9610832e738a26.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c4e4ae9610832e738a26.ogg")
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
        voice ("audio/voice/narr_shenlan_d27e5408e3f9a7a1d607.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d27e5408e3f9a7a1d607.ogg")
        "我说顺路，要送她回去。其实我前两晚都在店里睡，连钥匙还在我兜里。"
        voice ("audio/voice/narr_shenlan_8d7cbd18da93d6dcebe4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8d7cbd18da93d6dcebe4.ogg")
        "走到第一个路口，我把伞往她那边偏了偏，袖子立刻就湿了。"
    else:
        voice ("audio/voice/narr_shenlan_49f0fe6a2db92a54ebe7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_49f0fe6a2db92a54ebe7.ogg")
        "那天打烊的时候，雨大到站在檐下也会被溅到。"
        voice ("audio/voice/narr_shenlan_e5e430c921fe733c5a39.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e5e430c921fe733c5a39.ogg")
        "我锁门的时候，陆遥已经撑着伞在台阶下等了。"
        voice "audio/voice/story_mid_752.ogg"
        shenlan "你还没走？"
        voice "audio/voice/story_mid_753.ogg"
        luyao "顺路。"
        voice ("audio/voice/narr_shenlan_65c89652fff56e5af7f7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_65c89652fff56e5af7f7.ogg")
        "他说顺路，可他平常都是往另一头走的。"
        voice ("audio/voice/narr_shenlan_9e8bbfeb59364d5cf8d8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9e8bbfeb59364d5cf8d8.ogg")
        "我把钥匙收好，站到他的伞下面。"
        voice ("audio/voice/narr_shenlan_11df151328482a91ff15.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_11df151328482a91ff15.ogg")
        "走到路口等灯，我才发现他把伞几乎全偏到了我这边。"
        voice ("audio/voice/narr_shenlan_ce0122cb0aa34ab1e44b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ce0122cb0aa34ab1e44b.ogg")
        "他右边袖子都湿透了，还举着伞不动。"

    if pov == "luyao":
        menu:
            "伸手碰一碰她":
                $ m8_hand = True
                voice ("audio/voice/narr_shenlan_2702ede37fcd0d22cc0f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2702ede37fcd0d22cc0f.ogg")
                "我碰了碰她的手背。她把手指张开，等我握上去。"
            "把手留在口袋里":
                voice ("audio/voice/narr_shenlan_894b7e5e67fc453841d1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_894b7e5e67fc453841d1.ogg")
                "她让我把伞往自己这边挪挪。我从兜里腾出手，扶住被风吹歪的伞柄。"
    else:
        menu:
            "握住他的手":
                $ m8_hand = True
                voice ("audio/voice/narr_shenlan_8fa6bd13bc8f5de3904f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8fa6bd13bc8f5de3904f.ogg")
                "我把手从兜里抽出来，轻轻碰了碰他的手背。"
                voice ("audio/voice/narr_shenlan_c4dee7ba25192742a353.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c4dee7ba25192742a353.ogg")
                "他把伞换到另一只手，把空出来的手递给我。"
                voice ("audio/voice/narr_shenlan_3d4ac4bc9cc7c0e284d3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3d4ac4bc9cc7c0e284d3.ogg")
                "过了马路，他才想起来把伞往自己那头挪一点。"
            "把手留在口袋里":
                voice ("audio/voice/narr_shenlan_4832065aa95a06ef94fc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4832065aa95a06ef94fc.ogg")
                "我缩在伞下面，让他把伞往回挪一点。"
                voice ("audio/voice/narr_shenlan_1cddc80eca4337c2180a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1cddc80eca4337c2180a.ogg")
                "他低头看了看袖子，往回挪了一点点。"
                voice ("audio/voice/narr_shenlan_4eef0bda16e5d6dfe9bc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4eef0bda16e5d6dfe9bc.ogg")
                "到了下一个路口，伞又偏回来了。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_d88f664f51a86b3b9d43.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d88f664f51a86b3b9d43.ogg")
        "到了她家楼下，我收了伞。店里还有半杯咖啡，也许喝完就有力气爬回出租屋了。"
    else:
        voice ("audio/voice/narr_shenlan_9928be708bb9031c5497.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9928be708bb9031c5497.ogg")
        "走到那栋楼下面的时候，雨总算小了些。"
        voice ("audio/voice/narr_shenlan_4c085793487250e8ecd3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4c085793487250e8ecd3.ogg")
        "他把伞收在台阶下面。我走上两级，才发现他没跟上来。"
        voice ("audio/voice/narr_shenlan_9451069d4c6464bde511.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9451069d4c6464bde511.ogg")
        "楼道灯隔着一盏亮一盏，非得走近了才知道哪盏是坏的。"

    if pov == "luyao":
        menu:
            "提议再坐一会儿":
                $ m8_invite = True
                voice ("audio/voice/narr_shenlan_57fad7936d60385ca2c9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_57fad7936d60385ca2c9.ogg")
                "我问她能不能上去坐会儿。她看了眼楼道。"
                voice "audio/voice/story_mid_802.ogg"
                shenlan "……下次吧。"
                voice ("audio/voice/narr_shenlan_a979e9547fabb8d02ed3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a979e9547fabb8d02ed3.ogg")
                "她嘱咐我回去早点睡。我应得很快，忘了她还不知道我这几晚睡在哪儿。"
            "说晚安。":
                voice ("audio/voice/narr_shenlan_b916f393deb114d11761.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b916f393deb114d11761.ogg")
                "我跟她说了晚安。等楼上亮了灯，我才转身，踩着刚才的脚印往店里走。"
        $ unlock_record("umbrella")
        jump story_days_late
    else:
        menu:
            "问他要不要上来坐坐":
                $ m8_invite = True
                voice "audio/voice/story_mid_816.ogg"
                shenlan "要不要上来坐一会儿？"
                voice ("audio/voice/narr_shenlan_0f15264e3ea402624100.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0f15264e3ea402624100.ogg")
                "他抬头看了看楼上。"
                voice "audio/voice/story_mid_818.ogg"
                luyao "……下次吧。"
                voice ("audio/voice/narr_shenlan_0cdf2435deac47224b3a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0cdf2435deac47224b3a.ogg")
                "他又说，让我早点睡。"
                voice ("audio/voice/narr_shenlan_9b9bc4a2558a1eec0ea0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9b9bc4a2558a1eec0ea0.ogg")
                "我往他这边迈了一级台阶，最后还是只说了句「好」。"
            "说晚安。":
                voice ("audio/voice/narr_shenlan_453d94b684f36d087d4a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_453d94b684f36d087d4a.ogg")
                "我说：「谢谢你送我。」"
                voice "audio/voice/story_mid_823.ogg"
                luyao "顺路。"
                voice ("audio/voice/narr_shenlan_83ad02aca4f83eb7e3ae.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_83ad02aca4f83eb7e3ae.ogg")
                "他这回答得比刚才还快。"
                voice ("audio/voice/narr_shenlan_20c93afabd21baace05a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_20c93afabd21baace05a.ogg")
                "我也没忍住，笑着跟他说了声晚安。"
                voice ("audio/voice/narr_shenlan_637a2d904b48bc971ce7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_637a2d904b48bc971ce7.ogg")
                "后来我开灯的时候，从窗户看见他才撑伞往回走。"

    scene black with dissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_09c8ab293a08e1576208.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_09c8ab293a08e1576208.ogg")
        "后来有段时间，我每天下午都来，还是点最便宜的美式。"
        voice ("audio/voice/narr_shenlan_ee71110947d4b241b17e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ee71110947d4b241b17e.ogg")
        "她有时会多拿一颗星，放在我碟子边，一下午也不收走。"
        voice ("audio/voice/narr_shenlan_bb2a0b49dab9ca9ad0c0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bb2a0b49dab9ca9ad0c0.ogg")
        "打烊早的时候，她会叫我过去弹给她听。"
        voice ("audio/voice/narr_shenlan_0a613858b01cc1cf45c2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0a613858b01cc1cf45c2.ogg")
        "我前面都弹得好好的，偏偏到最后一下就按错。"
        voice ("audio/voice/narr_shenlan_8e8212d9d8a660cb92c4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e8212d9d8a660cb92c4.ogg")
        "她也不拆穿，往边上挪挪，两个人再弹一遍。"
    else:
        voice ("audio/voice/narr_shenlan_1267a6fc6015243d3e56.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1267a6fc6015243d3e56.ogg")
        "后来有段时间，下午一到，窗边总有人。"
        voice ("audio/voice/narr_shenlan_a2fb3231d4018e7f78fc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a2fb3231d4018e7f78fc.ogg")
        "他还是一来就点美式。"
        voice ("audio/voice/narr_shenlan_1378d8a564a50b379e1a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1378d8a564a50b379e1a.ogg")
        "有时我会多拿一颗星，也不给他，就在他那个碟子边放一下午。"
        voice ("audio/voice/narr_shenlan_9a0813a672d93f875e6f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9a0813a672d93f875e6f.ogg")
        "有几回打烊早，我就叫他过来弹给我听。"
        voice ("audio/voice/narr_shenlan_a823ac698b3447eee38a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a823ac698b3447eee38a.ogg")
        "他前面都弹得好好的，偏偏到最后一下就按错。"
        voice ("audio/voice/narr_shenlan_ee75bad10207224ca6ad.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ee75bad10207224ca6ad.ogg")
        "我也不拆穿他，往边上挪挪，两个人再弹一遍。"
    scene cg piano lesson with dissolve
    scene bg back room with dissolve
    voice ("audio/voice/narr_shenlan_3993fdf7247b021f7ead.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3993fdf7247b021f7ead.ogg")
    "那本星图册谁也不带回家了，翻完就塞回柜台下面。"
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_4ec966449e5d42eb9955.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4ec966449e5d42eb9955.ogg")
        "快到四点时，年糕就跳上窗台。等我出了门才跳下来。"
    else:
        voice ("audio/voice/narr_shenlan_e6536e5a5ce03cf35c86.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e6536e5a5ce03cf35c86.ogg")
        "快到四点时，年糕就跳上窗台。等他出了门才跳下来。"
    voice ("audio/voice/narr_shenlan_f4e215268250be60b76f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f4e215268250be60b76f.ogg")
    "小满在墙上又贴了一排星，踩着凳子才贴得到。"

    scene bg shop day with paperdissolve
    show xiaoman neutral_bust at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_434024197bf21b238aff.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_434024197bf21b238aff.ogg")
    "隔天下午，小满擦着擦着杯子，突然凑了过来。"
    voice "audio/voice/story_mid_866.ogg"
    xiaoman "老板，昨晚谁送你回来的？"
    voice "audio/voice/shenlan_d0ac7bc45c8acc901894.ogg"
    shenlan "他正好顺路。"
    voice "audio/voice/story_mid_868.ogg"
    xiaoman "哦——"
    voice ("audio/voice/narr_shenlan_3f1ffa99ce4092ba3e31.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3f1ffa99ce4092ba3e31.ogg")
    "她拖着调子应了一声，回头就去拿陆遥常用的那只杯子。"
    $ unlock_record("umbrella")

    scene black with warmfade
    voice ("audio/voice/narr_shenlan_90090be8e2b7e63e6b98.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_90090be8e2b7e63e6b98.ogg")
    "后来那把伞就放在门边，谁赶上下雨谁拿。"
    voice ("audio/voice/narr_shenlan_cceb92832c1ee422dc05.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cceb92832c1ee422dc05.ogg")
    "黑柄上那圈胶带是后来缠的，它折过一回。"
    voice ("audio/voice/narr_shenlan_4da3f08953e5753cf726.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4da3f08953e5753cf726.ogg")
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
    voice ("audio/voice/narr_shenlan_4cf19e90173547697d9e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4cf19e90173547697d9e.ogg")
    "房东挑了个没客人的时候来。"
    show landlord neutral_half at expr_left with dissolve
    voice ("audio/voice/narr_shenlan_08fd21140f699d48ed58.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_08fd21140f699d48ed58.ogg")
    "他站在柜台前，从牛皮纸袋里往外抽文件。"
    voice ("audio/voice/narr_shenlan_114a5ece1fe73cb8f673.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_114a5ece1fe73cb8f673.ogg")
    "小满倒了杯水给他，端着托盘退到后间。门还开着。"
    voice ("audio/voice/narr_shenlan_90903a78de8d498d85dc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_90903a78de8d498d85dc.ogg")
    "他从里面抽出来一份续租合同，推到我面前。"
    show screen doc_overlay("prop lease doc") with dissolve
    voice ("audio/voice/narr_shenlan_4c9c4d8f29f10fe3d5fc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4c9c4d8f29f10fe3d5fc.ogg")
    "我先去看每月租金。"
    hide screen doc_overlay with dissolve
    voice "audio/voice/story_mid_904.ogg"
    landlord "楼要卖了。新房东要重新签，租金按市价。"
    voice "audio/voice/story_mid_905.ogg"
    shenlan "……多少？"
    voice ("audio/voice/narr_shenlan_6bf0f463bf60d3839e45.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6bf0f463bf60d3839e45.ogg")
    "房东在我面前用手指点了点那个数字。"
    voice ("audio/voice/narr_shenlan_ff0b5e3b1242c826978f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ff0b5e3b1242c826978f.ogg")
    "我按着底下那行小字算了算，押两个月，还得先付三个月。"
    voice ("audio/voice/narr_shenlan_2bac074987d845cfd445.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2bac074987d845cfd445.ogg")
    "就算只算头一笔，账上也凑不出来。"

    voice "audio/voice/story_mid_910.ogg"
    landlord "我也不想涨。可新房东按合同来，我也没办法。"
    voice "audio/voice/story_mid_911.ogg"
    shenlan "……期限呢？"
    voice "audio/voice/story_mid_912.ogg"
    landlord "下个月十五号之前。签了，就按新价；不签，十五号之后腾房。"
    voice ("audio/voice/narr_shenlan_8d4f20640bdfc8f4437b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8d4f20640bdfc8f4437b.ogg")
    "他把纸往我手边又推了一点。"
    voice "audio/voice/story_mid_914.ogg"
    landlord "小沈，你这店开了几年了？"
    voice "audio/voice/story_mid_915.ogg"
    shenlan "三年。"
    voice "audio/voice/story_mid_916.ogg"
    landlord "嗯。"
    voice ("audio/voice/narr_shenlan_eebcaf9b6e35a5666fd2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_eebcaf9b6e35a5666fd2.ogg")
    "他把剩下的话咽了回去，低头喝了口水。"

    menu:
        "先签下续租合同":
            $ m10_signed = True
            voice ("audio/voice/narr_shenlan_1d07cb15815caf26ddcb.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1d07cb15815caf26ddcb.ogg")
            "我把合同拉过来，把名字签在了最底下。"
            voice ("audio/voice/narr_shenlan_9c3901ab7a8df3bc203c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9c3901ab7a8df3bc203c.ogg")
            "签完我又看了眼金额，笔盖扣了两次才扣上。"
            voice ("audio/voice/narr_shenlan_dca334f28fbd69d73efe.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dca334f28fbd69d73efe.ogg")
            "房东收起一份，把另一份留给了我。"
            voice "audio/voice/story_mid_925.ogg"
            landlord "十五号之前把第一笔打过来就行。"
            voice ("audio/voice/narr_shenlan_f6d5a2b7e6ae31993230.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f6d5a2b7e6ae31993230.ogg")
            "我点头。"
        "先把合同留下，再想想":
            voice ("audio/voice/narr_shenlan_dced635f08dd246b5c9a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dced635f08dd246b5c9a.ogg")
            "我把笔放了回去，说还要再想想。"
            voice "audio/voice/story_mid_929.ogg"
            landlord "行。十五号之前给我个准话。"
            voice ("audio/voice/narr_shenlan_1d384fe8bfacb56e58f1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1d384fe8bfacb56e58f1.ogg")
            "他把文件袋往胳膊下一夹。"
            hide landlord with dissolve
            voice ("audio/voice/narr_shenlan_7408559fe5f4dc86c1d7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7408559fe5f4dc86c1d7.ogg")
            "合同还在柜台上，他走了我也没去收。"

    scene bg shop night with paperdissolve
    show fx lamp night
    show xiaoman worried_half at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_6aa3b0424032c01b315c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6aa3b0424032c01b315c.ogg")
    "打烊以后，我把续租合同和几张没付的账单叠起来往抽屉里塞。"
    voice ("audio/voice/narr_shenlan_1dc4f111daa465771250.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1dc4f111daa465771250.ogg")
    "纸太多了。关抽屉时，还有一角露在外头。"
    voice ("audio/voice/narr_shenlan_ff3005ceaaff0ccfc42f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ff3005ceaaff0ccfc42f.ogg")
    "小满就站在后间门口，好像有话要说。"
    voice "audio/voice/story_mid_940.ogg"
    xiaoman "老板。"
    voice "audio/voice/story_mid_941.ogg"
    shenlan "嗯？"
    voice "audio/voice/story_mid_942.ogg"
    xiaoman "……没事。"
    voice ("audio/voice/narr_shenlan_afa905b4e7fa5fb27703.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_afa905b4e7fa5fb27703.ogg")
    "她给我换了杯温水，这才去擦桌子。"

    menu:
        "告诉陆遥店可能要关":
            $ m10_told = True
            voice ("audio/voice/narr_shenlan_25d5d25c76b94ab13d51.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_25d5d25c76b94ab13d51.ogg")
            "我点开陆遥的头像，发了一句「店可能要关了」。"
            voice ("audio/voice/narr_shenlan_e3865dde0975bf0b826f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e3865dde0975bf0b826f.ogg")
            "他几乎是立刻回过来：「我马上过来。」"
            voice ("audio/voice/narr_shenlan_9f95c9810ab622790f9e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9f95c9810ab622790f9e.ogg")
            "那天晚上他果然又来了，到了店里也没往窗边坐。"
            voice "audio/voice/story_mid_952.ogg"
            luyao "差多少？"
            voice "audio/voice/story_mid_953.ogg"
            shenlan "……不用你管。"
            voice "audio/voice/story_mid_954.ogg"
            luyao "我问差多少。"
            voice ("audio/voice/narr_shenlan_efe32a209f2d1c982f34.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_efe32a209f2d1c982f34.ogg")
            "我把手搭在抽屉的拉手上，没拉开。"
            voice ("audio/voice/narr_shenlan_e52c09d3da22eb2af7d1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e52c09d3da22eb2af7d1.ogg")
            "他站了一会儿，见我不说话就走了。"
            voice ("audio/voice/narr_shenlan_1f80bc067da718752b46.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1f80bc067da718752b46.ogg")
            "第二天，他没有来。"
        "先不告诉他":
            voice ("audio/voice/narr_shenlan_1e23235bfbd4d9e057cb.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1e23235bfbd4d9e057cb.ogg")
            "我把手机放回柜台，没发那条消息。"
            voice ("audio/voice/narr_shenlan_52251f48c6548931f67f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_52251f48c6548931f67f.ogg")
            "第二天下午，他还是照常来点了杯美式。"
            voice ("audio/voice/narr_shenlan_f8bb0bc2c274524b3144.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f8bb0bc2c274524b3144.ogg")
            "电脑刚开，他又把它合上了。"
            voice "audio/voice/story_mid_962.ogg"
            luyao "房东最近来过吗？"
            voice "audio/voice/story_mid_963.ogg"
            shenlan "……怎么突然问这个？"
            voice "audio/voice/story_mid_964.ogg"
            luyao "随便问问。"
            voice ("audio/voice/narr_shenlan_521a4489aa27c36363d9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_521a4489aa27c36363d9.ogg")
            "他去端那杯咖啡，搅拌棒外面的纸还没拆。"

    $ unlock_record("lease")
    scene black with warmfade
    voice ("audio/voice/narr_shenlan_d7f033e258779618266c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d7f033e258779618266c.ogg")
    "那张合同后来一直在抽屉里搁着。"
    voice ("audio/voice/narr_shenlan_51e1af471b400edb4b10.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_51e1af471b400edb4b10.ogg")
    "每次够别的东西，我都得先把它往旁边拨一拨。"
    jump scene_three_am


label scene_three_am:
    if pov == "luyao":
        jump luyao_pov_347
    scene black with warmfade
    call screen time_card("那天夜里", "记录 11 — 凌晨 3:47")

    scene cg 347 with paperdissolve
    voice ("audio/voice/narr_shenlan_b92e50a6f55c23217f2e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b92e50a6f55c23217f2e.ogg")
    "那天关门之后，我才想起来有东西落在店里。"
    voice ("audio/voice/narr_shenlan_c15ade490540d2e12997.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c15ade490540d2e12997.ogg")
    "再回来已经过了三点。"
    if m10_told:
        voice ("audio/voice/narr_shenlan_fe3790c85f149bab7ab9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fe3790c85f149bab7ab9.ogg")
        "他白天没来，倒是夜里来了。"
    voice ("audio/voice/narr_shenlan_af2cd0bf257987f2d95a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_af2cd0bf257987f2d95a.ogg")
    "我拿钥匙去开门，手刚碰到门把，门就开了。"
    voice ("audio/voice/narr_shenlan_c6acfb626431c3f4d7ee.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c6acfb626431c3f4d7ee.ogg")
    "他趴在柜台边，枕着自己的胳膊。"
    voice ("audio/voice/narr_shenlan_fb57ee220d05732c4a23.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fb57ee220d05732c4a23.ogg")
    "电脑屏幕没关，上面还开着店里的网页。"
    voice ("audio/voice/narr_shenlan_2acdfa4b201bd1bf1ca6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2acdfa4b201bd1bf1ca6.ogg")
    "我站到他身后，看见右下角写着 3:47。"

    menu:
        "看一眼屏幕上有什么":
            $ m11_looked = True
            voice ("audio/voice/narr_shenlan_f77e732b9a35537a4e5e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f77e732b9a35537a4e5e.ogg")
            "我扶着屏幕，把它往自己这边转了一点。"
            show screen doc_overlay("prop screen 347") with dissolve
            voice ("audio/voice/narr_shenlan_7b5639c7fdb4ca9a8e5e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7b5639c7fdb4ca9a8e5e.ogg")
            "原来他一直在修店里的支付后台。"
            voice ("audio/voice/narr_shenlan_3ab6ab967e672acd29b2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3ab6ab967e672acd29b2.ogg")
            "最后一条修改是 3:46，就在我过来前一分钟。"
            voice ("audio/voice/narr_shenlan_a620d3beb7821d7c7d48.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a620d3beb7821d7c7d48.ogg")
            "旁边还开着几个文件，最上面一份是房东开的收据。"
            voice ("audio/voice/narr_shenlan_f7a0b8986426c6a160b9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f7a0b8986426c6a160b9.ogg")
            "付款人写的是陆遥。"
            hide screen doc_overlay with dissolve
            voice ("audio/voice/narr_shenlan_7898bb123d920e15f2e1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7898bb123d920e15f2e1.ogg")
            "我站了一会儿，把屏幕轻轻转了回去。"
        "把外套给他盖上":
            voice ("audio/voice/narr_shenlan_0784036206ed7396d927.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0784036206ed7396d927.ogg")
            "我脱了外套，从背后搭在他肩上。"
            voice ("audio/voice/narr_shenlan_34bcb9a618bad101079f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_34bcb9a618bad101079f.ogg")
            "他动了动胳膊，往里埋了埋脸。"

    voice ("audio/voice/narr_shenlan_ab1070f8502c47dd5955.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ab1070f8502c47dd5955.ogg")
    "他睡着的时候眉头还是皱着的。"
    voice ("audio/voice/narr_shenlan_779008531b9559b64b89.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_779008531b9559b64b89.ogg")
    "手边那杯美式早凉了，还剩一半。"

    menu:
        "叫他起来":
            $ m11_confront = True
            voice ("audio/voice/narr_shenlan_92211c7f304d3be8f1f9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_92211c7f304d3be8f1f9.ogg")
            "我隔着柜台碰了碰他的肩膀。"
            voice ("audio/voice/narr_shenlan_591c69a8911c5992408a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_591c69a8911c5992408a.ogg")
            "他一醒，下意识就伸手去合电脑。"
            voice "audio/voice/story_mid_1017.ogg"
            luyao "……你怎么在这？"
            voice "audio/voice/story_mid_1018.ogg"
            shenlan "这是我想问的。"
            voice ("audio/voice/narr_shenlan_b1a9103cf62273c4e2a5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b1a9103cf62273c4e2a5.ogg")
            "他看着已经合起来的电脑，有一会儿没说话。"
            voice ("audio/voice/narr_shenlan_2dab0915f98e8566ee3f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2dab0915f98e8566ee3f.ogg")
            "我以为他要解释，等了好一会儿也没有。"
            voice ("audio/voice/narr_shenlan_242af4cecb9be8a5b1fe.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_242af4cecb9be8a5b1fe.ogg")
            "我给他倒了杯温水，在柜台另一头坐下。"
        "让他再睡一会儿":
            voice ("audio/voice/narr_shenlan_8e1f9e7e4ea31947d3f8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e1f9e7e4ea31947d3f8.ogg")
            "我拉了张椅子过来，在旁边坐到快天亮。"
            voice ("audio/voice/narr_shenlan_dd0a064f478798996bd2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dd0a064f478798996bd2.ogg")
            "他醒来时，伸手先去够鼠标。"

    scene bg shop day with paperdissolve
    scene bg shop day with paperdissolve
    show fx lamp day
    voice ("audio/voice/narr_shenlan_24b28469676f35bb3fa9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_24b28469676f35bb3fa9.ogg")
    "天亮了，他揉了揉眼睛，说还是想喝美式。"
    if not m11_looked:
        voice "audio/voice/story_mid_1031.ogg"
        luyao "昨晚……谢谢你。"
        voice "audio/voice/story_mid_1032.ogg"
        shenlan "谢什么？"
        voice "audio/voice/story_mid_1033.ogg"
        luyao "……外套。"
    voice ("audio/voice/narr_shenlan_e9e24a978567a386b74d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e9e24a978567a386b74d.ogg")
    "他端起杯子，喝得比平时快了些。"
    voice ("audio/voice/narr_shenlan_c602be3dabeecda700a2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c602be3dabeecda700a2.ogg")
    "那台电脑后来被他收回包里，我没去问。"
    if m11_confront:
        voice ("audio/voice/narr_shenlan_0c0f1c34d26cbe101700.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0c0f1c34d26cbe101700.ogg")
        "从早上到走，他都没再把电脑拿出来。"
        voice ("audio/voice/narr_shenlan_d3fd98e33e2d1eeaf00c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d3fd98e33e2d1eeaf00c.ogg")
        "临走到了门口，他回头站了一会儿。"
        voice ("audio/voice/narr_shenlan_5a0cdaaa4497bcf96ab3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5a0cdaaa4497bcf96ab3.ogg")
        "最后还是只说了句「明天见」。"
    else:
        voice ("audio/voice/narr_shenlan_2c9f3ce7dad2306570ab.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2c9f3ce7dad2306570ab.ogg")
        "下午四点，他收好电脑就走了。"

    $ unlock_record("truth_347")
    scene black with warmfade
    voice ("audio/voice/narr_shenlan_6fae92e11d4cf35911ac.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6fae92e11d4cf35911ac.ogg")
    "我后来核对店里的账，偶尔会点开后台。"
    voice ("audio/voice/narr_shenlan_252e7b8ce9f462990eaa.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_252e7b8ce9f462990eaa.ogg")
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
    voice ("audio/voice/narr_shenlan_ba606c76bd47ac1938ed.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ba606c76bd47ac1938ed.ogg")
    "那天下午不怎么忙，小满把本子摊在柜台上。"
    voice ("audio/voice/narr_shenlan_cacffee80e19df2dfc37.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cacffee80e19df2dfc37.ogg")
    "她写两笔就要停一下，伸手拨一拨罐子里的星。"
    voice "audio/voice/story_mid_1064.ogg"
    shenlan "在写什么？"
    voice "audio/voice/story_mid_1065.ogg"
    xiaoman "秘密。"
    voice ("audio/voice/narr_shenlan_ed6e5ec10bac920b20f9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ed6e5ec10bac920b20f9.ogg")
    "她啪地合上了本子，过了会儿又把它推到我面前。"
    voice ("audio/voice/narr_shenlan_6a268337be614886a24f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6a268337be614886a24f.ogg")
    "最上面写着「今天送出去 17 颗星」。"
    voice ("audio/voice/narr_shenlan_0b02b2300b2e2d35ce47.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0b02b2300b2e2d35ce47.ogg")
    "她在底下又添了句：「第四个客人想多要一颗。给了。」"
    voice ("audio/voice/narr_shenlan_b9a357e6dd66fe7a6655.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b9a357e6dd66fe7a6655.ogg")
    "翻过去，前面小半本都是这么记的。"
    show screen doc_overlay("prop notebook page") with dissolve
    hide screen doc_overlay with dissolve

    voice ("audio/voice/narr_shenlan_10c7cd0db31adb2b5c42.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_10c7cd0db31adb2b5c42.ogg")
    "手机振了两下，小满低头去看是谁。"
    voice "audio/voice/story_mid_1076.ogg"
    xiaoman "……我妈。"
    voice ("audio/voice/narr_shenlan_ede6156475f77f945af4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ede6156475f77f945af4.ogg")
    "她把本子往我手里一塞，去了后间。"
    voice ("audio/voice/narr_shenlan_dd2b5e0fe242a71cef68.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dd2b5e0fe242a71cef68.ogg")
    "门没带上，我还能听见她说话。"

    voice "audio/voice/story_mid_1080.ogg"
    xiaoman "……嗯，在上班。"
    voice "audio/voice/story_mid_1081.ogg"
    xiaoman "不是玩，是工作。"
    voice "audio/voice/story_mid_1082.ogg"
    xiaoman "……我知道。"
    voice "audio/voice/story_mid_1083.ogg"
    xiaoman "妈，我会想的。"
    voice ("audio/voice/narr_shenlan_29753b797dd90e8a5306.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_29753b797dd90e8a5306.ogg")
    "挂了电话以后，后间又安静了好一会儿。"

    show xiaoman worried_half at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_181f31e2cb2ebbd7afc7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_181f31e2cb2ebbd7afc7.ogg")
    "她走出来的时候，眼睛有点红。"
    voice "audio/voice/story_mid_1088.ogg"
    xiaoman "我妈说，让我回老家考编。"
    voice "audio/voice/story_mid_1089.ogg"
    shenlan "……你怎么说？"
    voice "audio/voice/story_mid_1090.ogg"
    xiaoman "我说我再干一年。"
    voice ("audio/voice/narr_shenlan_52e84d5d84e4048549eb.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_52e84d5d84e4048549eb.ogg")
    "她把本子接过去，翻到没写过的那一页。"
    voice "audio/voice/story_mid_1092.ogg"
    xiaoman "老板，我是不是很没出息？"

    menu:
        "告诉她，她一直干得很好":
            $ m9_support = True
            voice "audio/voice/story_mid_1097.ogg"
            shenlan "不会。你比我认真。"
            voice ("audio/voice/narr_shenlan_bed52b2366a263e84373.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bed52b2366a263e84373.ogg")
            "她抬头看了我一眼。"
            voice "audio/voice/story_mid_1099.ogg"
            xiaoman "……真的？"
            voice "audio/voice/story_mid_1100.ogg"
            shenlan "本子都记了小半本了。"
            voice ("audio/voice/narr_shenlan_4d12f684b31615ca1007.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4d12f684b31615ca1007.ogg")
            "她笑了一下，抬手的工夫用袖口擦了擦眼睛。"
        "劝她也考虑一下回老家":
            voice "audio/voice/story_mid_1103.ogg"
            shenlan "你妈说得也有道理。"
            voice ("audio/voice/narr_shenlan_b3052da79b6264ec3479.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b3052da79b6264ec3479.ogg")
            "她垂下眼，把刚翻开的本子合上了。"
            voice "audio/voice/story_mid_1105.ogg"
            xiaoman "……嗯。"

    voice "audio/voice/story_mid_1108.ogg"
    xiaoman "老板。"
    voice "audio/voice/story_mid_1109.ogg"
    shenlan "嗯？"
    voice "audio/voice/story_mid_1110.ogg"
    xiaoman "如果有一天你不想开了，我可以当店长。"
    voice ("audio/voice/narr_shenlan_efcff30a4ba99291545a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_efcff30a4ba99291545a.ogg")
    "她把本子捏得有点紧，纸角都弯了。"
    voice ("audio/voice/narr_shenlan_ff3dbe7646521e249044.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ff3dbe7646521e249044.ogg")
    "我手里还拿着杯子。那句「好啊」到嘴边了，又没说出来。"

    menu:
        "告诉她续租可能有问题":
            $ m9_told = True
            voice "audio/voice/story_mid_1117.ogg"
            shenlan "……店可能要关了。"
            voice ("audio/voice/narr_shenlan_033f2fe5949f97b4afec.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_033f2fe5949f97b4afec.ogg")
            "她把本子放了下来。"
            voice "audio/voice/story_mid_1119.ogg"
            xiaoman "什么时候的事？"
            voice "audio/voice/story_mid_1120.ogg"
            shenlan "下个月十五号之前。"
            if m9_support:
                voice "audio/voice/xiaoman_063a03081e163a76be3d.ogg"
                xiaoman "你刚才还说我比你认真。我还以为……"
            else:
                voice ("audio/voice/narr_shenlan_5afb70e7cdc13d6ed925.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5afb70e7cdc13d6ed925.ogg")
                "她按着本子，慢慢坐了下去。我想起刚才劝她回老家那句话，这回才听出有多重。"
            voice ("audio/voice/narr_shenlan_96cdeeecc93cb9e26261.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_96cdeeecc93cb9e26261.ogg")
            "我拿起壶，才发现刚才那只杯子已经满了。"
            voice "audio/voice/xiaoman_7a12ba3b03aa1353982a.ogg"
            xiaoman "那我还能看看店里的账吗？我想知道还差多少。"
            voice ("audio/voice/narr_shenlan_e7144cf0987d591c158d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e7144cf0987d591c158d.ogg")
            "我给她腾了点地方，把账本从柜台下面拿出来。她翻开自己的本子，一项一项地对。"
        "先不告诉她":
            voice ("audio/voice/narr_shenlan_44a0f2d505e9e870aee4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_44a0f2d505e9e870aee4.ogg")
            "我想了想，还是跟她说了声「好啊」。"
            voice ("audio/voice/narr_shenlan_2369121d9529ee4fac7c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2369121d9529ee4fac7c.ogg")
            "她把本子抱起来，腾出手去收桌上的杯子。"

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    show luyao quiet_half at expr_left with dissolve
    voice ("audio/voice/narr_shenlan_200f306dd935be785a26.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_200f306dd935be785a26.ogg")
    "陆遥傍晚才来。"
    voice ("audio/voice/narr_shenlan_e88f1c55f720c780928c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e88f1c55f720c780928c.ogg")
    "小满给他送咖啡，放下杯子才问：「陆哥，听说你找到工作了？」"
    voice "audio/voice/story_mid_1136.ogg"
    luyao "……嗯。找到了。"
    voice ("audio/voice/narr_shenlan_b9fa45b54a784a0e95ac.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b9fa45b54a784a0e95ac.ogg")
    "他没抬头，拇指贴着杯把蹭来蹭去。"
    voice "audio/voice/story_mid_1138.ogg"
    xiaoman "那挺好的。"
    voice ("audio/voice/narr_shenlan_ccd0ebb885cf3783ba36.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ccd0ebb885cf3783ba36.ogg")
    "她收起托盘，回去擦柜台了。"
    voice ("audio/voice/narr_shenlan_29a4f977384433ed1c39.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_29a4f977384433ed1c39.ogg")
    "陆遥等她走远，才压着声音叫了我一声。"
    voice "audio/voice/story_mid_1141.ogg"
    luyao "房东最近来过吗？"
    voice ("audio/voice/narr_shenlan_1395e7574972e33b9f99.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1395e7574972e33b9f99.ogg")
    "我转头去看他。"
    voice "audio/voice/story_mid_1143.ogg"
    luyao "……随便问问。"

    $ unlock_record("notebook")
    scene black with warmfade
    voice ("audio/voice/narr_shenlan_a381abc87fbb37a6a472.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a381abc87fbb37a6a472.ogg")
    "那天打烊，我发现小满把本子落在柜台上了。"
    voice ("audio/voice/narr_shenlan_6a932fa542c30aad735c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6a932fa542c30aad735c.ogg")
    "封面上那颗星的最后一笔画歪了，她用蓝笔给它补了个角。"
    jump scene_lease


label luyao_pov_book:
    $ bgm("night")
    scene black with warmfade
    call screen time_card("又过了一阵子", "记录 6 — 书页边")

    scene bg shop night with paperdissolve
    show fx lamp night
    show luyao quiet_half at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_686f9b78dadaa34add82.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_686f9b78dadaa34add82.ogg")
    "她看我一直盯着电脑，就从柜台底下拿了本旧星图册给我。"
    voice ("audio/voice/narr_shenlan_07fc8e8a9b19b6564142.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_07fc8e8a9b19b6564142.ogg")
    "猎户座的图我一眼就认出来了。刚好柜台上也有三颗纸星排在一起，我就在旁边写了句："
    voice ("audio/voice/narr_shenlan_a54ef16da087487ce176.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a54ef16da087487ce176.ogg")
    "「你柜台上那三颗星，排得跟猎户座的腰带一样。」"
    voice ("audio/voice/narr_shenlan_911175c18ff8bde3035d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_911175c18ff8bde3035d.ogg")
    "第二天，我把书还她，指给她看的是那一页。"

    menu:
        "再借来看看她写了什么":
            $ m6_write = True
            voice ("audio/voice/narr_shenlan_6432947619fd814aa350.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6432947619fd814aa350.ogg")
            "隔天我又把书借过来。她在底下添了一行：「你漏数一颗。在罐子后面。」"
            voice ("audio/voice/narr_shenlan_eca0b1a2f7f2c1ba4516.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_eca0b1a2f7f2c1ba4516.ogg")
            "我把罐子往前挪了一点，后头还真有一颗。"
        "不提页边的字，照常借书":
            voice ("audio/voice/narr_shenlan_6e694dcf0140818b5443.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6e694dcf0140818b5443.ogg")
            "隔天我去借书，谁都没提那行字。"
            voice ("audio/voice/narr_shenlan_ba15e4357d1ba41dca6a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ba15e4357d1ba41dca6a.ogg")
            "不过我一进门就又数了一遍，这回数出了四颗。"

    voice ("audio/voice/narr_shenlan_4434ea6e4cd6b71dd59c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4434ea6e4cd6b71dd59c.ogg")
    "下午我把书还给她，照例指了指那一页。"
    if m6_write:
        voice ("audio/voice/narr_shenlan_00e23ce7986005805388.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_00e23ce7986005805388.ogg")
        "这回我写的是：「那第四颗算哪儿的？」"
        voice ("audio/voice/narr_shenlan_0ed28da8e21c0b0af011.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0ed28da8e21c0b0af011.ogg")
        "她忙着擦桌子，看完倒先去挪柜台上的星。"
    else:
        voice ("audio/voice/narr_shenlan_d413545c149f4ab625e4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d413545c149f4ab625e4.ogg")
        "她没回我，我又添了一句。"
        voice ("audio/voice/narr_shenlan_1f1a2a0e51062f55e14b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1f1a2a0e51062f55e14b.ogg")
        "「今天我数过了，真有四颗。」"

    voice ("audio/voice/narr_shenlan_77fd38daebe776b48b44.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_77fd38daebe776b48b44.ogg")
    "我之前翻得急，掉出来一朵干花。仔细一看，是满天星。"
    voice ("audio/voice/narr_shenlan_2447659939388eb639fc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2447659939388eb639fc.ogg")
    "怕把花瓣碰碎，我把它夹回了书里。"
    voice ("audio/voice/narr_shenlan_d838d40f08661e22f446.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d838d40f08661e22f446.ogg")
    "那一页的右下角，我还写过三个字。"
    voice ("audio/voice/narr_shenlan_1743ea9017f432cf704b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1743ea9017f432cf704b.ogg")
    "「留下来」。写完没几秒，我就拿铅笔划掉了。"

    menu:
        "让她看看夹花的那页":
            $ m6_ask = True
            voice ("audio/voice/narr_shenlan_c64ffce87d098f89c13a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c64ffce87d098f89c13a.ogg")
            "我把书翻开，给她看那朵花，她的目光却落到了右下角。"
            voice "audio/voice/story_mid_1191.ogg"
            shenlan "这行划掉的是什么？"
            show luyao awkward_half at expr_right with dissolve
            voice "audio/voice/story_mid_1193.ogg"
            luyao "……写错了。"
            voice ("audio/voice/narr_shenlan_8584ad32860750113a01.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8584ad32860750113a01.ogg")
            "我伸手去盖，动作还是慢了一点。"
            voice ("audio/voice/narr_shenlan_a9a76cff32ed60f55344.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a9a76cff32ed60f55344.ogg")
            "她没追问，我也没把手挪开。"
        "先把那页合上":
            voice ("audio/voice/narr_shenlan_3e133ab24c840d3b0926.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3e133ab24c840d3b0926.ogg")
            "我把星图册合上，照原样放回柜台。"
            voice ("audio/voice/narr_shenlan_da891611ddc8372e2131.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_da891611ddc8372e2131.ogg")
            "那几道线划得太轻。不知道她翻到那儿会不会看清。"

    voice ("audio/voice/narr_shenlan_5d13d7f1cd610b518ff2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5d13d7f1cd610b518ff2.ogg")
    "打烊后，她把书往旁边挪了挪，底下露出几张催缴的账单。"
    voice ("audio/voice/narr_shenlan_ba3bea8638f70849cc74.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ba3bea8638f70849cc74.ogg")
    "她低头去理那些纸，我就去收杯子。"

    scene bg shop day with paperdissolve
    show fx lamp day
    show xiaoman neutral_bust at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_9280e1fce3e4103e4772.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9280e1fce3e4103e4772.ogg")
    "第二天小满借了书，还回来时，最后一页多了颗角有长有短的星。"
    voice "audio/voice/story_mid_1208.ogg"
    xiaoman "老板，这书挺好看的。"
    voice ("audio/voice/narr_shenlan_b6817da2c53dbda18ff6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b6817da2c53dbda18ff6.ogg")
    "沈岚把书放回柜台底下。"
    $ unlock_record("book_margin")

    scene black with warmfade
    voice ("audio/voice/narr_shenlan_fca52b58b7fbc4243752.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fca52b58b7fbc4243752.ogg")
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
    voice ("audio/voice/narr_shenlan_929a99e070c48e23617c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_929a99e070c48e23617c.ogg")
    "傍晚我进来的时候，小满正趴在柜台上写东西。"
    voice ("audio/voice/narr_shenlan_dd5d9147ecd5a569f967.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dd5d9147ecd5a569f967.ogg")
    "她一见是我，先把本子扣上，又朝我招手，让我过去看看。"
    voice ("audio/voice/narr_shenlan_6a268337be614886a24f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6a268337be614886a24f.ogg")
    "最上面写着「今天送出去 17 颗星」。"
    voice ("audio/voice/narr_shenlan_310bc0d48b3890de81ef.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_310bc0d48b3890de81ef.ogg")
    "底下她又添了一句：「第四个客人想多要一颗。给了。」"
    voice ("audio/voice/narr_shenlan_d7a679c60f43d5f22576.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d7a679c60f43d5f22576.ogg")
    "她翻给我看的时候，我才发现都快记了半本。"
    show screen doc_overlay("prop notebook page") with dissolve
    hide screen doc_overlay with dissolve

    voice ("audio/voice/narr_shenlan_c755e15265908061a839.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c755e15265908061a839.ogg")
    "后间门没关严，我听见她妈妈说：「你不能一辈子在咖啡店。」"
    voice ("audio/voice/narr_shenlan_bc6e0c87e10e0b1699b3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bc6e0c87e10e0b1699b3.ogg")
    "小满只说了句「妈，我会想的」。"
    voice ("audio/voice/narr_shenlan_dc7d9f2d08c724912269.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dc7d9f2d08c724912269.ogg")
    "挂了电话她也没出来。过了一会儿，里头才有动静。"

    show xiaoman worried_half at expr_right with dissolve
    voice ("audio/voice/narr_shenlan_0f3f35405a507b30b544.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0f3f35405a507b30b544.ogg")
    "她出来的时候，眼睛有点红。"
    voice ("audio/voice/narr_shenlan_e93dee3e665c17255fde.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e93dee3e665c17255fde.ogg")
    "她先把沈岚手边那杯凉水换了，才给我送咖啡。"
    voice "audio/voice/story_mid_1249.ogg"
    xiaoman "陆哥，如果有一天老板不想开了，我可以当店长。"
    voice ("audio/voice/narr_shenlan_2ef79d8e8b060275a8fd.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2ef79d8e8b060275a8fd.ogg")
    "她说得很快，手却还揪着本子的一角。"

    menu:
        "说「你可以」。":
            $ m9_support = True
            voice ("audio/voice/narr_shenlan_33de130e12c9f60ddf1e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_33de130e12c9f60ddf1e.ogg")
            "我说：「我觉得你行。」她想了想，才笑出来。"
        "告诉她店可能要关。":
            $ m9_told = True
            voice ("audio/voice/narr_shenlan_1a06b230de0c7f919ed7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1a06b230de0c7f919ed7.ogg")
            "我说：「我看见一张续租单，店可能开不下去。」她半天没接话。"
            voice "audio/voice/xiaoman_e219c7ed9456431abf2f.ogg"
            xiaoman "那我去问问老板，能不能给我也看看账。水电费我手上有。"
            voice ("audio/voice/narr_shenlan_c5e0e683f3efdd90787a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c5e0e683f3efdd90787a.ogg")
            "她抱着本子去了柜台后面。沈岚听完，让了半张桌子给她。"
        "说「别把自己搭进去」。":
            voice ("audio/voice/narr_shenlan_0d279e98ca36f6119900.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0d279e98ca36f6119900.ogg")
            "她听我说完，把本子合上了：「我就是问问。」"

    voice "audio/voice/story_mid_1263.ogg"
    xiaoman "陆哥，听说你找到工作了？"
    voice "audio/voice/story_mid_1264.ogg"
    luyao "……嗯。找到了。"
    voice ("audio/voice/narr_shenlan_8a61766318068f46164a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8a61766318068f46164a.ogg")
    "我答得太快了，自己都愣了一下。"
    voice ("audio/voice/narr_shenlan_5112d42cfbdd6f8f2ba2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5112d42cfbdd6f8f2ba2.ogg")
    "录用通知还在包里，我一直没回人家。"
    show screen doc_overlay("prop offer letter") with dissolve
    voice ("audio/voice/narr_shenlan_5728ac68f57b140f4569.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5728ac68f57b140f4569.ogg")
    "上面的工资够我再付几个月房租。入职日期也快到了。"
    hide screen doc_overlay with dissolve
    voice "audio/voice/story_mid_1271.ogg"
    xiaoman "那挺好的。"
    voice ("audio/voice/narr_shenlan_b8fd8c190b3e7b57de2d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b8fd8c190b3e7b57de2d.ogg")
    "她端着空托盘回了柜台。"
    voice ("audio/voice/narr_shenlan_bf748f4bd25a5b4412e2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bf748f4bd25a5b4412e2.ogg")
    "沈岚朝我看过来，我假装忙着喝咖啡。"
    voice "audio/voice/story_mid_1275.ogg"
    luyao "房东最近来过吗？"
    voice "audio/voice/story_mid_1276.ogg"
    shenlan "……怎么突然问这个？"
    voice "audio/voice/story_mid_1277.ogg"
    luyao "随便问问。"
    voice ("audio/voice/narr_shenlan_5ee857bf093f2b1dd031.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5ee857bf093f2b1dd031.ogg")
    "我大概知道自己还能拿出多少，可差多少，总得先问到数。"

    $ unlock_record("notebook")
    scene black with warmfade
    voice ("audio/voice/narr_shenlan_1d4da64b057ea2fd6731.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1d4da64b057ea2fd6731.ogg")
    "那天走之前，我看见小满把本子落在柜台上了。"
    voice ("audio/voice/narr_shenlan_5152fa0be12fb9a68d81.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5152fa0be12fb9a68d81.ogg")
    "封面那颗星画歪了一角，她还用蓝笔描了一遍。"
    jump scene_lease


label luyao_pov_landlord:
    scene black with warmfade
    call screen time_card("还有二十天", "记录 10 — 租约")

    voice ("audio/voice/narr_shenlan_34790aa58ff7a7b43658.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_34790aa58ff7a7b43658.ogg")
    "房东在隔壁街办公，我绕过一排招牌才找到门。"
    voice ("audio/voice/narr_shenlan_14674169c7c023e8d37d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_14674169c7c023e8d37d.ogg")
    "我把裁员拿到的补偿转给他，先垫上店里欠的租金。"
    voice ("audio/voice/narr_shenlan_18666c7388c056e33d58.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_18666c7388c056e33d58.ogg")
    "显示转账成功后，我看了眼余额，只剩我自己的房租和一点生活费。"
    voice ("audio/voice/narr_shenlan_f58833966add85ef248f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f58833966add85ef248f.ogg")
    "他收了钱，抬头问：「你跟小沈是什么关系？」"
    voice ("audio/voice/narr_shenlan_2461e62c803678acd75a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2461e62c803678acd75a.ogg")
    "我说：「我在她那儿喝咖啡。」"
    voice ("audio/voice/narr_shenlan_2c7b568d6e6b0f38c755.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2c7b568d6e6b0f38c755.ogg")
    "他看了我一眼，拿了张收据给我。"
    voice "audio/voice/story_mid_1298.ogg"
    landlord "十五号之前把第一笔打过来就行。"
    voice ("audio/voice/narr_shenlan_0c792971e3cd39842dbf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0c792971e3cd39842dbf.ogg")
    "我把收据折起来。新租约的首期还没着落，我只说我会想办法。"
    voice ("audio/voice/narr_shenlan_1ccfefb341285601456d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1ccfefb341285601456d.ogg")
    "出了办公室，雨已经下起来了。"

    menu:
        "发消息告诉她":
            $ l_lease_told = True
            voice ("audio/voice/narr_shenlan_a474a4eb4bd41951eb02.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a474a4eb4bd41951eb02.ogg")
            "我站在屋檐下给她发消息：「店里之前欠的那笔房租，我先垫了。」"
            voice ("audio/voice/narr_shenlan_36885651b0aa0897d5bf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_36885651b0aa0897d5bf.ogg")
            "隔了很久，她才回：「你哪来的钱？」"
            voice ("audio/voice/narr_shenlan_9b512726f97146fb3601.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9b512726f97146fb3601.ogg")
            "我打了几个字又删掉，没回那句。"
        "先把收据收起来":
            voice ("audio/voice/narr_shenlan_d84385df1f553a4af00f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d84385df1f553a4af00f.ogg")
            "我打开她的聊天框，打了几个字。"
            voice ("audio/voice/narr_shenlan_75a3403f2c094723ccbb.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_75a3403f2c094723ccbb.ogg")
            "临走又一个个删掉了。"
            voice ("audio/voice/narr_shenlan_ff21267777fbe2f47498.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ff21267777fbe2f47498.ogg")
            "收据跟纸星一起放进钱包，那里平常不会有人翻。"

    scene bg street rain with paperdissolve
    show fx rain slow
    voice ("audio/voice/narr_shenlan_d5619458da344b9f0b52.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d5619458da344b9f0b52.ogg")
    "回去时我绕到店对面，往里看了一眼。"
    voice ("audio/voice/narr_shenlan_2f3ef8ea0cd4cfb2fc10.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2f3ef8ea0cd4cfb2fc10.ogg")
    "店招亮着，小满挂在窗边的那串灯也亮着。"
    voice ("audio/voice/narr_shenlan_fc91dca0ce72125368fa.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fc91dca0ce72125368fa.ogg")
    "包里还放着那张我摘下来的转让告示。我摸了摸拉链，没进去。"
    $ unlock_record("lease")
    scene black with warmfade
    jump scene_three_am


label luyao_pov_347:
    scene black with warmfade
    call screen time_card("那天夜里", "记录 11 — 凌晨 3:47")

    scene bg shop night with paperdissolve
    show fx lamp night
    voice ("audio/voice/narr_shenlan_2e74931cd013495069d7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2e74931cd013495069d7.ogg")
    "门响的时候，我刚把支付页面的修改提交上去。"
    voice ("audio/voice/narr_shenlan_d86979f9bffcf1a2e6e5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d86979f9bffcf1a2e6e5.ogg")
    "沈岚上次说过，她有东西会顺手塞在柜台底下。我猜这回也是回来找东西的。"
    voice ("audio/voice/narr_shenlan_88024ab562aa180c2ec8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_88024ab562aa180c2ec8.ogg")
    "我趴在柜台上没动，电脑屏幕还亮着。"
    voice ("audio/voice/narr_shenlan_3fcd5a314c4063a6c39e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3fcd5a314c4063a6c39e.ogg")
    "右下角跳到了 3:47。刚才那条修改是 3:46。"
    voice ("audio/voice/narr_shenlan_c9adf532e06ebd1bdc45.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c9adf532e06ebd1bdc45.ogg")
    "脚步声到我旁边就停了。"
    voice ("audio/voice/narr_shenlan_a1f1f56c4088f95aa614.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a1f1f56c4088f95aa614.ogg")
    "她拿了件外套，轻轻搭在我肩上。"
    voice ("audio/voice/narr_shenlan_09c19bc67eecf69a642a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_09c19bc67eecf69a642a.ogg")
    "我听见她吸了一下鼻子，紧跟着又吸了一下。"
    voice ("audio/voice/narr_shenlan_f000a1c0c69a52bdb77b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f000a1c0c69a52bdb77b.ogg")
    "我本来想告诉她，我还醒着。"
    voice ("audio/voice/narr_shenlan_82a7c6793c1912267866.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_82a7c6793c1912267866.ogg")
    "一睁眼，我就得解释为什么凌晨还留在店里。"
    if l_lease_told:
        voice ("audio/voice/narr_shenlan_a111d84985544af21a27.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a111d84985544af21a27.ogg")
        "房租的消息她已经看过了，关于我在店里过夜这件事，我还没提。"
    else:
        voice ("audio/voice/narr_shenlan_2fd7e808c057103ea202.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2fd7e808c057103ea202.ogg")
        "到这会儿，她连我垫了租金都还不知道。"

    menu:
        "睁开眼":
            $ l_awake = True
            voice ("audio/voice/narr_shenlan_c833b3bea2e0dfd25149.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c833b3bea2e0dfd25149.ogg")
            "我动了动胳膊，抬起头。"
            voice "audio/voice/story_mid_1350.ogg"
            luyao "……我没睡。"
            voice ("audio/voice/narr_shenlan_666830b01477395aa958.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_666830b01477395aa958.ogg")
            "她还抓着外套没松手。"
            voice "audio/voice/story_mid_1352.ogg"
            shenlan "你什么时候醒的？"
            voice "audio/voice/story_mid_1353.ogg"
            luyao "你进门的时候。"
            voice ("audio/voice/narr_shenlan_ced86e8c6e2dde2a0423.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ced86e8c6e2dde2a0423.ogg")
            "电脑亮光照得她眯了下眼。我这才看见她眼睛是红的。"
            voice "audio/voice/story_mid_1355.ogg"
            luyao "别哭。"
            voice ("audio/voice/narr_shenlan_9ea21a94433bf0f7b9e9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9ea21a94433bf0f7b9e9.ogg")
            "她拉开旁边那把椅子，慢慢坐了下来。"
            voice ("audio/voice/narr_shenlan_63ec64d90a4ca7bceeda.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_63ec64d90a4ca7bceeda.ogg")
            "我把电脑合上。我们就这么坐到天亮。"
        "继续装睡":
            voice ("audio/voice/narr_shenlan_0109dbd5b36b12f64940.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0109dbd5b36b12f64940.ogg")
            "我闭着眼，等她先走。"
            voice ("audio/voice/narr_shenlan_1b66470c3e4098f65cc6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1b66470c3e4098f65cc6.ogg")
            "她又站了一会儿，才拿了东西出去。"
            voice ("audio/voice/narr_shenlan_7c923104d0f4859e5d5b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7c923104d0f4859e5d5b.ogg")
            "听见门扣上，我才抬头。"
            voice ("audio/voice/narr_shenlan_b5a522fffab134329fcb.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b5a522fffab134329fcb.ogg")
            "屏幕上还是 3:47。"

    scene bg shop day with paperdissolve
    show fx lamp day
    voice ("audio/voice/narr_shenlan_a4e831f27dc63b379226.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a4e831f27dc63b379226.ogg")
    "天亮以后，她照旧给我倒了一杯美式，还问我杯子用不用先温一下。"
    voice "audio/voice/story_mid_1368.ogg"
    luyao "昨晚……谢谢你。"
    voice "audio/voice/story_mid_1369.ogg"
    shenlan "谢什么？"
    voice "audio/voice/story_mid_1370.ogg"
    luyao "……外套。"
    voice ("audio/voice/narr_shenlan_01c4b235977e4b70986c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_01c4b235977e4b70986c.ogg")
    "她低头继续擦杯子，擦完才把外套从我椅背上拿回去。"
    $ unlock_record("truth_347")
    scene black with warmfade
    jump puzzle_scene
