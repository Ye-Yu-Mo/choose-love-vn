# ============================================================
# 《满天星》· 第一章「葬礼」可玩样片
# 一周目：沈岚视角
# ============================================================

label start:
    if pov == "shenlan":
        $ persistent.star_view = "her"
    $ bgm("funeral")
    scene black with warmfade
    call screen chapter_card("第一章", "葬礼", "距关店 60 天")

    scene prop model funeral with paperdissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_d5a4f7bf03e7ca28ff22.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d5a4f7bf03e7ca28ff22.ogg")
        "门铃一响，桌边的女孩抬头看了我一眼。我进门时，她正在说想把二十二岁那个太乖的自己埋了。"
        voice ("audio/voice/narr_shenlan_25accf573f33db81acd0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_25accf573f33db81acd0.ogg")
        "我想起上午收拾工位的纸箱。保安问我工牌交了没有，我点了头。出了门才摸到它还在包里。"
        scene bg back room with paperdissolve
        show fx lamp back
        show xiaoman worried_half at expr_right with dissolve
        show luyao awkward_half at expr_left with dissolve
    else:
        voice ("audio/voice/narr_shenlan_be5f6cdbf3e7d19b01f7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_be5f6cdbf3e7d19b01f7.ogg")
        "那天下午，小满在店里给自己办了一场葬礼。"
        voice ("audio/voice/narr_shenlan_a133e86a227951daddf7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a133e86a227951daddf7.ogg")
        "一座手工小墓地摆在桌子上。墓碑虽然只有拇指大，但前面摆着星星、花朵、还有一只小兔子。"
        voice ("audio/voice/narr_shenlan_e71a6d097a416e3ec30a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e71a6d097a416e3ec30a.ogg")
        "小满趴在桌边，光是那只兔子就摆了好几回。"

        scene bg back room with paperdissolve
        show fx lamp back
        show xiaoman neutral_bust at expr_right with dissolve
        voice "audio/voice/script_26.ogg"
        xiaoman "老板，你看，像不像真的？"
        voice "audio/voice/script_27.ogg"
        shenlan "……这是给谁的？"
        voice "audio/voice/script_28.ogg"
        xiaoman "给我自己呀。"
        voice "audio/voice/script_29.ogg"
        xiaoman "二十二岁的我，太乖了。我想把她埋掉。"
        voice ("audio/voice/narr_shenlan_78fe57b19b2291022af2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_78fe57b19b2291022af2.ogg")
        "她说着笑了一声。"
        voice ("audio/voice/narr_shenlan_dab2f806adbe401a5bc9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dab2f806adbe401a5bc9.ogg")
        "我没有笑。"
        show xiaoman worried_half at expr_right with dissolve
        voice ("audio/voice/narr_shenlan_603a53c614b6208517e1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_603a53c614b6208517e1.ogg")
        "小满抬头看我，笑声一下就没了。"
        voice ("audio/voice/narr_shenlan_53ddaa95306441d339d3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_53ddaa95306441d339d3.ogg")
        "我说没事。"
        show xiaoman neutral_bust at expr_right with dissolve
        show screen doc_overlay("prop transfer sign") with dissolve
        voice ("audio/voice/narr_shenlan_a3a549ed38e324bdcc5d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a3a549ed38e324bdcc5d.ogg")
        "玻璃门上贴着张转让告示，纸角已经卷起来了。"
        hide screen doc_overlay with dissolve
        voice ("audio/voice/narr_shenlan_f5ac60f7ce19a2cbc687.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f5ac60f7ce19a2cbc687.ogg")
        "我在日历上圈了个日子。"
        voice ("audio/voice/narr_shenlan_01e488886ee1a67336fd.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_01e488886ee1a67336fd.ogg")
        "我打算活到那一天为止。这件事，我一直没告诉她。"

        voice ("audio/voice/narr_shenlan_8e93748970547c9da6f1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e93748970547c9da6f1.ogg")
        "门铃响了。"
        show luyao awkward_half at expr_left with dissolve
        voice ("audio/voice/narr_shenlan_99040ddf82871f24c71f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_99040ddf82871f24c71f.ogg")
        "一个背电脑包的男生站在门口，头发还湿着。"
        voice ("audio/voice/narr_shenlan_3c56d6520061860dc723.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3c56d6520061860dc723.ogg")
        "他看了看那座小墓地，又看了看我。"
        voice "audio/voice/script_61.ogg"
        luyao "……这是葬礼吗？"
        voice "audio/voice/script_62.ogg"
        xiaoman "对呀，我自己的。你要不要也埋一个？"
    voice "audio/voice/script_63.ogg"
    luyao "……我可以先要一杯美式吗？"
    voice "audio/voice/script_64.ogg"
    shenlan "……好。"

    if pov == "luyao":
        menu:
            "说自己是路过的":
                $ f_asked = True
                voice "audio/voice/script_70.ogg"
                shenlan "你……怎么找到这里的？"
                voice "audio/voice/script_71.ogg"
                luyao "……路过。"
                voice ("audio/voice/narr_shenlan_3ce2b907efcf75e409e9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3ce2b907efcf75e409e9.ogg")
                "她看了看我，又看了看玻璃门上那张告示。"
            "什么也不说":
                voice ("audio/voice/narr_shenlan_366663fbd97756c068d6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_366663fbd97756c068d6.ogg")
                "我低头去找手机，等她把咖啡端过来。"
    else:
        menu:
            "问他怎么找到这里的":
                $ f_asked = True
                voice "audio/voice/script_80.ogg"
                shenlan "你……怎么找到这里的？"
                voice "audio/voice/script_81.ogg"
                luyao "……路过。"
                voice ("audio/voice/narr_shenlan_5314e9e37aeed264bf54.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5314e9e37aeed264bf54.ogg")
                "他答得很快，眼睛却一直看着菜单。"
            "什么也不问":
                voice ("audio/voice/narr_shenlan_21c8153fc19595bffb6d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_21c8153fc19595bffb6d.ogg")
                "我转身去做咖啡。"

    if pov == "luyao":
        if l_prologue == "wait":
            voice ("audio/voice/narr_shenlan_e0cd26c5e7c8b4c007aa.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e0cd26c5e7c8b4c007aa.ogg")
            "她见我裤脚湿透了，从柜台底下拿了块布给我。我坐在窗边，等裤脚干，也等手机上再跳出一条消息。"
        else:
            voice ("audio/voice/narr_shenlan_254232fa748793047fde.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_254232fa748793047fde.ogg")
            "我坐到窗边，把公司群里艾特我的那条消息划掉了。那天没人再找我。"
    else:
        voice ("audio/voice/narr_shenlan_940e573eca35be91b963.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_940e573eca35be91b963.ogg")
        "他端着咖啡坐到打烊。我翻过门口的牌子，他才开始收电脑。"
    $ unlock_record("funeral")

    scene black with warmfade
    jump story_days_early


label piano_scene:
    stop music fadeout 2.0
    scene black with warmfade
    call screen chapter_card("第二章", "满天星", "距关店 45 天")

    if pov == "shenlan":
        scene bg piano corner with paperdissolve
        voice ("audio/voice/narr_shenlan_63b03fb2e8ba7d444926.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_63b03fb2e8ba7d444926.ogg")
        "打烊前，老周来调琴。"
        voice ("audio/voice/narr_shenlan_6ba7ccdd0eae497eac96.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6ba7ccdd0eae497eac96.ogg")
        "他敲了下音叉，等响声慢慢没了，才回头去试琴键。"
        voice "audio/voice/zhou_7612462ec272a5255ce0.ogg"
        zhou "这就够了。你弹两下，有哪个音听着别扭，再叫我来。"
        voice ("audio/voice/narr_shenlan_8f8dcd0632a264471255.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8f8dcd0632a264471255.ogg")
        "他收好工具，走了。"
        voice ("audio/voice/narr_shenlan_5c46db170a57741b9399.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5c46db170a57741b9399.ogg")
        "玻璃门上，那张转让告示的位置还留着一块胶印。"
        show mem cat at cat_sit with dissolve
        voice ("audio/voice/narr_shenlan_ea8c63cf140bebdcc436.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ea8c63cf140bebdcc436.ogg")
        "打烊后，店里只剩琴边一盏灯。年糕跳上琴凳，占了正中间的位置。"

    scene cg piano lesson with paperdissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_95fefea5a3d4ab583647.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_95fefea5a3d4ab583647.ogg")
        "她把年糕抱下去，自己往边上挪了挪，示意我也过来坐。"
    else:
        voice ("audio/voice/narr_shenlan_5a802a535561ad0a9718.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5a802a535561ad0a9718.ogg")
        "我把年糕抱下去，往边上挪了挪，让他也过来坐。"
    play music "audio/piano_touch_the_starlight.ogg" fadein 1.0
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_c9d39ebba418be7ff3b6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c9d39ebba418be7ff3b6.ogg")
        "她弹了一小段，问我要不要学。我本来只打算进来拿落下的充电器，听完又把包放回了地上。"
    else:
        voice ("audio/voice/narr_shenlan_224f089575dc2a41329e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_224f089575dc2a41329e.ogg")
        "我弹的是自己写的那首，以前只在没人的时候弹。"
        voice "audio/voice/script_127.ogg"
        shenlan "你想学吗？"
        voice "audio/voice/script_128.ogg"
        luyao "我五音不全。"
        voice "audio/voice/script_129.ogg"
        shenlan "没关系，我也不是教音乐的。"
        voice ("audio/voice/narr_shenlan_e744a5e3b8028a1ecbe0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e744a5e3b8028a1ecbe0.ogg")
        "我拉过他的手，先指给他看拇指该放哪儿。"

    if pov == "luyao":
        menu:
            "跟着她弹":
                $ f_piano = "teach"
                voice "audio/voice/script_139.ogg"
                shenlan "手腕放松一点。"
                voice ("audio/voice/narr_shenlan_7103c8c0387b08778547.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7103c8c0387b08778547.ogg")
                "我把手腕放低了点，一紧张，还是按错了键。"
            "故意乱弹两下":
                $ f_piano = "tease"
                voice "audio/voice/script_143.ogg"
                luyao "……这样？"
                voice "audio/voice/script_144.ogg"
                shenlan "你这是在敲代码吗？"
                voice ("audio/voice/narr_shenlan_54c5ac94c65a95f60dbc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_54c5ac94c65a95f60dbc.ogg")
                "她先笑出声，我才敢抬头。"
            "自己试一遍":
                $ f_piano = "try"
                voice ("audio/voice/narr_shenlan_4bebe5f794c44855f540.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4bebe5f794c44855f540.ogg")
                "她把手收了回去，在旁边等我。"
                voice ("audio/voice/narr_shenlan_9f86789cd365617e92c2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9f86789cd365617e92c2.ogg")
                "前几个音是我自己摸出来的。"
                voice "audio/voice/script_150.ogg"
                shenlan "你看，你可以的。"
    else:
        menu:
            "认真教他":
                $ f_piano = "teach"
                voice "audio/voice/script_155.ogg"
                shenlan "手腕放松一点。"
                voice ("audio/voice/narr_shenlan_72009a369ca422484a59.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_72009a369ca422484a59.ogg")
                "手腕倒是放松了，可他还是按到了隔壁那个键。"
            "逗他":
                $ f_piano = "tease"
                voice "audio/voice/script_159.ogg"
                shenlan "陆同学，你这是在敲代码吗？"
                voice "audio/voice/script_160.ogg"
                luyao "……差不多。"
                voice ("audio/voice/narr_shenlan_6478d798ed2d22aa89af.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6478d798ed2d22aa89af.ogg")
                "他当真似的点了点头，我反倒先笑了。"
            "让他自己试":
                $ f_piano = "try"
                voice ("audio/voice/narr_shenlan_d7be6dda70182919c2ef.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d7be6dda70182919c2ef.ogg")
                "我把手收回来，让他先找找前几个音。"
                voice ("audio/voice/narr_shenlan_943df7441b41f99612f9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_943df7441b41f99612f9.ogg")
                "他试了几遍，前几个音都弹对了。"
                voice "audio/voice/script_166.ogg"
                shenlan "你看，你可以的。"

    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_b293f1fe4402649b1cff.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b293f1fe4402649b1cff.ogg")
        "最后那个音我其实记得。故意按到旁边，她就把手搭过来，陪我又弹了一遍。"
        voice ("audio/voice/narr_shenlan_d1b1efb9dfbf0dab5171.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d1b1efb9dfbf0dab5171.ogg")
        "便利店发来的调班消息亮了两次。我把手机翻过去，想等她把这段弹完。"
    else:
        voice ("audio/voice/narr_shenlan_c6f4c62b50ad29b0c702.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c6f4c62b50ad29b0c702.ogg")
        "最后一个音又错了。我把手搭上去，带他弹了一遍。"
        voice "audio/voice/script_174.ogg"
        luyao "……这样？"
        voice "audio/voice/script_175.ogg"
        shenlan "嗯。"
        voice ("audio/voice/narr_shenlan_75e5caafb0758ff7018f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_75e5caafb0758ff7018f.ogg")
        "他低着头看琴键，肩膀碰到我的时候也没往旁边挪。"
        voice ("audio/voice/narr_shenlan_d27fb2b853c1470dad32.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d27fb2b853c1470dad32.ogg")
        "那天他只学会了开头那一小段。我本来想告诉他曲名，后来想想，等他学完再说吧。"
    $ unlock_record("piano")

    stop music fadeout 2.0
    scene black with warmfade
    if pov == "shenlan":
        centered "{size=40}{color=#e8c7a8}满天星{/color}{/size}"
    jump story_days_middle
