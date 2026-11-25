# ============================================================
# 《满天星》· 第一章「葬礼」可玩样片
# 一周目：沈岚视角
# ============================================================

label start:
    $ bgm("funeral")
    scene black with warmfade
    call screen chapter_card("第一章", "葬礼", "距关店 60 天")

    scene prop model funeral with paperdissolve
    if pov == "luyao":
        "门铃响过之后，店里安静了一秒。"
        "一个女孩趴在一座微型墓地前，另一个女人站在她身后。"
        "墓碑只有拇指大，前面摆着纸星、干花、一只缝歪耳朵的兔子。"
    else:
        "那天下午，小满在店里给自己办了一场葬礼。"
        "一座微型墓地摆在桌上。墓碑只有拇指大，前面摆着纸星、干花、一只缝歪耳朵的兔子。"
        "小满趴在那儿，摆得很认真。"

    scene bg back room with paperdissolve
    show fx lamp back
    show xiaoman neutral_half at half_right with dissolve
    xiaoman "老板，你看，像不像真的？"
    shenlan "……这是给谁的？"
    xiaoman "给我自己呀。"
    xiaoman "二十二岁的我，太乖了。我想把她埋掉。"
    "她笑得很开心。"
    if pov == "luyao":
        "她笑起来的时候，眼睛是亮的。亮得有点用力。"
    else:
        "我没有笑。"
    show xiaoman worried_half at expr_right with dissolve
    if pov == "luyao":
        "她看见门口的我，愣了一下。"
        "站在旁边的女人说没事。声音很轻。"
        "然后小满低下头，把一只纸星摆正。"
    else:
        "小满看了我一眼。"
        "我说没事。"
    show xiaoman neutral_half at half_right with dissolve
    show prop transfer sign at doc_center with dissolve
    "玻璃门上贴着一张「转让」，边角已经卷起来了。"
    hide prop transfer sign with dissolve
    if pov == "luyao":
        "我站在门口，电脑包还在滴水。"
        show luyao awkward_half at expr_left with dissolve
        luyao "……这是葬礼吗？"
    else:
        "因为我也给自己定了一个日子。"
        "只是我没告诉她。"
        "我在日历上圈了一个日子。"
        "圈住的那天，我打算不在了。"

        "门铃响了。"
        show luyao awkward_half at expr_left with dissolve
        "一个背着电脑包的男生站在门口，头发上还有雨。"
        "他看了看那座小墓地，又看了看我。"
        luyao "……这是葬礼吗？"
    xiaoman "对呀，我自己的。你要不要也埋一个？"
    luyao "……我可以先要一杯美式吗？"
    shenlan "……好。"

    if pov == "luyao":
        menu:
            "老实说「路过」。":
                $ f_asked = True
                shenlan "你……怎么找到这里的？"
                luyao "……路过。"
                "她看了我一眼。那个眼神告诉我，她不信。"
            "什么也不说。":
                "她没有问。"
                "我也没有说。"
    else:
        menu:
            "问他为什么来":
                $ f_asked = True
                shenlan "你……怎么找到这里的？"
                luyao "……路过。"
                "他说谎的样子很笨。"
            "什么也不问":
                "我没有问。"
                "他也没有说。"

    if pov == "luyao":
        "那天我坐在窗边，坐到打烊。"
        "咖啡凉了，我也没有再点。"
        if l_prologue == "wait":
            "进门之前，我在雨里站的那一会儿，好像把什么留在了门外。"
    else:
        "那天他坐在窗边，坐到打烊。"
    "后来的事，都从那天开始。"
    $ unlock_record("funeral")

    scene black with warmfade
    jump story_days_early


label piano_scene:
    stop music fadeout 2.0
    scene black with warmfade
    call screen chapter_card("第二章", "满天星", "距关店 45 天")

    scene bg piano corner with paperdissolve
    "打烊前，老周来调琴。"
    "他把音叉放在琴盖上，听了很久。"
    zhou "琴不用调得太准，人也是。"
    "他收好工具，走了。"
    "门上原来挂牌子的地方，留着一块浅色的印子。"
    show mem cat at cat_sit with dissolve
    "年糕跳上琴凳，趴下来。"
    "打烊以后，店里只剩钢琴上的那盏灯。"

    scene cg piano lesson with paperdissolve
    "她在琴前坐下，手指落在键上。"
    play music "audio/piano_touch_the_starlight.ogg" fadein 1.0
    "是那首她自己写的曲子。"

    shenlan "你想学吗？"
    luyao "我五音不全。"
    shenlan "没关系，我也不是教音乐的。"
    if pov == "luyao":
        "她把我的手放在琴键上。"
    else:
        "她把他的手放在琴键上。"

    menu:
        "认真教他":
            $ f_piano = "teach"
            shenlan "手腕放松一点。"
            if pov == "luyao":
                "我照做，还是弹错。"
            else:
                "他照做，还是弹错。"
        "逗他":
            $ f_piano = "tease"
            shenlan "陆同学，你这是在敲代码吗？"
            luyao "……差不多。"
            if pov == "luyao":
                "她笑，我也笑。"
            else:
                "她笑，他也笑。"
        "让他自己试":
            $ f_piano = "try"
            "她没有说话，退后半步。"
            if pov == "luyao":
                "我试了几次，终于按对。"
            else:
                "他试了几次，终于按对。"
            shenlan "你看，你可以的。"

    if pov == "luyao":
        "我按了四个音，错了两个。最后一个音，我是故意的。"
        "她没有纠正，只是把手覆在我手上。"
        "我想让她再教一次。"
    else:
        "他按了四个音，错了两个。她没有纠正，只是把手覆在他手上。"
    luyao "……这样？"
    shenlan "嗯。"
    if pov == "luyao":
        "我闻到她袖口的咖啡味。窗外还在下雨。"
        "那天我学会了一句旋律。她没有告诉我名字。后来我才知道，那是她自己写的，叫《满天星》。"
    else:
        "他闻到她袖口的咖啡味。窗外还在下雨。"
        "那天他学会了一句旋律。后来他才知道，那是她自己写的，叫《满天星》。"
    $ unlock_record("piano")

    stop music fadeout 2.0
    scene black with warmfade
    centered "{size=40}{color=#e8c7a8}满天星{/color}{/size}"
    jump story_days_middle
