# ============================================================
# 底座解谜 · 可玩样片
# 模型特写 + 热点 + 状态机 + 三条分支
# ============================================================

default p_found_seam = False
default p_found_board = False
default p_base_open = False
default p_text = "点一下模型，找找卡住抽屉的地方。"
default p_debug = False
default p_branch = ""

screen model_puzzle():
    modal True
    add "prop model funeral"

    # 底座 / 抽屉（大范围，优先级最低）
    button:
        xpos 120 ypos 575
        xysize (1040, 100)
        background None
        hover_background "#fff0cb32"
        action Return("drawer")

    # 土 / 草地
    button:
        xpos 450 ypos 478
        xysize (300, 105)
        background None
        hover_background "#fff0cb32"
        action Return("soil")

    # 墓碑
    button:
        xpos 488 ypos 282
        xysize (212, 232)
        background None
        hover_background "#fff0cb32"
        action Return("tombstone")

    # 布兔子（优先级最高）
    button:
        xpos 724 ypos 208
        xysize (236, 340)
        background None
        hover_background "#fff0cb32"
        action Return("rabbit")

    frame:
        xalign 0.98 ypos 30
        background "#000000a8"
        padding (14, 8)
        textbutton "算了，收起来" action Return("close") text_size 20

    if p_base_open:
        frame:
            xpos 30 ypos 108
            background "#000000a8"
            padding (14, 8)
            vbox:
                spacing 6
                textbutton "叫小满来" action Return("toolbox") text_size 20 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "打给陆遥" action Return("phone") text_size 20 text_color "#f2ede4" text_hover_color "#e8c7a8"
                textbutton "自己掰开" action Return("alone") text_size 20 text_color "#f2ede4" text_hover_color "#e8c7a8"

    # 文本
    frame:
        xalign 0.5
        yalign 0.96
        xmaximum 1080
        background "#000000c8"
        padding (28, 14)
        text p_text size 24 color "#f2ede4" xmaximum 1020

    # 调试：热点边框
    if p_debug:
        add Solid("#ff000040") xpos 120 ypos 575 xysize (1040, 100)
        add Solid("#00ff0040") xpos 450 ypos 478 xysize (300, 105)
        add Solid("#0080ff40") xpos 488 ypos 282 xysize (212, 232)
        add Solid("#ff00ff40") xpos 724 ypos 208 xysize (236, 340)


label puzzle_scene:
    $ quick_menu = False
    $ bgm("night")
    scene black with warmfade
    call screen chapter_card("第三章", "底座", "距关店 10 天")

    $ unlock_record("model")
    if pov == "luyao":
        jump luyao_pov_model

    scene prop model funeral with paperdissolve
    "打烊以后，桌子擦过了。小满做的那座墓地还在原处。"
    "我把模型转过来，想把藏进去的钥匙和信取出来。封底那天胶水挤多了，抽屉怎么拉都不动。"

label puzzle_loop:
    $ quick_menu = False
    call screen model_puzzle

    $ r = _return

    if r == "tombstone":
        if not p_found_seam:
            $ p_found_seam = True
            $ p_text = "墓碑后面还卡着一颗螺丝。再看看前面那层假土。"
        else:
            $ p_text = "螺丝藏得太深，指甲够不着。"
        jump puzzle_loop

    if r == "soil":
        if not p_found_board:
            $ p_found_board = True
            $ p_text = "拨开一小块假土，就能摸到抽屉的木板。"
        else:
            $ p_text = "木板边上露出抽屉的一角。"
        jump puzzle_loop

    if r == "drawer":
        if p_found_seam and p_found_board:
            $ p_base_open = True
            $ p_text = "找到抽屉的边了，干了的胶还粘着。得找人帮忙，或者自己试试。"
        else:
            $ p_text = "从这里拉不开。先看看墓碑后面和土下面。"
        jump puzzle_loop

    if r == "rabbit":
        $ p_text = "兔子坐不稳，一松手就往缝歪的那只耳朵那边倒。"
        jump puzzle_loop

    if r == "toolbox":
        jump puzzle_xiaoman

    if r == "phone":
        jump puzzle_luyao

    if r == "alone":
        jump puzzle_alone

    if r == "close":
        jump puzzle_put_away


label puzzle_xiaoman:
    $ quick_menu = True
    $ p_branch = "xiaoman"
    scene bg back room with paperdissolve
    show fx lamp back
    show xiaoman neutral_bust at expr_right with dissolve
    "我给小满发了条消息。她还没走远，回来时围裙都没解。"
    voice "audio/voice/puzzle_173.ogg"
    xiaoman "老板，这是什么？"
    "她从盒子里挑了把趁手的小螺丝刀。再一拉，抽屉就滑了出来。"
    show cg base inside with dissolve
    "底下铺了层绒布。店门钥匙搁在信封旁边。"
    hide cg base inside with dissolve
    show screen doc_overlay("prop letter xiaoman") with dissolve
    "信封上写的是小满的名字。"
    hide screen doc_overlay with dissolve
    $ unlock_record("keys")
    voice "audio/voice/puzzle_182.ogg"
    xiaoman "……给我的？"
    "我把抽屉再往她跟前推了推。"
    "她先扫了一眼，紧接着从头又读了一遍。"
    voice "audio/voice/puzzle_185.ogg"
    xiaoman "你早就想好了？"
    "小满把信折回去，放进围裙口袋里。她走的时候，连工具盒都忘了带。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_luyao:
    $ quick_menu = True
    $ p_branch = "luyao"
    scene bg back room with paperdissolve
    show fx lamp back
    show luyao guilty_half at expr_left with dissolve
    "我给陆遥打了个电话。他来时只带了那把常用的螺丝刀。"
    "他帮我把卡住的一角拨开，我伸手拉开抽屉。"
    show cg base inside with dissolve
    "绒布上放着店门的备用钥匙，还有一封信。"
    hide cg base inside with dissolve
    show screen doc_overlay("prop letter xiaoman") with dissolve
    "上面写的是「小满」。我拆开信递给陆遥，他一眼就认出了我的字。"
    hide screen doc_overlay with dissolve
    $ unlock_record("keys")
    voice "audio/voice/puzzle_207.ogg"
    luyao "你早就想好了？"
    "我把手里的钥匙攥得太紧，齿都硌到掌心了。"
    voice "audio/voice/puzzle_209.ogg"
    luyao "……你至少应该告诉我。"
    "他把信折好放回去。我送他到门口，还是没能把那句话说出来。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_alone:
    $ quick_menu = True
    $ p_branch = "alone"
    "我扶住底座，用力拉了一下，抽屉总算出来了。"
    show cg base inside with dissolve
    "钥匙就在信封旁边，底下的绒布被它压出了一道印。"
    hide cg base inside with dissolve
    show screen doc_overlay("prop letter xiaoman") with dissolve
    "我写的「小满」还在信封正中间。"
    hide screen doc_overlay with dissolve
    $ unlock_record("keys")
    "我拆开看了一遍，照原来的折痕把信放了回去。"
    "抽屉推到尽头，我把模型端回柜台。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_put_away:
    $ quick_menu = True
    $ p_branch = "closed"
    "我把模型端回柜台最里面。"
    if p_base_open:
        "抽屉已经摸到拉手了。我还是把它按了回去。"
    else:
        "底座还合得紧，端起来也没听见什么响动。"
    "我让它面朝里。这样从柜台外面看过去，只能看见墓碑背面。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


# 二周目 · 陆遥视角的底座：他打开模型，看见她的离开计划
label luyao_pov_model:
    $ quick_menu = True
    scene black with warmfade

    scene bg back room with paperdissolve
    show fx lamp back
    "我回来拿充电器，插座就在放模型的那张桌子下面。"
    "拔插头时，我磕了一下桌脚。模型底下响了一声。"
    "我拨开底座边缘的假土，摸到一块松动的薄木板。"
    "木板一掀，底下露出一只小抽屉。我用包里的螺丝刀把它拨开了。"
    show cg base inside with dissolve
    "里面有把店门钥匙，旁边压着一个信封。"
    hide cg base inside with dissolve
    show screen doc_overlay("prop letter xiaoman") with dissolve
    "信封上写的是小满的名字。"
    "「如果有一天我不在了，店就交给你。」"
    hide screen doc_overlay with dissolve
    "我以为自己读岔了，拿着那张纸又从头看了一遍。"
    "我照着刚才的位置把信放回去，推上抽屉。"
    "手没使上劲，头一下没推到底。"
    $ unlock_record("keys")
    $ p_branch = "luyao_seen"
    scene black with warmfade
    "三天后。"
    jump argument_scene
