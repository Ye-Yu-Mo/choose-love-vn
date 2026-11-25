# ============================================================
# 底座解谜 · 可玩样片
# 模型特写 + 热点 + 状态机 + 三条分支
# ============================================================

default p_found_seam = False
default p_found_board = False
default p_base_open = False
default p_text = "模型已经封好了。底座比看上去厚。"
default p_clicks = 0
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
        hover_background "#ffffff18"
        action Return("drawer")

    # 土 / 草地
    button:
        xpos 450 ypos 478
        xysize (300, 105)
        background None
        hover_background "#ffffff14"
        action Return("soil")

    # 墓碑
    button:
        xpos 488 ypos 282
        xysize (212, 232)
        background None
        hover_background "#ffffff18"
        action Return("tombstone")

    # 布兔子（优先级最高）
    button:
        xpos 724 ypos 208
        xysize (236, 340)
        background None
        hover_background "#ffffff12"
        action Return("rabbit")

    # 工具盒 / 手机 / 算了
    frame:
        xpos 30 ypos 30
        background "#000000a8"
        padding (14, 8)
        textbutton "小满的工具盒" action Return("toolbox") text_size 20

    frame:
        xpos 980 ypos 30
        background "#000000a8"
        padding (14, 8)
        textbutton "手机" action Return("phone") text_size 20

    frame:
        xalign 0.98 ypos 30
        background "#000000a8"
        padding (14, 8)
        textbutton "算了，收起来" action Return("close") text_size 20

    if p_base_open:
        frame:
            xpos 30 ypos 90
            background "#000000a8"
            padding (14, 8)
            textbutton "自己掰开" action Return("alone") text_size 20

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
    call screen chapter_card("第三章", "底座", "D-10")

    $ unlock_record("model")
    if pov == "luyao":
        jump luyao_pov_model

    scene prop model funeral with paperdissolve
    "打烊以后，模型还在桌上。"
    "底座比看上去厚。小满说，里面本来不该有东西。"
    $ unlock_record("model")

label puzzle_loop:
    $ quick_menu = False
    $ p_clicks += 1
    if p_clicks == 3:
        $ p_text = "……小满说过，有些东西不是越用力越开。"

    call screen model_puzzle

    $ r = _return

    if r == "tombstone":
        if not p_found_seam:
            $ p_found_seam = True
            $ p_text = "墓碑背面有一道细缝，里面有一颗很小的螺丝。"
        else:
            $ p_text = "细缝里能看到螺丝。手边没有合适的工具。"
        jump puzzle_loop

    if r == "soil":
        if not p_found_board:
            $ p_found_board = True
            $ p_text = "土是软的。拨开一点，下面是一块薄木板。"
        else:
            $ p_text = "木板下面是一个小抽屉，卡住了。"
        jump puzzle_loop

    if r == "drawer":
        if p_found_seam and p_found_board:
            $ p_base_open = True
            $ p_text = "底座松了。抽屉卡住，需要工具——小满的工具盒，或者陆遥的螺丝刀。"
        else:
            $ p_text = "抽屉没有锁孔，像被胶粘住了。先从墓碑和土那边看看。"
        jump puzzle_loop

    if r == "rabbit":
        $ p_text = "布兔子的耳朵是缝歪的。小满说，这样才像真的。"
        jump puzzle_loop

    if r == "toolbox":
        if p_base_open:
            jump puzzle_xiaoman
        else:
            $ p_text = "小满的工具盒。她今天不在。"
            jump puzzle_loop

    if r == "phone":
        if p_base_open:
            jump puzzle_luyao
        else:
            $ p_text = "手机。可以叫他，但你还没想好。"
            jump puzzle_loop

    if r == "alone":
        jump puzzle_alone

    if r == "close":
        jump puzzle_put_away


label puzzle_xiaoman:
    $ quick_menu = True
    $ p_branch = "xiaoman"
    scene bg back room with paperdissolve
    show fx lamp back
    show xiaoman neutral_half at half_right with dissolve
    "小满来得很快。她看见桌上的模型，又看见我手里的螺丝刀。"
    xiaoman "老板，这是什么？"
    "她打开抽屉。里面是店的钥匙，和一封写给她的信。"
    show cg base inside with dissolve
    "抽屉里铺着深色绒布。钥匙和一封信并排放着。"
    hide cg base inside with dissolve
    show prop letter xiaoman at doc_center with dissolve
    "信封上写着「小满」。"
    hide prop letter xiaoman with dissolve
    $ unlock_record("keys")
    xiaoman "……给我的？"
    "我没有说话。"
    "她把信读了一遍，又读了一遍。"
    xiaoman "你早就想好了？"
    "那天晚上，她把信折好，放进口袋，什么也没再问。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_luyao:
    $ quick_menu = True
    $ p_branch = "luyao"
    scene bg back room with paperdissolve
    show fx lamp back
    show luyao guilty_half at expr_left with dissolve
    "陆遥来得很快。他看见模型，愣了一下。"
    "抽屉里是钥匙和一封信。他没有伸手。"
    show cg base inside with dissolve
    "抽屉里铺着深色绒布。钥匙和一封信并排放着。"
    hide cg base inside with dissolve
    show prop letter xiaoman at doc_center with dissolve
    "信封上写着「小满」。"
    hide prop letter xiaoman with dissolve
    $ unlock_record("keys")
    luyao "你早就想好了？"
    "我没有回答。"
    luyao "……你至少应该告诉我。"
    "他没有等到我的回答。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_alone:
    $ quick_menu = True
    $ p_branch = "alone"
    "我自己掰开了抽屉。钥匙和信都在里面。"
    show cg base inside with dissolve
    "抽屉里铺着深色绒布。钥匙和一封信并排放着。"
    hide cg base inside with dissolve
    show prop letter xiaoman at doc_center with dissolve
    "信封上写着「小满」。"
    hide prop letter xiaoman with dissolve
    $ unlock_record("keys")
    "我看了一遍，又放回去。"
    "我把模型盖好，放回柜台。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_put_away:
    $ quick_menu = True
    $ p_branch = "closed"
    "我把模型端起来，放回柜台最里面。"
    "底座还是封着的。"
    "有些东西，不知道也没关系。"
    scene black with warmfade
    "三天后。"
    jump argument_scene


label puzzle_end_sample:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}样片到此为止{/color}{/size}\n\n{size=18}下一场：第四章 — 争吵{/size}"
    return


# 二周目 · 陆遥视角的底座：他打开模型，看见她的离开计划
label luyao_pov_model:
    $ quick_menu = True
    scene black with warmfade

    scene bg back room with paperdissolve
    show fx lamp back
    "我回店里拿充电器。"
    "模型还在桌上。底座比看上去厚。"
    "我拨开土，摸到一块薄木板。"
    "抽屉里是店的钥匙，和一封写给小满的信。"
    show cg base inside with dissolve
    "抽屉里铺着深色绒布。钥匙和一封信并排放着。"
    hide cg base inside with dissolve
    show prop letter xiaoman at doc_center with dissolve
    "信封上写着「小满」。"
    "信上写着：如果我不在了，店交给你。"
    hide prop letter xiaoman with dissolve
    "我把信读了两遍。"
    "她不是随便说说。她真的要走。"
    "我把信放回去，把抽屉推回去。"
    "手一直在抖。"
    $ unlock_record("keys")
    $ p_branch = "luyao_seen"
    scene black with warmfade
    "三天后。"
    jump argument_scene
