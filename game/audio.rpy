# ============================================================
# BGM 管理
# 5 首曲子共用 music 通道；女主弹琴的曲子也走 music，
# 进入教琴场景前会先停掉 BGM。
# ============================================================

init python:
    BGM = {
        "funeral": "audio/bgm/qingyi_piano.ogg",    # 青衣：模型葬礼 / 告别
        "rain": "audio/bgm/rain_air.ogg",           # 雨に濡れた空気：雨天日常 / 伞 / 争吵
        "night": "audio/bgm/autumn_sleep.ogg",      # 暮秋沉眠：深夜 / 3:47 / 琴盖
        "ending": "audio/bgm/sunset_galaxy.ogg",    # 落日星河不及你：一起开 / 她和他走
        "letter": "audio/bgm/love_letter.ogg",      # 恋文：真结局片尾
    }

    def bgm(name, fadein=1.8, fadeout=1.2):
        """切 BGM；同一首正在放就不重启。"""
        path = BGM[name]
        if renpy.music.get_playing("music") == path:
            return
        renpy.music.play(path, channel="music", loop=True, fadein=fadein, fadeout=fadeout)