# ============================================================
# 中段故事 · 相遇（记录 2–4）
# 记录 2：一杯咖啡，一颗星
# ============================================================

default m2_star = False
default m2_talk = False
default m3_fix = False
default m3_ask = False
default m4_feed = False
default m4_ask = False
default m6_write = False
default m6_ask = False

label story_days_early:
    jump scene_first_star


label scene_first_star:
    scene black with warmfade
    centered "{size=32}{color=#e8c7a8}两个月前{/color}{/size}"

    scene bg shop day with paperdissolve
    "两个月前。那天下雨。"
    "店里没有客人，只有窗边坐了一个人。"
    show luyao sad_half at expr_right with dissolve
    "他背着一个旧电脑包，电脑开着。屏幕停在一封邮件上。"
    "离得很远，也能看见「裁员」两个字。"
    "他点了最便宜的美式，不加糖。"
    "我做好咖啡，端过去。"
    "柜台上放着一罐纸星，每一颗上面都写着一句话。"
    "有一颗写着：撑住。"

    menu:
        "把「撑住」放在碟子边。":
            $ m2_star = True
            "我把那颗星放在碟子边，没有解释。"
            "他愣了一下。"
        "只放咖啡。":
            "我把咖啡放下，收走了托盘。"

    "他抬头看了我一眼。"
    luyao "……谢谢。"
    if m2_star:
        "他把那颗星捏在手里，看了很久，放进了口袋。"
        "那天他走的时候，罐子里的星星少了一颗。"
    else:
        "他把咖啡挪到电脑旁边，继续盯着那封邮件。"
        "走的时候，他在碟子下面压了一枚硬币。正好是一颗纸星的钱。"

    menu:
        "问他屏幕上是什么。":
            $ m2_talk = True
            shenlan "……工作的事？"
            luyao "嗯。"
            luyao "今天开始，不用去了。"
            "他说得很平静，像在说天气。"
            shenlan "……那你还点最便宜的？"
            luyao "习惯了。"
            "他笑了一下。那个笑很轻，像随时会掉。"
        "什么也不问。":
            "我没有问。"
            "他也没有说。"
            "我们隔着一张桌子，听了一下午的雨。"

    "那天他坐到打烊。"
    "第二天，他又来了。还是最便宜的美式，还是窗边。"
    "从那以后，他几乎每天都来。"
    "我每天在碟子边放一颗星。"
    if m2_star:
        "他把每一颗都收进口袋。"
    else:
        "他每天在柜台放一枚硬币，自己拿一颗星。"
    "下午四点，他会合上电脑离开。"
    "我从来没有问过他要去哪。"

    $ unlock_record("first_star")
    scene black with warmfade
    "后来店里的人都说，那位常客很奇怪。"
    "只点最便宜的美式，从来不笑，走的时候电脑包总是鼓的。"
    if m2_star:
        "只有我知道，他口袋里有星星。"
    else:
        "只有我知道，他每天都会自己拿一颗星星。"
    jump scene_card_reader


label scene_card_reader:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}几天后{/color}{/size}"

    scene bg shop day with paperdissolve
    show xiaoman neutral_half at half_right with dissolve
    "几天后，刷卡机坏了。"
    "客人排到门口，机器一直响，屏幕上跳出一行看不懂的字。"
    shenlan "……等一下，马上好。"
    xiaoman "老板，你按那个红色的——"
    shenlan "哪个红色？"
    "小满凑过来，按了两下，机器响得更凶了。"
    show xiaoman pout_half at expr_right with dissolve
    xiaoman "……不是我。"
    "我正要拔电源，窗边那位常客站了起来。"

    show luyao awkward_half at expr_left with dissolve
    luyao "我看看。"
    "他蹲到柜台后面，把线拔了，又插回去。"
    "手指很稳。"

    menu:
        "让他修。":
            $ m3_fix = True
            "我退开半步，把位置让给他。"
            xiaoman "老板，你就让他修嘛。"
            "小满在旁边小声起哄。"
            "他低头拧着什么，耳朵有点红。"
        "自己修。":
            "我说不用，自己来。"
            "我把机器翻过来，学着他的样子拔线，拔错了。"
            "他伸手，按住我的手。"
            luyao "这根。"
            "他的手指很凉。"

    "几分钟后，机器吐出一张长长的小票。"
    shenlan "……好了？"
    luyao "好了。"
    xiaoman "哇。"
    shenlan "你是做什么的？"
    luyao "程序员。"
    shenlan "程序员还修这个？"
    luyao "都是修东西。"
    "他说得很自然。"
    "我笑了一下。"
    "他抬头，正好看见。"
    "然后他低下头，去收工具。"

    "手背上贴着一块创可贴，边缘已经卷起来了。"
    "电脑包侧袋里，露出一角折起来的纸。"

    menu:
        "问他工作的事。":
            $ m3_ask = True
            shenlan "你以前……在哪家公司？"
            luyao "说了你也不认识。"
            "他把工具收进包里，动作停了一下。"
            luyao "最近在休息。"
            "他没有说「失业」。"
            "我也没有再问。"
        "什么也不问。":
            "我没有问。"
            "他把工具收好，回窗边坐下。"
            "那角折纸从包里露出一小截，像一句没说完的话。"

    "他走的时候，又点了一杯美式。"
    "我在碟子边放了一颗星。"
    if m3_fix:
        "他把星和螺丝刀一起收进包里。"
    else:
        "他把星放在电脑旁边，看了很久。"
    $ unlock_record("card_reader")

    scene black with warmfade
    "后来机器又坏过两次。"
    "第二次，我自己修好了。"
    "第三次，我没修，等他来。"
    jump scene_useless_things

label scene_useless_things:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}又一个打烊的晚上{/color}{/size}"

    scene bg back room with paperdissolve
    show luyao awkward_half at expr_right with dissolve
    "打烊以后，我在后间捏一个泥人。"
    "他坐在旁边看，电脑包放在脚边。"
    "后间的架子上摆着小满做的兔子，耳朵是缝歪的。"
    "墙上贴着她剪的星星，胶带都翘起来了。"
    "这个店里到处都是她。"
    luyao "你做的这些，有人买吗？"
    shenlan "没有。"
    luyao "那你为什么还做？"
    shenlan "……那你写的代码，有人用吗？"
    luyao "以前有。现在没了。"
    "我们同时笑了一下。"
    "笑完，谁都没有说话。"

    "门口传来一声很轻的响动。"
    "一只三花猫从纸箱后面探出头。"
    show mem cat at cat_sit with dissolve
    "它脖子上挂着一个小小的牌子，上面写着：年糕。"
    "是小满的字。"
    luyao "……它叫年糕？"
    shenlan "小满取的。"
    luyao "挺合适的。"
    "年糕看了我们一会儿，慢吞吞地走过来。"

    menu:
        "一起喂它。":
            $ m4_feed = True
            "我把猫粮倒在手心，他把手伸过来，和我一起托着。"
            "年糕低头吃，胡须扫过我们的手指。"
            "他的手很暖。"
        "让他自己喂。":
            "我把猫粮递给他。"
            "他蹲下去，手心摊开，很认真地等。"
            "年糕闻了闻，才低头吃。"
            "他笑得很轻，像怕吓到它。"

    "年糕吃完，跳上窗台，团成一团。"
    "他站起来，看见玻璃门上的「转让」牌子。"
    "他伸手，把它摘了下来。"
    shenlan "……你干嘛？"
    luyao "风大。"
    "他把牌子折好，塞进自己的电脑包。"
    "我没有问。"

    menu:
        "问他为什么四点走。":
            $ m4_ask = True
            shenlan "你每天四点走……是有事吗？"
            "他把包带往肩上提了提。"
            luyao "有点事。"
            "他没有说是什么事。"
            "我也没有再问。"
        "什么也不问。":
            "我没有问。"
            "四点的时候，他照例合上电脑。"
            "走到门口，他回头看了一眼，像要说什么。"
            "最后只说了一句：「明天见。」"

    "那天他走后，我把泥人捏完了。"
    "一个很小的、没有名字的人。"
    "年糕从窗台上跳下来，蹭了蹭我的脚踝。"
    "我忽然意识到，这家店不只是我的。"
    "架子上有兔子，墙上有星星，猫碗上有一个歪歪扭扭的「年糕」。"
    $ unlock_record("shop_cat")

    scene black with warmfade
    "后来我常常想，那天他摘牌子，真的是因为风大吗。"
    jump piano_scene


label story_days_middle:
    jump scene_book_margin


label scene_book_margin:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}又过了一阵子{/color}{/size}"

    scene bg shop night with paperdissolve
    show luyao awkward_half at expr_right with dissolve
    "他每天下午都坐在窗边，对着电脑上同一个页面。"
    "有一天，我从柜台下面翻出一本旧星图册。"
    shenlan "你总看电脑，眼睛会坏。"
    luyao "……这是给我的？"
    shenlan "借你的。看完还我。"
    "他接过去，翻了两页，停在一张星图上。"
    "第二天，他把书还了回来。"

    "书页的空白处，多了一行铅笔字。"
    "「猎户座腰带的三颗星，和柜台上的三颗星排列一样。」"
    "我愣了一下。"
    "那是他第一天来，我在碟子边摆的三颗星。"

    menu:
        "在页边回他。":
            $ m6_write = True
            "我拿起铅笔，在下面写：「你数错了，是四颗。」"
            "写完又觉得太认真，想擦掉，最后没擦。"
        "只把书还回去。":
            "我把书合上，放回柜台。"
            "那一页的铅笔字，我没有动。"

    "第二天，他来借书。"
    "还回来的时候，页边又多了一行。"
    if m6_write:
        "「四颗就四颗。那第四颗是哪一颗？」"
        "我看着那行字，笑了很久。"
    else:
        "「你那次没写。」"
        "我盯着那四个字，不知道该怎么回。"

    "书里夹着一朵压干的满天星。"
    "花瓣很脆，像一碰就会碎。"
    "再往后翻，有一行被划掉的字。划得很轻，还是看得见。"

    menu:
        "问他划掉的是什么。":
            $ m6_ask = True
            "我把书推回他面前。"
            shenlan "这行划掉的是什么？"
            luyao "……写错了。"
            "他把书拿过去，用手指按住那一行。"
            "我看见他的耳朵红了。"
            "我还是看见了。那三个字是：留下来。"
            "我没有再问。"
        "不问。":
            "我把书合上。"
            "那行被划掉的字，像一句没有说出口的话。"

    "那天晚上，我把书带回家。"
    "桌上摊着店里的欠款单。我把书压在它上面。"
    "书页里那朵满天星，被我夹回了原来的位置。"

    scene bg shop day with paperdissolve
    show xiaoman neutral_half at half_right with dissolve
    "第二天，小满借走了那本书。"
    "还回来的时候，她在最后一页画了一颗星。"
    xiaoman "老板，这书挺好看的。"
    "她什么也没问。"
    "我把书放回柜台，压在收据下面。"
    $ unlock_record("book_margin")

    scene black with warmfade
    "后来那本书一直在柜台上。"
    "我们谁也没有再提页边的事。"
    jump puzzle_scene
