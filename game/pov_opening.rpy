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

    voice ("audio/voice/narr_shenlan_90223f9a4250059c0cc7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_90223f9a4250059c0cc7.ogg")
    "上午十点，我收到一封邮件。"
    show screen doc_overlay("prop layoff mail") with dissolve
    voice ("audio/voice/narr_shenlan_ed58803c6e07ab237473.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ed58803c6e07ab237473.ogg")
    "邮件标题写着「调整」。"
    voice ("audio/voice/narr_shenlan_74bd4a2f5eb0303616b5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_74bd4a2f5eb0303616b5.ogg")
    "我点开附件，第一个名字就是我的。"
    hide screen doc_overlay with dissolve
    voice ("audio/voice/narr_shenlan_b40e642da21ae3d6dbf4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b40e642da21ae3d6dbf4.ogg")
    "收拾工位的时候，我才发现东西也不多。键盘、杯子，再加一盆早就死了的绿萝，一个纸箱就装完了。"
    voice ("audio/voice/narr_shenlan_8f2ec64de0d1e1ba05f3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8f2ec64de0d1e1ba05f3.ogg")
    "人事说，补偿按 N+1 算，直接打到卡上。"
    voice ("audio/voice/narr_shenlan_6e53d3239ea8b63b5523.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6e53d3239ea8b63b5523.ogg")
    "我说了声好，问她纸箱能不能带走。"
    voice ("audio/voice/narr_shenlan_c264ff3d01816679cae8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c264ff3d01816679cae8.ogg")
    "出了写字楼才发现外面在下雨。"
    voice ("audio/voice/narr_shenlan_caeec8b916f4820856de.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_caeec8b916f4820856de.ogg")
    "平时下雨我会在楼下打车。"
    voice ("audio/voice/narr_shenlan_a2ade9521febebe74f4d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a2ade9521febebe74f4d.ogg")
    "那天我站在屋檐下，点开地址栏，一时没想好要去哪儿。"

    scene bg street rain with paperdissolve
    show fx rain slow
    voice ("audio/voice/narr_shenlan_c152031011f3dd51f16b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c152031011f3dd51f16b.ogg")
    "我沿着街一直走。"
    voice ("audio/voice/narr_shenlan_bb8a25e7fb896f0574b2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bb8a25e7fb896f0574b2.ogg")
    "等肩带勒得疼了，我才想起来换一边背。"
    voice ("audio/voice/narr_shenlan_381bf5446f0ea82ae472.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_381bf5446f0ea82ae472.ogg")
    "雨小了一阵，我闻到一股咖啡味。"
    voice ("audio/voice/narr_shenlan_498a993a336195878492.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_498a993a336195878492.ogg")
    "前面有家小店，玻璃门上贴着张卷了角的纸。"
    voice ("audio/voice/narr_shenlan_3ef77fb1e92f9b974b27.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3ef77fb1e92f9b974b27.ogg")
    "我往里看了眼，有人趴在桌上摆一座小得出奇的墓碑。"

    menu:
        "推门进去":
            $ l_prologue = "in"
            voice ("audio/voice/narr_shenlan_7972bd8ec422d8a53faf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7972bd8ec422d8a53faf.ogg")
            "我抬手去推门。"
        "在门外再站一会儿":
            $ l_prologue = "wait"
            voice ("audio/voice/narr_shenlan_774582b68af951178b7a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_774582b68af951178b7a.ogg")
            "我往屋檐底下站了站。"
            voice ("audio/voice/narr_shenlan_ddd564e093e00f443b04.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ddd564e093e00f443b04.ogg")
            "桌边的女孩抬起头，正好看见我。"
            voice ("audio/voice/narr_shenlan_26ee803eb41dbd2d4c1f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_26ee803eb41dbd2d4c1f.ogg")
            "我这才去推门。"

    jump start
