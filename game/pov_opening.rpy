# ============================================================
# 二周目 · 陆遥视角序章
# 从裁员那天上午开始，到推开咖啡店的门为止
# 只复用现有背景，不出新图
# ============================================================

label luyao_pov_start:
    $ pov = "luyao"
    $ bgm("rain")
    scene black with warmfade
    call screen time_card("那天上午")

    "上午十点，我收到一封邮件。"
    show prop layoff mail at doc_center with dissolve
    "主题只有两个字：调整。"
    "附件里是一份名单。第一行是我的名字。"
    hide prop layoff mail with dissolve
    "我把工位上的东西装进纸箱。键盘、杯子、一盆养死的绿萝。"
    "HR 说，赔偿会按 N+1 打到卡上。"
    "我说好。"
    "走出写字楼的时候，天在下雨。"
    "我没有带伞。"
    "也没有地方要去。"

    scene bg street rain with paperdissolve
    show fx rain slow
    "我在街上走了很久。"
    "电脑包越来越沉。路过一家便利店，又路过一家便利店。"
    "后来雨小了，我闻到咖啡味。"
    "那家店就在前面，门上的灯亮着。"
    "玻璃里面，有人在办葬礼。"

    menu:
        "直接推门进去。":
            $ l_prologue = "in"
            "我推开了门。门铃响了一声。"
        "在雨里再站一会儿。":
            $ l_prologue = "wait"
            "我在雨里站了一会儿。"
            "隔着玻璃，看见那个办葬礼的女孩抬起头。"
            "她也在看我。"
            "然后我推开了门。"

    jump start