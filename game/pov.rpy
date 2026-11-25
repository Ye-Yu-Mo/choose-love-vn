# ============================================================
# POV 与通关标记
# 一周目：沈岚视角；二周目：陆遥视角
# ============================================================

default persistent.cleared_once = False
default persistent.cleared_pov = False

default pov = "shenlan"
default l_prologue = ""
default f_asked = False
default f_piano = ""
default sign_removed = False
default l_four_told = False
default l_lease_told = False
default l_awake = False
default l_truth = False

init python:

    def mark_cleared():
        """任意结局播放时写入；二周目结局额外解锁星图「他没说的」。"""
        persistent.cleared_once = True
        if getattr(renpy.store, "pov", None) == "luyao":
            persistent.cleared_pov = True
        renpy.save_persistent()