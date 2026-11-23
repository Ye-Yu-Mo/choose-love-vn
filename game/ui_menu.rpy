# ============================================================
# 主菜单 / 全局转场
# ============================================================

define paperdissolve = ImageDissolve("images/ui/paper_mask.png", 0.8, ramplen=64)
define warmfade = Fade(0.45, 0.15, 0.65, color="#120c07")

image ui vignette = "images/ui/vignette.png"
image ui menu left shade = "images/ui/menu_left_shade.png"

style paper_button is button:
    background Frame("images/ui/paper_tag_idle.png", 22, 18)
    hover_background Frame("images/ui/paper_tag_hover.png", 22, 18)
    padding (30, 12)
    xsize 300

style paper_button_text is button_text:
    size 22
    color "#3a2c1e"
    hover_color "#8a4a20"
    xalign 0.5
    text_align 0.5

transform menu_in:
    alpha 0.0
    linear 1.2 alpha 1.0

transform button_appear(delay=0.0):
    alpha 0.0 yoffset 8
    pause delay
    linear 0.5 alpha 1.0 yoffset 0

screen main_menu():
    tag menu
    add "bg shop night"
    add "ui menu left shade"
    add "ui vignette"

    vbox:
        xpos 86
        ypos 74
        spacing 12
        at menu_in
        text "满天星" size 88 color "#f2e5cf" outlines [(5, "#2a1908aa", 0, 0)]
        text "一杯咖啡，一件小手工，和一个抬头看星星的夜晚。" size 17 color "#d9c4a6" xmaximum 500 outlines [(2, "#24150588", 0, 0)]

    vbox:
        xpos 92
        ypos (296 if not persistent.cleared_once else 258)
        spacing (14 if not persistent.cleared_once else 10)
        if persistent.cleared_once:
            textbutton "以陆遥的视角重看" action Start("luyao_pov_start") style "paper_button" text_style "paper_button_text" at button_appear(0.02)
        textbutton "开始游戏" action Start() style "paper_button" text_style "paper_button_text" at button_appear(0.10)
        textbutton "读取游戏" action ShowMenu("load") style "paper_button" text_style "paper_button_text" at button_appear(0.20)
        textbutton "星图" action Show("star_map") style "paper_button" text_style "paper_button_text" at button_appear(0.30)
        textbutton "设置" action ShowMenu("preferences") style "paper_button" text_style "paper_button_text" at button_appear(0.40)
        textbutton "关于" action ShowMenu("about") style "paper_button" text_style "paper_button_text" at button_appear(0.50)

    textbutton "退出" action Quit(confirm=False) text_size 16 text_color "#b9a58c" text_hover_color "#f2e5cf" xpos 96 ypos 662

    text "v[config.version]" size 14 color "#8a7a66" xalign 0.98 yalign 0.97