# ============================================================
# 第五章 — 琴盖合上
# 最后的岔路：一起开 / 交给她 / 跟他走 / 一个人 / 完成葬礼
# 每个结局都有自己的场景与画面
# ============================================================

default f_told = ""
default f_ending = ""

transform end_title_in:
    alpha 0.0
    linear 1.0 alpha 1.0

# 白夜：复用「一起开」CG，压低饱和度
transform cold_wash:
    matrixcolor SaturationMatrix(0.35) * BrightnessMatrix(-0.02)

screen ending_title(title, line, no):
    modal True
    add Solid("#00000055")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16
        at end_title_in
        text "结局 [no]" size 16 color "#e8c7a8" xalign 0.5 outlines [(2, "#00000066", 0, 0)]
        text title size 56 color "#f2ede4" xalign 0.5 outlines [(3, "#00000088", 0, 0)]
        text line size 22 color "#d8cfc2" xalign 0.5 xmaximum 900 text_align 0.5 outlines [(2, "#00000066", 0, 0)]
        null height 28
        textbutton "回到标题" action Return() text_size 18 xalign 0.5 text_color "#e8c7a8" text_hover_color "#ffffff"


label finale_scene:
    if pov == "luyao":
        jump luyao_pov_finale
    $ quick_menu = False
    $ bgm("night")
    scene black with warmfade
    call screen chapter_card("第五章", "琴盖合上", "原定关店前一晚")

    scene bg shop night with paperdissolve
    show fx lamp night
    show xiaoman worried_half at expr_right with dissolve
    $ unlock_record("finale")
    voice ("audio/voice/narr_shenlan_510b748b52eec3ec2b1f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_510b748b52eec3ec2b1f.ogg")
    "原定关门的前一晚，到打烊一个客人也没来。"
    voice ("audio/voice/narr_shenlan_68fee4db86b2dd273ebf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_68fee4db86b2dd273ebf.ogg")
    "小满擦着一只早就擦干净的杯子，连底下的商标都又抹了一遍。"
    voice ("audio/voice/narr_shenlan_5d4d91c5a6ddf090c399.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5d4d91c5a6ddf090c399.ogg")
    "琴盖合着。我早上还用它压了几张没收的谱子。"
    voice "audio/voice/finale_48.ogg"
    xiaoman "老板。"
    voice "audio/voice/finale_49.ogg"
    shenlan "嗯。"
    voice "audio/voice/finale_50.ogg"
    xiaoman "你最近……是不是在交代什么？"
    voice ("audio/voice/narr_shenlan_c116c9284d367f7853a3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c116c9284d367f7853a3.ogg")
    "我想说「没有」，嘴都张开了，还是没说出来。"
    voice ("audio/voice/narr_shenlan_645cb506d89139473150.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_645cb506d89139473150.ogg")
    "外头雨已经停了，小满还在等我开口。"

    menu:
        "告诉她我圈了一个日子":
            $ f_told = "truth"
            voice "audio/voice/finale_57.ogg"
            shenlan "……我给自己定了个日子。"
            show xiaoman crying_half at expr_right with dissolve
            voice "audio/voice/finale_59.ogg"
            xiaoman "什么日子？"
            voice "audio/voice/shenlan_da203005ed46d3ddcf23.ogg"
            shenlan "那天以后，我就不想再活了。"
            voice ("audio/voice/narr_shenlan_cd9f2601b7663e0eaa54.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cd9f2601b7663e0eaa54.ogg")
            "小满还捏着擦杯布。眼泪掉下去，她也没腾手去擦。"
            voice "audio/voice/xiaoman_dc36dfc5acef50081703.ogg"
            xiaoman "这么大的事，你怎么连我都不告诉？"
        "说「没有」":
            $ f_told = "lie"
            voice "audio/voice/finale_65.ogg"
            shenlan "没有。"
            voice ("audio/voice/narr_shenlan_e274f4c269919e1d9d9f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e274f4c269919e1d9d9f.ogg")
            "她停下来，看着我。"
            voice "audio/voice/finale_67.ogg"
            xiaoman "你骗人。"
            show xiaoman pout_half at expr_right with dissolve
            voice ("audio/voice/narr_shenlan_c185f9f42b9d5722f384.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c185f9f42b9d5722f384.ogg")
            "她把杯子往架子上一放，转身去了后间。"
        "问她我走了以后，她会怎么办":
            $ f_told = "ask"
            voice "audio/voice/finale_72.ogg"
            shenlan "如果我不在了，你会怎么办？"
            show xiaoman crying_half at expr_right with dissolve
            voice "audio/voice/finale_74.ogg"
            xiaoman "……那我就一个人开。"
            voice ("audio/voice/narr_shenlan_06b70ff81f9ed8f74bae.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_06b70ff81f9ed8f74bae.ogg")
            "她一开口就带了哭腔，「开」字说到一半差点没说出来。"
            voice "audio/voice/finale_76.ogg"
            xiaoman "所以你是在问我，还是在通知我？"
            voice ("audio/voice/narr_shenlan_c66aea078a6359514083.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c66aea078a6359514083.ogg")
            "我找不出一句能接上的话。"

    voice ("audio/voice/narr_shenlan_42c6fdbdf3acceb5fa2b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_42c6fdbdf3acceb5fa2b.ogg")
    "我从抽屉里取出给陆遥的信，压在他平时放杯子的那个位置。"

label finale_door:
    voice ("audio/voice/narr_shenlan_8e93748970547c9da6f1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e93748970547c9da6f1.ogg")
    "门铃响了。"
    show luyao sad_half at expr_left with dissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_63daa138dc186f7e994c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_63daa138dc186f7e994c.ogg")
        "柜台上压着一封没写名字的信，摆在我平常放杯子的地方。我拆开看了。"
    else:
        voice ("audio/voice/narr_shenlan_933b42cb1af7435c0546.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_933b42cb1af7435c0546.ogg")
        "陆遥走到柜台边。我把信抽出来递给他，等他看完。"
    show screen doc_overlay("prop letter luyao") with dissolve
    voice ("audio/voice/narr_shenlan_a3973abb1da2fa198d1d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a3973abb1da2fa198d1d.ogg")
    "信很短，有一行提到了那颗写着「留下」的星。"
    hide screen doc_overlay with dissolve
    if pov == "luyao":
        voice "audio/voice/finale_89.ogg"
        luyao "信我看了。"
        if m7_star:
            voice ("audio/voice/narr_shenlan_1dedfe0d164a01be3e8a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1dedfe0d164a01be3e8a.ogg")
            "信里写了「留下」。我包上那颗星也写着这两个字。"
        else:
            voice ("audio/voice/narr_shenlan_6cf7ac5c1d6605126088.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6cf7ac5c1d6605126088.ogg")
            "信里说我总坐窗边，让我有空自己弹一遍。我就知道了。"
        voice "audio/voice/finale_91.ogg"
        luyao "所以，你打算什么时候走？"
        voice ("audio/voice/narr_shenlan_6878da1a08765a703297.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6878da1a08765a703297.ogg")
        "我尽量问得轻一点，怕后间的小满听见。"
        if p_branch == "closed":
            voice ("audio/voice/narr_shenlan_544c6365dceb73c98e83.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_544c6365dceb73c98e83.ogg")
            "模型还在柜台最里边，我看不见它的正面。"
        elif p_branch == "luyao_seen" or p_branch == "alone":
            voice ("audio/voice/narr_shenlan_864281612137b3df680a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_864281612137b3df680a.ogg")
            "我朝柜台另一头看去。前几天被我拉开过的那个抽屉，已经合得严严实实。"
        else:
            voice ("audio/voice/narr_shenlan_dae69ccd5b5ae0bd4c3a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dae69ccd5b5ae0bd4c3a.ogg")
            "模型还摆在老地方。"
        if a_broke:
            voice ("audio/voice/narr_shenlan_b7864c8e66450dbaf513.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b7864c8e66450dbaf513.ogg")
            "上回我把钥匙留在柜台就走了。今天进来，我下意识还在摸口袋。"
        if m2_star:
            voice ("audio/voice/narr_shenlan_2d0625e407c86f85a440.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2d0625e407c86f85a440.ogg")
            "我头一回在罐子里挑走的那颗星，上面的「撑住」已经快磨掉了。"
        if m3_fix:
            voice ("audio/voice/narr_shenlan_a752b304c34ae43f9f0b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a752b304c34ae43f9f0b.ogg")
            "修刷卡机那天，我还蹲在柜台底下，一抬头就看见她笑了。"
        if m6_write:
            voice ("audio/voice/narr_shenlan_c3f3ce2532575eb3ceab.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c3f3ce2532575eb3ceab.ogg")
            "柜台底下还压着那本星图册，不知道她后来有没有再翻过。"
        if m8_invite:
            voice ("audio/voice/narr_shenlan_bca669084f6bcd90c03a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bca669084f6bcd90c03a.ogg")
            "那晚我问能不能再坐一会儿，她说下次吧。"
        if m7_phone:
            voice ("audio/voice/narr_shenlan_a7d720f547f1c8645b37.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a7d720f547f1c8645b37.ogg")
            "当初我在街对面接电话，她也是这么站着等我的。"
    else:
        voice "audio/voice/finale_116.ogg"
        luyao "信我看了。"
        voice ("audio/voice/narr_shenlan_bae0fcdc11f5578f9baf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bae0fcdc11f5578f9baf.ogg")
        "他把纸展平，说完就朝我看过来。"
        voice "audio/voice/finale_118.ogg"
        luyao "所以，你打算什么时候走？"
        voice ("audio/voice/narr_shenlan_a070c66d6d4cdfaa5214.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a070c66d6d4cdfaa5214.ogg")
        "他问得很轻，后间的小满大概听不见。"
        if p_branch == "closed":
            voice ("audio/voice/narr_shenlan_69b95bc6977c43bebe25.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_69b95bc6977c43bebe25.ogg")
            "模型还在柜台最里面，只露出墓碑的背。"
        elif p_branch == "xiaoman":
            voice ("audio/voice/narr_shenlan_36ed4e83257f201bc111.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_36ed4e83257f201bc111.ogg")
            "模型的抽屉还开着，钥匙在绒布上放着。小满已经把信拿走了。"
        else:
            voice ("audio/voice/narr_shenlan_12933abfe82244484159.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_12933abfe82244484159.ogg")
            "底座合着。信和备用钥匙都收回了抽屉里。"
        if a_broke:
            voice ("audio/voice/narr_shenlan_71a4f28b12923ce8ebd8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_71a4f28b12923ce8ebd8.ogg")
            "自从把钥匙留在柜台上，他就没来过。今天他站在门口，却没往里走。"
        if m2_star:
            voice ("audio/voice/narr_shenlan_da3ceb7dd4cdede7f4a1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_da3ceb7dd4cdede7f4a1.ogg")
            "我头一回送他的那颗纸星，上面还写着「撑住」。"
        if m3_fix:
            voice ("audio/voice/narr_shenlan_2eca2a9b1a4a5bfdc959.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2eca2a9b1a4a5bfdc959.ogg")
            "第一次修刷卡机，他从那么窄的柜台底下抬起头，正好撞见我在笑。"
        if m6_write:
            voice ("audio/voice/narr_shenlan_441c8bda57fc6da10398.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_441c8bda57fc6da10398.ogg")
            "我想起他在书上划掉的几个字。铅笔印到现在还看得见。"
        if m8_invite:
            voice ("audio/voice/narr_shenlan_4d5033ad6a08e71c4b1a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4d5033ad6a08e71c4b1a.ogg")
            "那天我都走到楼梯上了，又下来问他要不要上去。他说下次吧。"
        if m7_phone:
            voice ("audio/voice/narr_shenlan_f4fc0b389ca0bfd1bc4b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f4fc0b389ca0bfd1bc4b.ogg")
            "他过马路去接电话的那晚，我也扶着这扇门等过他。"

label finale_choice:
    if pov == "luyao":
        jump finale_choice_luyao
    menu:
        "留下来，和他们一起开店":
            jump ending_together
        "问小满愿不愿意接店":
            jump ending_xiaoman
        "和陆遥一起走":
            jump ending_with_him
        "买张车票，一个人走":
            jump ending_alone
        "按照日历上圈的那天告别":
            jump ending_funeral_confirm


label ending_funeral_confirm:
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_5d389805f66a1f510731.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5d389805f66a1f510731.ogg")
        "你要让她按信里说的那样告别吗？"
        menu:
            "继续":
                jump ending_funeral_luyao
            "回去再想想":
                jump finale_choice_luyao
    voice ("audio/voice/narr_shenlan_ddb1881bf7e41361bab4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ddb1881bf7e41361bab4.ogg")
    "你确定要按照原定的计划告别吗？"
    menu:
        "继续":
            jump ending_funeral
        "回去再想想":
            jump finale_choice


# ---------------- 结局 ----------------

label ending_together:
    $ f_ending = "一起开"
    $ mark_cleared()
    $ bgm("ending")
    $ unlock_record("end_together")
    scene cg ending together with paperdissolve
    if a_broke:
        voice ("audio/voice/narr_shenlan_5a2526a833363ce08e0a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5a2526a833363ce08e0a.ogg")
        "争吵那晚他把钥匙留在桌上。今天他回来，我才把钥匙还给他。"
        voice ("audio/voice/narr_shenlan_93e1d04c154c45085edc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_93e1d04c154c45085edc.ogg")
        "他接过钥匙，在门口等我一起翻牌。"
        voice ("audio/voice/narr_shenlan_b95adb8035e02132767a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b95adb8035e02132767a.ogg")
        "第二天，我们照常开了门。"
    else:
        voice ("audio/voice/narr_shenlan_bb09e9a5d47efa5fdcee.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bb09e9a5d47efa5fdcee.ogg")
        "第二天我照常开门。陆遥在窗边坐下，小满去给他拿杯子。"
    voice ("audio/voice/narr_shenlan_d4828b9d3e864f3f6c43.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d4828b9d3e864f3f6c43.ogg")
    "我在关掉日历之前，用笔把原来圈着的那个日期涂掉了。"
    voice ("audio/voice/narr_shenlan_8e3317693bb54eba3dfa.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e3317693bb54eba3dfa.ogg")
    "早上拉开帘子，柜台上前一天没擦干的那一块还透着水印。"
    voice ("audio/voice/narr_shenlan_bcb24e40dd5b5ad2fd0c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bcb24e40dd5b5ad2fd0c.ogg")
    "小满在柜台后面喊，说窗边那位今天点了份最贵的。"
    voice ("audio/voice/narr_shenlan_6d4d46b39a035f109f1b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6d4d46b39a035f109f1b.ogg")
    "陆遥拿着咖啡，手边还放着新公司的录用通知。"
    voice ("audio/voice/narr_shenlan_2434bf6020814b44bebf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2434bf6020814b44bebf.ogg")
    "他等我走过去，把那几页纸往我这边推了推。"
    voice "audio/voice/finale_192.ogg"
    luyao "这次，我先问你。"
    voice "audio/voice/finale_193.ogg"
    shenlan "问什么？"
    voice "audio/voice/finale_194.ogg"
    luyao "你愿不愿意，让我留下来。"
    if p_branch == "xiaoman":
        voice ("audio/voice/narr_shenlan_d69b04a4c375e0c84108.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d69b04a4c375e0c84108.ogg")
        "小满已经把信收走了。我把备用钥匙放回绒布上，推好抽屉。"
    elif p_branch == "closed":
        voice ("audio/voice/narr_shenlan_52c68ff2c2b72c951085.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_52c68ff2c2b72c951085.ogg")
        "我把底座上的土抹平了。藏在里面的那封信，我没再动。"
    else:
        voice ("audio/voice/narr_shenlan_5fe6478742dcda45fe48.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5fe6478742dcda45fe48.ogg")
        "我把松了的底座重新粘好，搬回柜台角上。"
    if m10_signed:
        voice ("audio/voice/narr_shenlan_9f0244a84fb388adbee4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9f0244a84fb388adbee4.ogg")
        "签完的合同还在抽屉里。我们都看过那个数，又各自列了一张能省下的开支。"
    else:
        voice ("audio/voice/narr_shenlan_574814d6cd4176288e25.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_574814d6cd4176288e25.ogg")
        "下个月要交的钱还没定。我们约了房东过来，当面谈。"
    voice ("audio/voice/narr_shenlan_2055b01c5d6959b23584.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2055b01c5d6959b23584.ogg")
    "营业前我把琴盖掀开，随手试了两个音。"
    if m8_hand:
        voice ("audio/voice/narr_shenlan_902bb4452c59a2853161.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_902bb4452c59a2853161.ogg")
        "我刚把手从琴键上拿开，陆遥就把手递过来了。"
    if m4_feed:
        voice ("audio/voice/narr_shenlan_e50ca7be0a628f3cefdf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e50ca7be0a628f3cefdf.ogg")
        "年糕又跳到陆遥腿上。陆遥就用一只手翻他的录用通知。"
    voice ("audio/voice/narr_shenlan_13b77ad68583eb7c9dcf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_13b77ad68583eb7c9dcf.ogg")
    "下午有客人问店里在放什么，我告诉她，叫《满天星》。"
    voice ("audio/voice/narr_shenlan_0ec2ee185b8255f07816.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0ec2ee185b8255f07816.ogg")
    "又过了一个月，我们腾了半个柜台出来摆了个小展。"
    show cg exhibition with dissolve
    voice ("audio/voice/narr_shenlan_81545c988acb70a725d6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_81545c988acb70a725d6.ogg")
    "那本星图册摊开让人翻，旁边就是模型和小满攒下来的纸星。"
    hide cg exhibition with dissolve
    $ bgm("letter", fadein=2.5)
    call screen ending_title("一起开", "明天开门的时候，这回有人一起。", "一")
    return


label ending_xiaoman:
    jump xiaoman_handover


label xiaoman_handover:
    $ f_ending = "朋友一个人开"
    $ bgm("funeral")
    scene bg shop night with paperdissolve
    show fx lamp night
    show xiaoman worried_half at expr_right with dissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_b69365623e53379e676e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b69365623e53379e676e.ogg")
        "我提议把小满叫出来谈谈。沈岚朝后间喊了一声，又拉了张椅子过来。"
    else:
        voice ("audio/voice/narr_shenlan_39ad0d70c1979b5e436b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_39ad0d70c1979b5e436b.ogg")
        "我把桌上那把椅子拉开，请小满过来坐一会儿。"
    voice "audio/voice/shenlan_cdbc3ddea092f977c945.ogg"
    shenlan "我想歇一阵。店里的事，你愿意接着做吗？"
    if p_branch == "xiaoman":
        voice "audio/voice/xiaoman_46c82f7d43268eb6c112.ogg"
        xiaoman "那封信我收好了。今天你坐在这儿，我想听你当面说。"
        voice "audio/voice/shenlan_11e6c547f21a354be5de.ogg"
        shenlan "好。你也可以慢慢想。"
    if m9_told:
        voice ("audio/voice/narr_shenlan_0974c56f3f71abe759fc.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0974c56f3f71abe759fc.ogg")
        "小满起身去拿她的本子。有一页折着角，进账和开支都已经写进去了。"
        voice "audio/voice/xiaoman_10fa2f93d767d7d6d6ed.ogg"
        xiaoman "我带着这个去见过房东了。他肯谈首期怎么付。我算下来，先只开白天，能省一些。"
        voice "audio/voice/xiaoman_e5ad5c8d60e0e86db0b6.ogg"
        xiaoman "我想接。等房东把新条件写下来，我自己去谈。"
    else:
        voice ("audio/voice/narr_shenlan_1494d75e1666c9dab3f9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1494d75e1666c9dab3f9.ogg")
        "小满翻开账本。她看到续租的数，笔都搁下了。"
        voice "audio/voice/xiaoman_3b40f60843683849a303.ogg"
        xiaoman "这几天我可以先替你开门。我得看看账，也得想想自己愿不愿意做。给我一周，好吗？"
        voice "audio/voice/shenlan_c4bbaceeea4376525cf4.ogg"
        shenlan "好。我先问问房东，能不能给我们一周。"
        voice ("audio/voice/narr_shenlan_9c59aed221ea59868721.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9c59aed221ea59868721.ogg")
        "过了好一会儿，房东才回消息，说肯多留七天。小满看了一眼，把下周的排班表翻了出来。"

    voice ("audio/voice/narr_shenlan_ce47442dcb0ea9e3c156.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ce47442dcb0ea9e3c156.ogg")
    "小满合上本子，把手伸到桌子中间。"
    voice "audio/voice/xiaoman_409a73b6853b6afffc90.ogg"
    xiaoman "钥匙给我吧。明天我来开门。"
    scene cg ending xiaoman with paperdissolve
    if pov == "luyao":
        voice ("audio/voice/narr_shenlan_ab6e5f09183068973d23.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ab6e5f09183068973d23.ogg")
        "沈岚把钥匙放到她手里。后来她告诉我，日历上那个圈也划掉了。"
    else:
        voice ("audio/voice/narr_shenlan_2a97d984814e6baa4286.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2a97d984814e6baa4286.ogg")
        "我把钥匙放到她手里。回家以后，我把日历上那个圈划掉了。"

    if not m9_told:
        scene black with warmfade
        call screen time_card("一周后")
        scene bg shop day with paperdissolve
        show xiaoman neutral_bust at expr_right with dissolve
        voice ("audio/voice/narr_shenlan_6b405b476eeac5f2db76.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6b405b476eeac5f2db76.ogg")
        "小满把账本里的欠款都用蓝笔圈了出来，旁边列着下一周要付的几笔钱。"
        voice "audio/voice/xiaoman_ea395bc0021532d3873e.ogg"
        xiaoman "我想再开一个月。下个月续不续，我去跟房东谈完再定。"
        voice ("audio/voice/narr_shenlan_ec80b28b81b622e64754.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ec80b28b81b622e64754.ogg")
        "她说完，把钥匙挂到自己包上。"

    voice ("audio/voice/narr_shenlan_3e1b5f4d2e3eeb05bc1d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3e1b5f4d2e3eeb05bc1d.ogg")
    "后来小满在店里腾了半张桌子办展，把那座模型摆在正中间。"
    show cg exhibition with dissolve
    voice ("audio/voice/narr_shenlan_5e9d7d34d061ec33b976.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5e9d7d34d061ec33b976.ogg")
    "纸星罐和星图册放在旁边，谁来都能翻两页。"
    voice ("audio/voice/narr_shenlan_e81b830a7a0cdd5208c3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e81b830a7a0cdd5208c3.ogg")
    "她把布兔子挪到收银机旁边，说站柜台的人总得有个伴。"
    $ mark_cleared()
    $ unlock_record("end_xiaoman")
    call screen ending_title("朋友一个人开", "玻璃门上的牌子翻回了「营业」。", "二")
    return


label ending_with_him:
    $ f_ending = "她和他走"
    $ mark_cleared()
    $ bgm("ending")
    $ unlock_record("end_depart")
    scene cg ending depart with paperdissolve
    voice ("audio/voice/narr_shenlan_cb30b3eba1416a6902b6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cb30b3eba1416a6902b6.ogg")
    "小满答应先帮我开几天门。把钥匙给她以后，我只带走了自己常用的那只杯子。"
    voice ("audio/voice/narr_shenlan_648649e9b237aa3c327c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_648649e9b237aa3c327c.ogg")
    "陆遥在车站等着，背的还是头一天来店里那个电脑包。"
    voice "audio/voice/finale_263.ogg"
    shenlan "去哪？"
    voice "audio/voice/luyao_678daf243a1698d144d9.ogg"
    luyao "你有想去的地方吗？"
    voice "audio/voice/luyao_1cfaddf38d233b80d7ae.ogg"
    luyao "咱们去看看下一班车去哪儿吧。"
    voice "audio/voice/finale_266.ogg"
    shenlan "好。"
    voice ("audio/voice/narr_shenlan_576b0d250e3515024161.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_576b0d250e3515024161.ogg")
    "我先去看了眼车次，挑了还有两个空位的那趟。"
    voice ("audio/voice/narr_shenlan_b3de5fe0ef50bbae7135.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b3de5fe0ef50bbae7135.ogg")
    "他帮我抱着那只杯子，我把两张票都收进自己的兜里。"
    if m8_hand:
        voice ("audio/voice/narr_shenlan_ff86f6da08e845cd4a4b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ff86f6da08e845cd4a4b.ogg")
        "检票之前，我空出一只手牵住了他。"
    voice ("audio/voice/narr_shenlan_00d577db43bfe4cbe311.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_00d577db43bfe4cbe311.ogg")
    "我低头看了眼票上的日期，离日历上那个圈还有几天。"
    voice ("audio/voice/narr_shenlan_73ccee51592d8e8dd8fd.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_73ccee51592d8e8dd8fd.ogg")
    "我想先坐完这趟车，看看路上会经过些什么地方。"
    call screen ending_title("她和他走", "下一班车，两张票。", "三")
    return


label ending_alone:
    $ f_ending = "没有回头"
    $ mark_cleared()
    $ bgm("night")
    $ unlock_record("end_alone")
    scene cg ending alone with paperdissolve
    voice ("audio/voice/narr_shenlan_8bdd1489c8f442174d87.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8bdd1489c8f442174d87.ogg")
    "走之前，我找人把钥匙带给小满，托她替我看店。"
    voice ("audio/voice/narr_shenlan_c09877da14c3da10f059.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c09877da14c3da10f059.ogg")
    "原来圈的日子还没到，我就给自己买了张车票。"
    voice ("audio/voice/narr_shenlan_cfd6a1d2cc8d8dc6cab2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cfd6a1d2cc8d8dc6cab2.ogg")
    "车什么时候开，我谁也没告诉。"
    if p_branch == "xiaoman":
        voice ("audio/voice/narr_shenlan_09a7a4e0cc35cab9dcc5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_09a7a4e0cc35cab9dcc5.ogg")
        "写给小满的那封信已经在她那儿，我没再另外留字条。"
    elif p_branch == "luyao":
        voice ("audio/voice/narr_shenlan_216107ae1200bea3c0f7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_216107ae1200bea3c0f7.ogg")
        "写给小满的信还在抽屉里，陆遥没拿走。"
    elif p_branch == "closed":
        voice ("audio/voice/narr_shenlan_b81b7017a7f380f15e63.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b81b7017a7f380f15e63.ogg")
        "模型的底座没动过，信还封在里面。"
        voice ("audio/voice/narr_shenlan_d35f832d8c0028b8ff97.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d35f832d8c0028b8ff97.ogg")
        "我把它放在柜台最深的那个角上。"
    else:
        voice ("audio/voice/narr_shenlan_03039f89dac5775952b5.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_03039f89dac5775952b5.ogg")
        "我把信折回去，留在了模型里。"
    voice ("audio/voice/narr_shenlan_b39db7e2d25aa38c2fd8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b39db7e2d25aa38c2fd8.ogg")
    "车开的时候，我正忙着把票塞进外套里，再抬头车站已经过了。"
    voice ("audio/voice/narr_shenlan_09ef455d9b0d152953be.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_09ef455d9b0d152953be.ogg")
    "窗上只剩我的影子。我后来一路没再朝来时那头看。"
    voice ("audio/voice/narr_shenlan_2ef72bdb10deee8a2d8a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2ef72bdb10deee8a2d8a.ogg")
    "后来有老客给我发照片，店招还亮着。"
    voice ("audio/voice/narr_shenlan_b96ec02ee1ba15b70989.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b96ec02ee1ba15b70989.ogg")
    "小满把模型摆在照片正中间，底座没有再打开。"
    if f_told == "truth" or f_told == "ask":
        voice ("audio/voice/narr_shenlan_3f4bea80810b966d0520.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3f4bea80810b966d0520.ogg")
        "她知道我原来的打算。我走那天托人带的那把钥匙，比说再见容易一点。"
    elif m9_told or p_branch == "xiaoman":
        voice ("audio/voice/narr_shenlan_a6435d5dd1062d5d9969.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_a6435d5dd1062d5d9969.ogg")
        "她早知道这家店可能要关。后来还有客人敲门，是她去开的。"
    if m6_ask:
        voice ("audio/voice/narr_shenlan_778b9fe8bd66a02d25a7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_778b9fe8bd66a02d25a7.ogg")
        "我走前想起问过陆遥，为什么把那三个字划掉。他那天到底没告诉我。"
    else:
        voice ("audio/voice/narr_shenlan_04b1f5ff378ee4bc2604.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_04b1f5ff378ee4bc2604.ogg")
        "我到最后也没问，为什么他写了「留下来」，又把它划掉。"
    call screen ending_title("没有回头", "车开了，窗外的灯一盏一盏往后退。", "四")
    return


label ending_funeral:
    $ f_ending = "完成葬礼"
    $ mark_cleared()
    $ bgm("funeral")
    $ unlock_record("end_funeral")
    scene cg ending funeral with paperdissolve
    voice ("audio/voice/narr_shenlan_72ecc29e94f37f61c1b3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_72ecc29e94f37f61c1b3.ogg")
    "沈岚在那天去世了。"
    voice ("audio/voice/narr_shenlan_7af3e7d47ddf3e1adeee.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7af3e7d47ddf3e1adeee.ogg")
    "接下来三天，咖啡店一直关着门。"
    voice ("audio/voice/narr_shenlan_0c1d20cb4fee287c31c6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0c1d20cb4fee287c31c6.ogg")
    "第四天，是小满来开的门。"
    voice ("audio/voice/narr_shenlan_69762c4344ccd89aa63d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_69762c4344ccd89aa63d.ogg")
    "她从柜台那张桌子开始，一张一张擦过去。抹布脏了就去洗一遍。"
    voice ("audio/voice/narr_shenlan_58d9bf113dccf4951c85.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_58d9bf113dccf4951c85.ogg")
    "陆遥带了束满天星，在门口站了会儿才进来。"
    voice ("audio/voice/narr_shenlan_64701462163eb725424b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_64701462163eb725424b.ogg")
    "小满从架子上取了个空杯子，往里倒了点水，让他把花插进去。"
    voice ("audio/voice/narr_shenlan_d2a57a9e4280f9ec3dc2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d2a57a9e4280f9ec3dc2.ogg")
    "模型还摆在柜台上。小满把那只耳朵缝歪的布兔子扶了扶。"
    if p_branch != "xiaoman":
        voice ("audio/voice/narr_shenlan_e0634401509dc1edb46a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e0634401509dc1edb46a.ogg")
        "小满后来把抽屉拉开，从里面拿出那封写着自己名字的信。"
    else:
        voice ("audio/voice/narr_shenlan_34169b646849dc5e78f4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_34169b646849dc5e78f4.ogg")
        "小满把那封写给自己的信重新展开。"
    voice ("audio/voice/narr_shenlan_2d062f6d7519a0cbe276.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2d062f6d7519a0cbe276.ogg")
    "信的末尾是沈岚的字：「累了就关门，饿了就吃饭。」"
    voice ("audio/voice/narr_shenlan_ae257b3835afc30cdafa.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ae257b3835afc30cdafa.ogg")
    "后来他们收拾了店里的东西，把能带走的分了分。"
    voice ("audio/voice/narr_shenlan_0c5a3b93e790d19f56c4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0c5a3b93e790d19f56c4.ogg")
    "陆遥把钥匙和剩下的账单一起交还给房东。"
    voice ("audio/voice/narr_shenlan_6b21b95c0b1843155acf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6b21b95c0b1843155acf.ogg")
    "那扇玻璃门再也没翻到「营业」。"
    call screen ending_title("完成葬礼", "柜台上的杯子里，还插着那束满天星。", "五")
    return


# ---------------- 白夜 / 真话结局 ----------------

label ending_white_night:
    $ f_ending = "白夜"
    $ mark_cleared()
    $ bgm("night")
    $ unlock_record("end_white")
    scene cg ending together at cold_wash with paperdissolve
    voice ("audio/voice/narr_shenlan_3739afd202a6abe42251.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3739afd202a6abe42251.ogg")
    "店又开了。早上来送牛奶的人照旧在后门敲了三下。"
    voice ("audio/voice/narr_shenlan_e0627c518ae72b725ed4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e0627c518ae72b725ed4.ogg")
    "我划掉了原来圈着的日期，也没特意去给陆遥看。"
    voice ("audio/voice/narr_shenlan_d349db915ad5f49dfebd.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d349db915ad5f49dfebd.ogg")
    "新合同是我签的，首期房租还差一点。陆遥用晚班的钱一点点补上。"
    voice ("audio/voice/narr_shenlan_699de36efcf17381b37a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_699de36efcf17381b37a.ogg")
    "我几次想问他还要做多久夜班，话到嘴边又收回去。"
    voice ("audio/voice/narr_shenlan_744e32ab79f3d4beb0c0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_744e32ab79f3d4beb0c0.ogg")
    "他来时还是点美式，四点一到就走。"
    voice ("audio/voice/narr_shenlan_e0d195caa4b5c773aac3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e0d195caa4b5c773aac3.ogg")
    "我也还往他碟子边放纸星，偶尔放两颗。"
    voice ("audio/voice/narr_shenlan_8e89fd29232474b55557.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8e89fd29232474b55557.ogg")
    "客人进来看到的，还是原来那个样子。"
    voice ("audio/voice/narr_shenlan_245caa04f998b11f08a6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_245caa04f998b11f08a6.ogg")
    "只有我在翻账的时候，总不知道他转来的钱该记在哪一页。"
    if a_broke:
        voice ("audio/voice/narr_shenlan_fa24a267f092a877aa42.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fa24a267f092a877aa42.ogg")
        "他回来那天，我把他留在桌上的钥匙递还给他。"
        voice ("audio/voice/narr_shenlan_624a3483cb49794d2163.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_624a3483cb49794d2163.ogg")
        "他接过去，第二天就拿它给送货的人开了门。"
    voice ("audio/voice/narr_shenlan_0f49f47e5f3d45742d77.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0f49f47e5f3d45742d77.ogg")
    "有一回隔着窗户，我看见他靠在椅背上睡着了。"
    voice ("audio/voice/narr_shenlan_cf0f6e5a297444293de8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cf0f6e5a297444293de8.ogg")
    "我在门外站了一阵，等他自己醒。"
    call screen ending_title("白夜", "明天四点，他还是得去换班。", "六")
    return


label ending_told:
    $ quick_menu = False
    $ f_ending = "如果那天我说了"
    $ mark_cleared()
    $ bgm("ending")
    $ unlock_record("end_told")
    scene black with warmfade
    call screen chapter_card("第五章", "如果那天我说了", "那天晚上")
    scene bg shop night with paperdissolve
    if l_lease_told:
        voice ("audio/voice/narr_shenlan_3d182cc8b4996984aebe.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3d182cc8b4996984aebe.ogg")
        "都聊到这里了，我把垫过多少钱也写了下来。"
    else:
        voice ("audio/voice/narr_shenlan_b4ef4b269a0d79c0e3f2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b4ef4b269a0d79c0e3f2.ogg")
        "她把我垫过钱的那张收据翻到背面，留了空白给我写。"
    voice ("audio/voice/narr_shenlan_507483427c389cb6b35d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_507483427c389cb6b35d.ogg")
    "我把补偿、排班，还有那份推掉的工作逐项写下。店里过夜那几晚，我这回也照实说了。"
    voice ("audio/voice/narr_shenlan_4eb6abf6a9801d70888c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4eb6abf6a9801d70888c.ogg")
    "她等我写完，才去翻自己的账本。"
    voice ("audio/voice/narr_shenlan_8a7688e33ab4bbbf9968.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8a7688e33ab4bbbf9968.ogg")
    "我看她摊开账本，才知道原来还有几笔钱她也在瞒着。"
    voice "audio/voice/finale_382.ogg"
    shenlan "……店可能要关了。"
    voice "audio/voice/finale_383.ogg"
    luyao "我知道。"
    voice "audio/voice/finale_384.ogg"
    shenlan "你早就知道？"
    voice "audio/voice/finale_385.ogg"
    luyao "我一直在算。"
    voice ("audio/voice/narr_shenlan_c599cd4a4c1e0dd85c92.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c599cd4a4c1e0dd85c92.ogg")
    "她把模型的抽屉打开，取出那把备用钥匙和写给小满的信。"
    voice ("audio/voice/narr_shenlan_929f18dffefc504669e3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_929f18dffefc504669e3.ogg")
    "她从柜台底下拿出日历，指给我看圈住的那个日期。她说，那是她原来给自己定的日子。说完她把日历合上，问我能不能先帮她算算下个月的账。"
    voice ("audio/voice/narr_shenlan_bc67841d81c9915ff130.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bc67841d81c9915ff130.ogg")
    "沈岚朝后间喊了声小满。小满推门进来的时候，手里还拿着扫帚。"
    voice "audio/voice/xiaoman_faa782801c61a109afe8.ogg"
    xiaoman "我在后间听见了。你们算到哪儿了？上个月的水电费是我记的。"
    voice ("audio/voice/narr_shenlan_8340963ed815af5544a6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8340963ed815af5544a6.ogg")
    "小满把账本翻到新的一页，把我们俩说的数都记下来。"
    if m9_told:
        voice "audio/voice/xiaoman_7b27d660f8ce3c126d8b.ogg"
        xiaoman "后间那几桌平时坐不满。我拿账本问过房东，他愿意谈只租前面的价钱。"
    else:
        voice "audio/voice/xiaoman_87d47b00c84f5995c54e.ogg"
        xiaoman "后间那几桌平时坐不满。要是只租前面呢？先等我算算。"
    voice "audio/voice/shenlan_5dacd81ba9f68edc9197.ogg"
    shenlan "铺子要是能留下，小满，你想管店吗？"
    voice "audio/voice/xiaoman_73d7dbb155a439f795f1.ogg"
    xiaoman "我想先试一个月。到时候咱们再坐下来看看。"
    voice ("audio/voice/narr_shenlan_62c4ea73af965be18203.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_62c4ea73af965be18203.ogg")
    "我去找能在家做的活。沈岚说她继续做手工，每周给自己多留一天休息。"
    scene cg ending told with paperdissolve
    voice ("audio/voice/narr_shenlan_8646f4ad8860b8f67c34.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8646f4ad8860b8f67c34.ogg")
    "一周后，小满把门口的小黑板擦干净，重新写上了字。"
    voice ("audio/voice/narr_shenlan_89e8f21b32dc6e6b740e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_89e8f21b32dc6e6b740e.ogg")
    "上面还留着旧菜单擦不掉的粉笔印。她在空白的地方写了「营业中」。"
    voice ("audio/voice/narr_shenlan_e8cb235a0482e66a39c8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_e8cb235a0482e66a39c8.ogg")
    "沈岚把原来圈过的那页日历折起来，放进了空着的模型底座。"
    voice ("audio/voice/narr_shenlan_7017091d9fb95a5ebe4d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7017091d9fb95a5ebe4d.ogg")
    "晚上她比平时早走。我出来锁门时，小满已经在门口等我了。"
    $ bgm("letter", fadein=2.5)
    call screen ending_title("如果那天我说了", "后来值谁的班，三个人都知道。", "七")
    return


# ============================================================
# 二周目 · 陆遥视角 · 琴盖合上
# 他在门外听见两人说话；进屋后接回门铃段落。
# ============================================================

label luyao_pov_finale:
    $ quick_menu = False
    $ bgm("night")
    scene black with warmfade
    call screen chapter_card("第五章", "琴盖合上", "原定关店前一晚")

    scene bg street rain with paperdissolve
    voice ("audio/voice/narr_shenlan_285f9ee3f1d8fa48e1e9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_285f9ee3f1d8fa48e1e9.ogg")
    "原定关门的前一晚，我站在门口，听见小满在里头说话。"
    voice ("audio/voice/narr_shenlan_34ae0484702b28afa89e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_34ae0484702b28afa89e.ogg")
    "她的声音隔着玻璃听不全，只听见她问，怎么突然交代这么多事。"
    voice ("audio/voice/narr_shenlan_0e3bc1cc076e31cec291.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0e3bc1cc076e31cec291.ogg")
    "我在外面站到雨停。"
    $ unlock_record("finale")
    scene bg shop night with paperdissolve
    jump finale_door


# ============================================================
# 二周目 · 陆遥视角 · 结局
# 玩家以陆遥的身份做最后的选择；CG 与结局卡复用
# ============================================================

label finale_choice_luyao:
    menu:
        "问她愿不愿意继续开店":
            if a_heat <= 1:
                jump ending_together_luyao
            else:
                jump ending_white_night_luyao
        "提议把店交给小满":
            jump ending_xiaoman_luyao
        "问她要不要跟我一起走":
            jump ending_with_him_luyao
        "让她自己走":
            jump ending_alone_luyao
        "由她照信里的打算告别":
            jump ending_funeral_confirm


label ending_together_luyao:
    $ f_ending = "一起开"
    $ mark_cleared()
    $ bgm("ending")
    $ unlock_record("end_together")
    scene cg ending together with paperdissolve
    voice ("audio/voice/narr_shenlan_69684c48aea016fc0a67.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_69684c48aea016fc0a67.ogg")
    "她等我问完，顺手把柜台上两只杯子叠了起来。"
    voice ("audio/voice/narr_shenlan_612ee43415de90111e36.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_612ee43415de90111e36.ogg")
    "她说：「后间退掉，店就得挤一点。」"
    voice ("audio/voice/narr_shenlan_3a01218cc20c6442c140.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3a01218cc20c6442c140.ogg")
    "我说：「杯子实在放不下，可以从我那个开始收。」"
    voice ("audio/voice/narr_shenlan_6208399ece2f1544505f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6208399ece2f1544505f.ogg")
    "第二天我还没到门口，就看见她已经把牌子翻到了「营业」。"
    voice ("audio/voice/narr_shenlan_7a88c7a464f5af12cdb9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7a88c7a464f5af12cdb9.ogg")
    "后来我见到她划掉了原来圈的那个日期，手边还有一支没盖帽的笔。"
    voice ("audio/voice/narr_shenlan_61baa205d33665b9c3b3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_61baa205d33665b9c3b3.ogg")
    "门开得早，太阳从玻璃门照进来，刚好照到我坐的那把椅子上。"
    voice ("audio/voice/narr_shenlan_bc0dcd659d70d58ae863.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bc0dcd659d70d58ae863.ogg")
    "小满没叫我去柜台取。她把那杯菜单上最贵的咖啡直接端了过来。"
    voice ("audio/voice/narr_shenlan_b1f7aa9e911448855821.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b1f7aa9e911448855821.ogg")
    "我刚收到新的录用通知。她走到窗边，我把那几页纸往她那边推了推。"
    voice "audio/voice/finale_461.ogg"
    luyao "这次，我先问你。"
    voice "audio/voice/finale_462.ogg"
    shenlan "问什么？"
    voice "audio/voice/finale_463.ogg"
    luyao "你愿不愿意，让我留下来。"
    voice ("audio/voice/narr_shenlan_584c78f76293d333972d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_584c78f76293d333972d.ogg")
    "她把松了的底座粘好，重新放回柜台角上。"
    if l_lease_told:
        voice ("audio/voice/narr_shenlan_7d924644cfe944ccc151.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_7d924644cfe944ccc151.ogg")
        "下个月的房租是当着我们的面一起算的。我等她算完，再说自己能出多少。"
    voice ("audio/voice/narr_shenlan_befb37f3a0eef0b8b346.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_befb37f3a0eef0b8b346.ogg")
    "她在开店前把琴盖掀了起来，试了两个音。"
    if m8_hand:
        voice ("audio/voice/narr_shenlan_9fd7cfccd39f810173e1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_9fd7cfccd39f810173e1.ogg")
        "我把手伸过去，她一把就牵住了。"
    if m4_feed:
        voice ("audio/voice/narr_shenlan_039f673ae14559804fc6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_039f673ae14559804fc6.ogg")
        "年糕爬到我腿上，我得用一只手翻那份通知。"
    voice ("audio/voice/narr_shenlan_aa5477c2002bf416baaa.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_aa5477c2002bf416baaa.ogg")
    "下午有人问店里在放什么，她说，那首叫《满天星》。"
    voice ("audio/voice/narr_shenlan_65d30663f67a93fbb25a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_65d30663f67a93fbb25a.ogg")
    "一个月以后，我们清出半个柜台摆了个小展。"
    show cg exhibition with dissolve
    voice ("audio/voice/narr_shenlan_1a3864b2d11b1a178009.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1a3864b2d11b1a178009.ogg")
    "模型旁边是一罐纸星。星图册翻开在猎户座那一页，想看的人可以自己往后翻。"
    hide cg exhibition with dissolve
    $ bgm("letter", fadein=2.5)
    call screen ending_title("一起开", "明天开门的时候，这回有人一起。", "一")
    return


label ending_white_night_luyao:
    $ f_ending = "白夜"
    $ mark_cleared()
    $ bgm("night")
    $ unlock_record("end_white")
    scene cg ending together at cold_wash with paperdissolve
    voice ("audio/voice/narr_shenlan_b33fd656899691e90c3c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b33fd656899691e90c3c.ogg")
    "她说，店再开一阵吧。"
    voice ("audio/voice/narr_shenlan_da12dc3af6fd1843dd8f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_da12dc3af6fd1843dd8f.ogg")
    "她跟房东签了新合同。我把攒下来的夜班钱转出去，又在手机上设了个提醒，下周还要转一笔。"
    voice ("audio/voice/narr_shenlan_c7017991a50d53dfda4f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c7017991a50d53dfda4f.ogg")
    "我后来去翻柜台上的日历，那个圈已经被涂掉了。"
    if l_lease_told:
        voice ("audio/voice/narr_shenlan_1cdabbc8d7e98546d434.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1cdabbc8d7e98546d434.ogg")
        "她问过我能不能先还一点。我说等月底再说。"
    voice ("audio/voice/narr_shenlan_d70bcc9a2d608a63fdb0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d70bcc9a2d608a63fdb0.ogg")
    "到了下午四点，我还是合上电脑去换班。"
    voice ("audio/voice/narr_shenlan_fa6282f81f7afa0e806a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_fa6282f81f7afa0e806a.ogg")
    "我走的时候，碟子边有颗纸星。我这几天没收，已经攒了好几颗。"
    voice ("audio/voice/narr_shenlan_3a6ceb0f3702f9067b67.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3a6ceb0f3702f9067b67.ogg")
    "我有时坐在窗边等咖啡，连她把杯子端上来都没听见。"
    if a_broke:
        voice ("audio/voice/narr_shenlan_5f8399a0bb6973b48576.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5f8399a0bb6973b48576.ogg")
        "后来她把我留在桌上的钥匙又还给了我。"
        voice ("audio/voice/narr_shenlan_3d804c551ee8db9fd006.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3d804c551ee8db9fd006.ogg")
        "我第二天照旧用它给送货的人开门，顺便把早班能干的活都干了。"
    voice ("audio/voice/narr_shenlan_50867bc1f535ed7217b0.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_50867bc1f535ed7217b0.ogg")
    "有回她站在窗外看我。我睁开眼的时候，她刚把门推开。"
    voice ("audio/voice/narr_shenlan_ae330b271114bbb2c8e9.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ae330b271114bbb2c8e9.ogg")
    "我坐直了，跟她说我没睡。"
    call screen ending_title("白夜", "明天四点，我还是得去换班。", "六")
    return


label ending_xiaoman_luyao:
    jump xiaoman_handover


label ending_with_him_luyao:
    $ f_ending = "她和他走"
    $ mark_cleared()
    $ bgm("ending")
    $ unlock_record("end_depart")
    scene cg ending depart with paperdissolve
    voice ("audio/voice/narr_shenlan_3337a03ae1bec70c51a1.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3337a03ae1bec70c51a1.ogg")
    "我问她，要不要一起出去几天。等到了车站，再看去哪儿。"
    voice ("audio/voice/narr_shenlan_81df42ced3a0d2d23a15.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_81df42ced3a0d2d23a15.ogg")
    "她低头想了一会儿，嗯了一声。"
    voice ("audio/voice/narr_shenlan_0493b734b444c994dbb6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0493b734b444c994dbb6.ogg")
    "小满答应先帮她开几天门。她把钥匙交过去，用旧围裙裹着那只常用的杯子就来了。"
    voice ("audio/voice/narr_shenlan_f4b9308a6fcb6c38a80b.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f4b9308a6fcb6c38a80b.ogg")
    "我在车站入口等她。她一到，就叫我一起去看车次。"
    voice ("audio/voice/narr_shenlan_80b91afb0b27df100445.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_80b91afb0b27df100445.ogg")
    "正好有一班车还剩两个空位，她说就这趟吧。"
    voice ("audio/voice/narr_shenlan_6bd5066e78008e9ee901.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6bd5066e78008e9ee901.ogg")
    "检票前，她把杯子递给我，自己腾出手去拿票。"
    if m8_hand:
        voice ("audio/voice/narr_shenlan_cec352d4c2ab6aa79f1e.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cec352d4c2ab6aa79f1e.ogg")
        "我牵住她的时候，她刚把两张票都拿出来。"
    voice ("audio/voice/narr_shenlan_8b6373bd6397e30fbb52.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8b6373bd6397e30fbb52.ogg")
    "她低头看了眼票上的日期，说离她原来定的那一天，还有几天。"
    voice ("audio/voice/narr_shenlan_2386925b111a396b3c25.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_2386925b111a396b3c25.ogg")
    "我问她这几天想先做什么。她说等上了车，先看看窗外。"
    call screen ending_title("她和他走", "下一班车，两张票。", "三")
    return


label ending_alone_luyao:
    $ f_ending = "没有回头"
    $ mark_cleared()
    $ bgm("night")
    $ unlock_record("end_alone")
    scene cg ending alone with paperdissolve
    voice ("audio/voice/narr_shenlan_36ac88dc5a67d672eff3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_36ac88dc5a67d672eff3.ogg")
    "我正要推门进店，沈岚打了通电话过来。"
    voice ("audio/voice/narr_shenlan_bf1a9e82dd0d7f019a74.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_bf1a9e82dd0d7f019a74.ogg")
    "她说车快开了，我才知道她已经到了车站。"
    voice ("audio/voice/narr_shenlan_05f40ea4941a3ec0877d.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_05f40ea4941a3ec0877d.ogg")
    "她没有说要去哪站。我也没问。"
    if p_branch == "xiaoman":
        voice ("audio/voice/narr_shenlan_ef70d75d52534b563921.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_ef70d75d52534b563921.ogg")
        "她给小满的信已经送到了，我没再去碰模型。"
    elif p_branch == "closed":
        voice ("audio/voice/narr_shenlan_4ff52831a33ac91df3e3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_4ff52831a33ac91df3e3.ogg")
        "那封信还封在底座里面。"
    else:
        voice ("audio/voice/narr_shenlan_c2b80600f274b0eca340.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_c2b80600f274b0eca340.ogg")
        "我上次放回去的那封信还在模型底座里。"
    voice ("audio/voice/narr_shenlan_6e3f84b69011344e52e8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_6e3f84b69011344e52e8.ogg")
    "火车那头好像有人在广播，隔着电话听不太清。"
    voice ("audio/voice/narr_shenlan_d4486375ccd891e7588f.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d4486375ccd891e7588f.ogg")
    "她说得收手机了。我拿着手机，又在街上站了一会儿。"
    voice ("audio/voice/narr_shenlan_8412490efe10621c07d7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8412490efe10621c07d7.ogg")
    "后来我经过那条街，店招还亮着，是小满开的门。"
    voice ("audio/voice/narr_shenlan_8ad8a73c0db6403b9c03.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8ad8a73c0db6403b9c03.ogg")
    "有天小满说要办个小展，让我来帮她把模型往中间挪一挪。"
    if m9_told:
        voice ("audio/voice/narr_shenlan_b341054d4980cf804466.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b341054d4980cf804466.ogg")
        "她走以后，小满拿了钥匙去见房东，回来还跟我说起铺租的事。"
    if m6_ask:
        voice ("audio/voice/narr_shenlan_63e4b050cf2af7d059a8.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_63e4b050cf2af7d059a8.ogg")
        "星图册还在老地方。那几个被划掉的字她问过，我没答。"
    else:
        voice ("audio/voice/narr_shenlan_f2551587aaf2a23adcd7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_f2551587aaf2a23adcd7.ogg")
        "星图册还在老地方。她看到过那一页没有，我一直都不知道。"
    call screen ending_title("没有回头", "她打来的那通电话里，火车就快开了。", "四")
    return


label ending_funeral_luyao:
    $ f_ending = "完成葬礼"
    $ mark_cleared()
    $ bgm("funeral")
    $ unlock_record("end_funeral")
    scene cg ending funeral with paperdissolve
    voice ("audio/voice/narr_shenlan_72ecc29e94f37f61c1b3.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_72ecc29e94f37f61c1b3.ogg")
    "沈岚在那天去世了。"
    voice ("audio/voice/narr_shenlan_5538d9335875226fcfd4.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_5538d9335875226fcfd4.ogg")
    "接下来三天，玻璃门一直锁着。"
    voice ("audio/voice/narr_shenlan_0c1d20cb4fee287c31c6.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_0c1d20cb4fee287c31c6.ogg")
    "第四天，是小满来开的门。"
    voice ("audio/voice/narr_shenlan_3adf211b17733e3e6607.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3adf211b17733e3e6607.ogg")
    "她拿着抹布，把柜台边那张桌子先擦了。擦完又去洗抹布。"
    voice ("audio/voice/narr_shenlan_8054d08afb18644fbd3c.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_8054d08afb18644fbd3c.ogg")
    "我带了束满天星，在门口站了会儿才进去。"
    voice ("audio/voice/narr_shenlan_dba68fed8d68ecb59346.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_dba68fed8d68ecb59346.ogg")
    "她拿了个空杯子给我。我去接水，把花插进去。"
    voice ("audio/voice/narr_shenlan_11fcf1b3deedaaceecb7.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_11fcf1b3deedaaceecb7.ogg")
    "模型还在柜台上，小满伸手扶了扶那只坐不稳的兔子。"
    if p_branch != "xiaoman":
        voice ("audio/voice/narr_shenlan_06a1c8f00c2ed45e3736.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_06a1c8f00c2ed45e3736.ogg")
        "小满把抽屉拉开，从里面拿出那封信。"
    voice ("audio/voice/narr_shenlan_b980b00bd6dfdded8da2.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_b980b00bd6dfdded8da2.ogg")
    "她把信展开，指给我看最后一行。"
    voice ("audio/voice/narr_shenlan_3e9baab4e89797a98d4a.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_3e9baab4e89797a98d4a.ogg")
    "「累了就关门，饿了就吃饭。」"
    voice ("audio/voice/narr_shenlan_d37a5d5484a801d5ebcf.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_d37a5d5484a801d5ebcf.ogg")
    "那天我们把店里的东西陆续收进纸箱。"
    voice ("audio/voice/narr_shenlan_1aaf563a02aa70f3e700.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_1aaf563a02aa70f3e700.ogg")
    "小满拿走了模型。我把剩下的账单和钥匙交给了房东。"
    voice ("audio/voice/narr_shenlan_cfecfbcaefa174a88876.ogg" if pov == "shenlan" else "audio/voice/narr_luyao_cfecfbcaefa174a88876.ogg")
    "后来每次经过，那扇玻璃门都锁着。"
    call screen ending_title("完成葬礼", "柜台上的杯子里，还插着那束满天星。", "五")
    return
