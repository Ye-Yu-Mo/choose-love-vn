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
default m7_star = False
default m7_phone = False
default m8_invite = False
default m8_hand = False
default m10_signed = False
default m10_told = False
default m11_looked = False
default m11_confront = False
default m9_told = False
default m9_support = False

label story_days_early:
    jump scene_first_star


label scene_first_star:
    $ bgm("rain")
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
    $ bgm("night")
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
    $ bgm("night")
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
    jump scene_door_light


label scene_door_light:
    $ bgm("rain")
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}入秋以后{/color}{/size}"

    scene bg street rain with paperdissolve
    show luyao awkward_half at expr_right with dissolve
    "入秋以后，天黑得越来越早。"
    "店招的灯不亮了。"
    "他站在门口，仰头看了一会儿。"
    luyao "有梯子吗？"
    shenlan "……你要修？"
    luyao "试试。"
    "我把后间的梯子搬出来。"
    "他爬上去，把灯罩拆下来，换了一根线。"
    "雨落在他的肩上。"
    "灯亮的时候，整条街都亮了一下。"
    shenlan "……好了。"
    luyao "好了。"

    "我从口袋里摸出一颗星。"
    "上面写着两个字：留下。"
    "我在柜台里写了很多颗星，这一颗，我一直没放回罐子里。"

    menu:
        "把星给他。":
            $ m7_star = True
            "我把星递过去。"
            shenlan "给你。"
            luyao "……这上面写的什么？"
            shenlan "你自己看。"
            "他低头看了很久。"
            "然后把它挂在了电脑包的拉链上。"
        "把星收回来。":
            "我把手缩回口袋。"
            "他没有看见。"
            "那颗星后来一直放在我的围裙口袋里。"

    "他的手机响了。"
    "他看了一眼屏幕，走到街对面去接。"
    "雨还在下。他没有打伞。"
    "我站在灯下，看见他的背影越来越远。"
    "他回来的时候，头发全湿了。"

    menu:
        "问他刚才的电话。":
            $ m7_phone = True
            shenlan "谁的电话？"
            luyao "……工作的事。"
            shenlan "这么晚？"
            luyao "嗯。"
            "他把湿头发往后拨了一下，没有看我。"
            "我没有再问。"
        "不问。":
            "我没有问。"
            "他也没有说。"
            "灯下只有雨声。"

    scene bg shop night with paperdissolve
    show xiaoman neutral_half at half_right with dissolve
    "回到店里，小满正踩在凳子上挂一串小灯。"
    xiaoman "老板，你看。"
    "暖黄色的小灯从柜台一直挂到窗边。"
    xiaoman "这样晚上也像有人等。"
    "她说这话的时候，没有看我。"
    $ unlock_record("door_light")

    scene black with warmfade
    "那天之后，店招的灯每天晚上都亮着。"
    if m7_star:
        "他的电脑包上，也多了一点光。"
    else:
        "我的围裙口袋里，那颗星一直没有送出去。"
    jump scene_umbrella


label scene_umbrella:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}那之后{/color}{/size}"

    scene bg street rain with paperdissolve
    show luyao awkward_half at expr_right with dissolve
    "那天下班，雨下得很大。"
    "他撑着一把黑色的伞，站在门口等我。"
    shenlan "你还没走？"
    luyao "顺路。"
    "他住在相反的方向。"
    "我没有拆穿他。"
    "走进雨里以后，伞一点一点往我这边偏。"
    "他的右肩很快就湿了。"

    menu:
        "牵住他的手。":
            $ m8_hand = True
            "我把手从口袋里拿出来，碰了碰他的手背。"
            "他愣了一下，然后把伞换到另一只手。"
            "他的手很凉，但握得很稳。"
        "把手插回口袋。":
            "我把手插回口袋。"
            "伞还是往我这边偏。"
            "我们隔着一小段距离，走得很慢。"

    "到楼下的时候，雨小了一点。"
    "他站在台阶下面，没有往上走。"
    "楼道的灯坏了一盏，亮一盏。"

    menu:
        "问他要不要上来。":
            $ m8_invite = True
            shenlan "要不要上来坐一会儿？"
            "他抬头看了看楼上。"
            luyao "……下次吧。"
            "他说完，又补了一句：「你早点睡。」"
            "我知道他不是不想，是不敢。"
        "说晚安。":
            "我说：「谢谢你送我。」"
            luyao "顺路。"
            "他又说了那个谎。"
            "我笑了笑，说晚安。"
            "他站在楼下，看我上楼，才走。"

    scene black with dissolve
    "那之后的日子，像被人偷偷调亮了。"
    scene bg shop day with dissolve
    "他每天下午来，点一杯最便宜的美式。"
    "我开始在碟子边放两颗星。"
    scene cg piano lesson with dissolve
    "打烊后，我教他弹琴。"
    "他还是总弹错同一个音。"
    "我从来不纠正。"
    scene bg back room with dissolve
    "书在柜台下面传来传去，页边的字越来越多。"
    "年糕开始在窗台上等他的四点。"
    "墙上的星星，多了一排。"

    scene bg shop day with paperdissolve
    show xiaoman neutral_half at half_right with dissolve
    "第二天，小满一边擦杯子一边问我。"
    xiaoman "老板，昨晚谁送你回来的？"
    shenlan "顺路。"
    xiaoman "哦——"
    "她拖长了声音，什么也没再问。"
    "但她笑了。"
    $ unlock_record("umbrella")

    scene black with warmfade
    "那把伞后来一直放在店门口。"
    "黑色的，手柄上缠了一圈胶带。"
    "是他说「坏了，还能用」的那把。"
    jump story_days_late


label story_days_late:
    jump scene_notebook


label scene_lease:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}月底{/color}{/size}"

    scene bg shop day with paperdissolve
    show xiaoman worried_half at expr_right with dissolve
    "月底，房东来了。"
    "他站在柜台外面，手里拿着一个牛皮纸文件袋。"
    "小满给他倒了水，然后退到后间门口，没有走。"
    "房东把一张纸推过来。"
    landlord "楼要卖了。新房东要重新签，租金按市价。"
    shenlan "……多少？"
    "他说了一个数。"
    "我在心里算了一遍，又算了一遍。"
    "还是不够。"

    landlord "我也不想涨。可新房东按合同来，我也没办法。"
    shenlan "……期限呢？"
    landlord "下个月十五号之前。签了，就按新价；不签，月底腾房。"
    "他说完，看了我一眼。"
    landlord "小沈，你这店开了几年了？"
    shenlan "三年。"
    landlord "嗯。"
    "他没有再说别的。"

    menu:
        "签下续租。":
            $ m10_signed = True
            "我拿起笔，签了。"
            "笔尖在纸上停了一下，还是落下去了。"
            "房东把属于我的那份推回来。"
            landlord "月底之前把第一笔打过来就行。"
            "我点头。"
        "先拖一拖。":
            "我说：「我再想想。」"
            landlord "行。十五号之前给我个准话。"
            "他把文件袋收好，走了。"
            "那张报价单留在柜台上，像一块烫手的铁。"

    scene bg shop night with paperdissolve
    show xiaoman worried_half at expr_right with dissolve
    "打烊以后，我把报价单和欠款单叠在一起，塞进柜台最里面。"
    "「转让」牌从抽屉里露出一角。"
    "小满站在门口，看着我。"
    xiaoman "老板。"
    shenlan "嗯？"
    xiaoman "……没事。"
    "她把一杯温水放在我手边，转身去擦桌子。"
    "她看见了。她没有问。"

    menu:
        "告诉陆遥。":
            $ m10_told = True
            "我给陆遥发了消息，只说了一句：店可能要关了。"
            "他回得很快：「我马上过来。」"
            "那天晚上，他来了，站在柜台外面，没有坐。"
            luyao "差多少？"
            shenlan "……不用你管。"
            luyao "我问差多少。"
            "我没有回答。"
            "他站了一会儿，走了。"
            "第二天，他没有来。"
        "不告诉他。":
            "我没有告诉他。"
            "第二天下午，他照常来，点了一杯最便宜的美式。"
            "他把电脑打开，又合上。"
            luyao "房东最近来过吗？"
            shenlan "……怎么突然问这个？"
            luyao "随便问问。"
            "他低头喝咖啡，没有再看我。"

    $ unlock_record("lease")
    scene black with warmfade
    "那张报价单一直压在柜台最里面。"
    "纸很薄，压在手里却很重。"
    jump scene_three_am


label scene_three_am:
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}那天夜里{/color}{/size}"

    scene cg 347 with paperdissolve
    "那天夜里，我落了东西在店里。"
    "回来的时候，已经过了三点。"
    if m10_told:
        "白天他没有来。夜里，他却在这里。"
    "店门没有锁。"
    "他趴在柜台上睡着了。"
    "电脑还亮着。"
    "屏幕右下角的时间是 3:47。"

    "电脑没有合上。"
    menu:
        "看。":
            $ m11_looked = True
            "我把屏幕转过来一点。"
            "店铺的支付后台，一行一行的提交记录。"
            "最新一条，三点四十六分。"
            "旁边开着一个文件夹：offer 信、租约、押金收据。"
            "付款人那一栏，是他的名字。"
            "我看了很久，才把屏幕合上。"
        "不看，只给他盖外套。":
            "我没有看。"
            "我把外套脱下来，盖在他肩上。"
            "他动了一下，没有醒。"
            "屏幕的光照着他的侧脸。"
            "有些事，不看也能猜到。"

    "他睡得很沉，眉头还皱着。"
    "柜台上放着一杯凉透的美式，只喝了一半。"

    menu:
        "叫醒他。":
            $ m11_confront = True
            "我伸手，碰到他的肩膀。"
            "他猛地醒了，第一反应是去合电脑。"
            luyao "……你怎么在这？"
            shenlan "这是我想问的。"
            "他看了一眼屏幕，又看我。"
            "他张了张嘴，最后什么也没说。"
            "我也没说话。"
            "我们隔着一台电脑，站了很久。"
        "不叫醒他。":
            "我没有叫醒他。"
            "我坐在旁边的椅子上，等到天快亮。"
            "他醒来的时候，我已经把电脑合上了。"

    scene bg shop day with paperdissolve
    "天亮以后，他像什么都没发生过一样，点了一杯美式。"
    luyao "昨晚……谢谢你。"
    shenlan "谢什么？"
    luyao "……外套。"
    "他低头喝咖啡。"
    "我们谁也没有提电脑。"
    if m11_confront:
        "他今天没有打开电脑。"
        "走的时候，他站在门口，像要说什么。"
        "最后还是只说了一句：「明天见。」"
    else:
        "走的时候，他照例在四点合上电脑。"
        "我看着他出门，没有拦。"

    $ unlock_record("truth_347")
    scene black with warmfade
    "后来我常常想起 3:47 这个时间。"
    "那是我从来没有醒着见过的时刻。"
    "他替我在那个时刻，守了很久。"
    jump puzzle_scene


label scene_notebook:
    $ bgm("night")
    scene black with warmfade
    centered "{size=30}{color=#e8c7a8}离月底还有几天{/color}{/size}"

    scene bg shop day with paperdissolve
    show xiaoman neutral_half at half_right with dissolve
    "下午没什么客人，小满趴在柜台上写东西。"
    "她写得很快，写两笔就抬头数一遍罐子里的星星。"
    shenlan "在写什么？"
    xiaoman "秘密。"
    "她把本子合上，又忍不住翻开给我看。"
    "「今天送出去 17 个星星。」"
    "下面还有一行小字：「第 4 位客人问能不能多要一颗，给了。」"
    "本子已经写了小半本。"

    "她的手机响了。"
    "她看了一眼屏幕，脸上的笑收了一点。"
    xiaoman "……我妈。"
    "她走到后间门口去接。"
    "门没有关严。"

    xiaoman "……嗯，在上班。"
    xiaoman "不是玩，是工作。"
    xiaoman "……我知道。"
    xiaoman "妈，我会想的。"
    "她挂了电话，站在那里没有动。"

    show xiaoman worried_half at expr_right with dissolve
    "她回来的时候，眼睛有点红。"
    xiaoman "我妈说，让我回老家考编。"
    shenlan "……你怎么说？"
    xiaoman "我说我再干一年。"
    "她低头，把本子翻到新的一页。"
    xiaoman "老板，我是不是很没出息？"

    menu:
        "支持她当店长。":
            $ m9_support = True
            shenlan "不会。你比我认真。"
            "她愣了一下。"
            xiaoman "……真的？"
            shenlan "本子都记了小半本了。"
            "她笑了，眼睛还是红的。"
        "劝她走。":
            shenlan "你妈说得也有道理。"
            "她低下头，把本子合上。"
            xiaoman "……嗯。"
            "她没有再说话。"

    xiaoman "老板。"
    shenlan "嗯？"
    xiaoman "如果有一天你不想开了，我可以当店长。"
    "她说完，自己先愣住了。"
    "我也愣住了。"

    menu:
        "告诉她店的事。":
            $ m9_told = True
            shenlan "……店可能要关了。"
            "她看着我，很久没有说话。"
            xiaoman "什么时候的事？"
            shenlan "月底之前。"
            xiaoman "……那你刚才还让我当店长。"
            "她的声音很轻。"
            "我没有回答。"
        "瞒着她。":
            "我没有说。"
            "我说：「好啊。」"
            "她笑了，把本子抱在怀里。"
            "那个笑让我更难受。"

    scene bg shop day with paperdissolve
    show xiaoman neutral_half at half_right with dissolve
    show luyao awkward_half at expr_left with dissolve
    "傍晚，陆遥来了。"
    "小满给他端咖啡，顺口问了一句：「陆哥，听说你找到工作了？」"
    luyao "……嗯。找到了。"
    "他说得很自然。"
    xiaoman "那挺好的。"
    "她端着托盘走了。"
    "陆遥低头喝咖啡。"
    luyao "房东最近来过吗？"
    "我看着他。"
    luyao "……随便问问。"

    $ unlock_record("notebook")
    scene black with warmfade
    "那天晚上，小满把本子落在柜台上。"
    "我没有翻，只看见封面上画着一颗歪歪的星。"
    jump scene_lease
