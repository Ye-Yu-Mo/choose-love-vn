# ============================================================
# 章节卡 / 时间卡
# 奶油纸片 + 一颗星 + 章节标题与日期
# ============================================================

image ui paper card = "images/ui/paper_card.png"
image ui paper card small = "images/ui/paper_card_small.png"

screen chapter_card(num, title, date=""):
    modal True
    zorder 150

    add Solid("#0b0f18")
    add "bg starry sky"
    add Solid("#0b0f18dd")

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (900, 560)
        add "ui paper card"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14
            text "满天星" size 14 color "#8a7a66" xalign 0.5
            add "star lit" zoom 0.20 xalign 0.5
            text num size 16 color "#8a7a66" xalign 0.5
            text title size 46 color "#3a2c1e" xalign 0.5
            if date:
                text date size 16 color "#8a7a66" xalign 0.5

    button:
        xysize (1280, 720)
        background None
        action Return()

    text "点击继续" size 13 color "#8a7f74" xalign 0.5 ypos 682


screen time_card(label_text):
    modal True
    zorder 150

    add Solid("#0b0f18")
    add "bg starry sky"
    add Solid("#0b0f18dd")

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (560, 330)
        add "ui paper card small"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 12
            add "star lit" zoom 0.16 xalign 0.5
            text label_text size 32 color "#3a2c1e" xalign 0.5

    button:
        xysize (1280, 720)
        background None
        action Return()

    text "点击继续" size 13 color "#8a7f74" xalign 0.5 ypos 682
