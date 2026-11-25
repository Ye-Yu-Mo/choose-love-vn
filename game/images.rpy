# 图片资源定义
# 文件名里有空格，用显式定义避免歧义

# 《满天星》场景
image bg shop day = ConditionSwitch(
    "sign_removed", "images/bg shop day no sign.png",
    "True", "images/bg shop day.png")
image bg shop night = ConditionSwitch(
    "sign_removed", "images/bg shop night no sign.png",
    "True", "images/bg shop night.png")
image bg back room = "images/bg back room.png"
image bg piano corner = "images/bg piano corner.png"
image bg street rain = "images/bg street rain.png"
image prop model funeral = "images/prop model funeral.png"
image cg 347 = "images/cg/cg_347.png"
image cg base inside = "images/cg/cg_base_inside.png"
image cg coffee star = "images/cg/cg_coffee_star.png"

# 结局 CG
image cg ending together = "images/cg/ending_together.png"
image cg ending xiaoman = "images/cg/ending_xiaoman.png"
image cg ending depart = "images/cg/ending_with_him.png"
image cg ending alone = "images/cg/ending_alone.png"
image cg ending funeral = "images/cg/ending_funeral.png"
image cg ending told = "images/cg/cg_ending_told.png"
image cg exhibition = "images/cg/cg_exhibition.png"


# 文档 / 屏幕特写（程序化生成，中文清晰）
image prop layoff mail = "images/props/layoff_mail.png"
image prop lease doc = "images/props/lease_doc.png"
image prop offer letter = "images/props/offer_letter.png"
image prop letter xiaoman = "images/props/letter_xiaoman.png"
image prop letter luyao = "images/props/letter_luyao.png"
image prop screen 347 = "images/props/screen_347.png"
image prop notebook page = "images/props/notebook_page.png"
image prop menu board = "images/props/menu_board.png"
image prop transfer sign = "images/props/transfer_sign.png"


screen doc_overlay(img):
    zorder -1
    add Solid("#00000055")
    add img xalign 0.5 yalign 0.04 zoom 0.64
