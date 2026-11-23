# ============================================================
# POV 与通关标记
# 一周目：沈岚视角；二周目：陆遥视角
# ============================================================

default persistent.cleared_once = False

default pov = "shenlan"
default l_prologue = ""

init python:

    def mark_cleared():
        """任意结局播放时写入，主菜单据此显示二周目入口。"""
        persistent.cleared_once = True
        renpy.save_persistent()