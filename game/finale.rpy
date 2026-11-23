# ============================================================
# 第五章 — 琴盖合上
# 最后的岔路：一起开 / 交给她 / 跟他走 / 一个人 / 完成葬礼
# 每个结局都有自己的场景与画面
# ============================================================

default f_told = ""
default f_ending = ""

transform end_title_in:
    alpha 0.0
    linear 1.0 alpha 1.0

screen ending_title(title, line, no):
    modal True
    add Solid("#00000055")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16
        at end_title_in
        text "结局 [no]" size 16 color "#e8c7a8" xalign 0.5 outlines [(2, "#00000066", 0, 0)]
        text title size 56 color "#f2ede4" xalign 0.5 outlines [(3, "#00000088", 0, 0)]
        text line size 22 color "#d8cfc2" xalign 0.5 xmaximum 900 text_align 0.5 outlines [(2, "#00000066", 0, 0)]
        null height 28
        textbutton "回到标题" action Return() text_size 18 xalign 0.5 text_color "#e8c7a8" text_hover_color "#ffffff"


label finale_scene:
    $ quick_menu = False
    $ bgm("night")
    scene black with warmfade
    call screen chapter_card("第五章", "琴盖合上", "D-1")

    scene bg shop night with paperdissolve
    show fx lamp shop
    show xiaoman worried_half at expr_right with dissolve
    $ unlock_record("finale")
    "最后一天，店里没有客人。"
    "小满把同一只杯子擦了三遍。"
    "钢琴盖合着。她已经很久没有弹了。"
    xiaoman "老板。"
    shenlan "嗯。"
    xiaoman "你最近……是不是在交代什么？"
    "我张了张嘴。"
    "窗外的雨停了。"

    menu:
        "告诉她实话。":
            $ f_told = "truth"
            shenlan "……我本来打算走。"
            show xiaoman crying_half at expr_right with dissolve
            xiaoman "走多久？"
            shenlan "不知道。"
            "她哭的时候没有声音，只是眼泪一直掉。"
            xiaoman "你连我都不要了。"
        "说“没有”。":
            $ f_told = "lie"
            shenlan "没有。"
            "她看了我很久。"
            xiaoman "你骗人。"
            show xiaoman pout_half at expr_right with dissolve
            "她把杯子放下，转身进了后间。"
        "反问她：如果我不在了，你会怎么办？":
            $ f_told = "ask"
            shenlan "如果我不在了，你会怎么办？"
            show xiaoman crying_half at expr_right with dissolve
            xiaoman "……那我就一个人开。"
            "她说完，自己先哭了。"
            xiaoman "所以你是在问我，还是在通知我？"
            "我没有回答。"

    "门铃响了。"
    show luyao sad_half at expr_left with dissolve
    "陆遥站在门口，手里拿着那封信。"
    luyao "信我看了。"
    "他没有问是不是写给他的。"
    luyao "所以，你打算什么时候走？"
    "他问得很轻，像怕把什么碰碎。"
    "模型还在柜台上。底座是空的。"
    if a_broke:
        "那天之后，他一直没有再来。今天是他第一次回来。"
    if m2_star:
        "我想起他第一次来的时候，碟子边那颗写着「撑住」的星。"
    if m3_fix:
        "我想起他蹲在柜台下面修刷卡机，第一次抬头看我笑。"
    if m6_write:
        "我想起书页边那些字。"
    if m8_invite:
        "我想起楼下那晚，他说「下次吧」。"
    if m7_phone:
        "我想起那晚他在雨里接的电话。"

label finale_choice:
    menu:
        "留下来，一起把店开下去。":
            jump ending_together
        "把钥匙交给小满。":
            jump ending_xiaoman
        "跟他走。":
            jump ending_with_him
        "一个人走。":
            jump ending_alone
        "完成那场葬礼。":
            jump ending_funeral_confirm


label ending_funeral_confirm:
    "你真的要这么做吗？"
    menu:
        "是。":
            jump ending_funeral
        "再想想。":
            jump finale_choice


# ---------------- 结局 ----------------

label ending_together:
    $ f_ending = "一起开"
    $ bgm("ending")
    $ unlock_record("end_together")
    scene cg ending together with paperdissolve
    "第二天，我照常开门。"
    "阳光从玻璃门照进来，落在柜台的木纹上。"
    "小满在柜台后面喊我，说有人点了一杯最贵的。"
    "陆遥坐在窗边，面前摊着一份新的招聘启事。"
    "他把 offer 折好，放进包里。"
    luyao "这次，我先问你。"
    shenlan "问什么？"
    luyao "你愿不愿意，让我留下来。"
    "我把模型底座重新封好。里面没有信了。"
    "琴盖打开着。"
    if m8_hand:
        "他先伸出手。我牵住了。"
    if m4_feed:
        "年糕还是喜欢跳上他的膝盖。"
    "那天下午，店里放了那首《满天星》。"
    $ bgm("letter", fadein=2.5)
    call screen ending_title("一起开", "有些星星，要两个人一起抬头，才看得见。", "一")
    return


label ending_xiaoman:
    $ f_ending = "朋友一个人开"
    $ bgm("funeral")
    $ unlock_record("end_xiaoman")
    scene cg ending xiaoman with paperdissolve
    "我把钥匙放在她掌心。"
    xiaoman "老板。"
    shenlan "嗯。"
    xiaoman "店我给你留着。"
    "她没有问我去哪。"
    "她把那只缝歪耳朵的兔子摆在收银台上。"
    "我走到街口，回头看了一眼。"
    "她把门口的牌子翻到了「营业」。"
    if m9_told:
        "她早就知道我要走。所以她没有问。"
    else:
        "她一直以为，店只是暂时关门。"
    "那天的阳光很好。"
    call screen ending_title("朋友一个人开", "店还亮着。她替你留了一盏灯。", "二")
    return


label ending_with_him:
    $ f_ending = "她和他走"
    $ bgm("ending")
    $ unlock_record("end_depart")
    scene cg ending depart with paperdissolve
    "我把店交给小满，只带走一只杯子。"
    "陆遥在车站等我，背着那个旧电脑包。"
    luyao "去哪？"
    shenlan "不知道。"
    luyao "那我跟你走。"
    "这次他没有替我决定。"
    "他只是把伞往我这边偏了一点。"
    if m8_hand:
        "这一次，是我先牵住他的手。"
    "进站的时候，我忽然想起来，我还没有告诉他，我给自己定的那个日子。"
    "现在不用说了。"
    call screen ending_title("她和他走", "这一次，她不是逃跑，是出发。", "三")
    return


label ending_alone:
    $ f_ending = "没有回头"
    $ bgm("night")
    $ unlock_record("end_alone")
    scene cg ending alone with paperdissolve
    "我一个人走的。"
    "没有告诉小满日期，也没有告诉陆遥。"
    "我把信留在了模型底座里。"
    "火车开动的时候，我一次也没有回头。"
    "车窗上倒映着我的脸。我看了很久，还是没有认出她。"
    "后来听说，店一直开着。"
    if m9_told:
        "小满知道我要走。我没有回头。"
    if m6_ask:
        "他划掉的那三个字，我到最后也没有问。"
    call screen ending_title("没有回头", "她走得很干脆，像从来没有来过。", "四")
    return


label ending_funeral:
    $ f_ending = "完成葬礼"
    $ bgm("funeral")
    $ unlock_record("end_funeral")
    scene cg ending funeral with paperdissolve
    "那天之后，店里空了三天。"
    "第四天，小满把门打开了。"
    "她没有哭。她把每一张桌子都擦了一遍。"
    "陆遥站在门口，手里拿着一束满天星。"
    "他们并排站着，像来参加一场很安静的葬礼。"
    "我的模型放在柜台上。墓碑前面，多了一只缝歪耳朵的兔子。"
    "信的最后一行写着："
    "「如果你们看到这封信，说明我终于还是没能学会抬头。」"
    "可窗外的星星，其实一直亮着。"
    "只是我没有看。"
    call screen ending_title("完成葬礼", "满天星开在她的墓碑前。这一次，是别人替她抬头。", "五")
    return
