# 动态氛围层：窗外雨丝、缓慢雾气、灯光呼吸
# 全部叠加在背景之上，不改变场景本身

image fx rain full = "images/fx rain full.png"
image fx window mask = "images/fx window mask.png"
image fx window mask ai = "images/fx window mask ai.png"

# 纵向无缝滚动的雨（两张上下拼接）
image fx rain scroll:
    contains:
        "fx rain full"
        yoffset 0
        linear 1.6 yoffset 720
        repeat
    contains:
        "fx rain full"
        yoffset -720
        linear 1.6 yoffset 0
        repeat

# 用遮罩裁切：雨只落在玻璃区域
image fx rain window = AlphaMask("fx rain scroll", "fx window mask")
image fx rain window ai = AlphaMask("fx rain scroll", "fx window mask ai")

image fx fog = "images/fx fog.png"
image fx glow = "images/fx glow.png"

# 叠加雨层降一点透明度，避免盖过画面里已经画好的雨
transform rain_soft:
    alpha 0.45

transform glow_pulse:
    alpha 0.16
    linear 3.0 alpha 0.32
    linear 4.0 alpha 0.16
    repeat

transform fog_drift_a:
    xoffset 0
    linear 80.0 xoffset 1280
    repeat

transform fog_drift_b:
    xoffset -1280
    linear 80.0 xoffset 0
    repeat

screen weather_fx(ai=True):
    zorder -5
    add "fx fog" at fog_drift_a
    add "fx fog" at fog_drift_b
    if ai:
        add "fx rain window ai" at rain_soft
    else:
        add "fx rain window"
    add "fx glow" at glow_pulse
