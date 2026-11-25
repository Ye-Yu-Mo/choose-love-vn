# ASSETS · 满天星

## 基本规范

- 分辨率 1280x720；所有全屏背景/CG 都裁成 16:9 再缩到 1280x720。
- 字体：`game/fonts/SourceHanSansLite.ttf`，**缺 U+00B7（·）**，章节/结局标题统一用「—」；也缺 ★☆，星图星星是 PNG 贴图，不要用字符。
- 图片名可以带空格，但不能用 Ren'Py 关键字（例如 `with`）；`cg ending with him` 会解析失败，已改成 `cg ending depart`。
- 对话立绘统一用半身表情差分：`expr_left` / `expr_right`（zoom 0.32）。小满的 `neutral_bust` 与 `worried/pout/crying` 同一构图，避免全身→半身跳变。
- 记忆物件统一画布 1024x1024，星图里直接叠加。

## 工具链

| 脚本 | 用途 |
|---|---|
| `tools/gen_images.py` | 文生图批量出图（manifest + 并发） |
| `tools/gen_edits.py` | 参考图改表情/姿势（透明底） |
| `tools/process_sprites.py` | 立绘去边、裁切、1.5x、锐化 |
| `tools/process_cgs.py` | CG 裁 16:9、缩到 1280x720 |
| `tools/process_memories.py` | 记忆物件裁切、统一 560 画布 |
| `tools/make_star.py` | 生成星图点亮/未点亮星星 |
| `tools/make_paper_ui.py` | 生成暗角、纸质按钮、翻页遮罩 |
| `tools/make_documents.py` | 程序化生成邮件、租约、offer、信、本子、3:47 屏幕 |
| `tools/make_object_props.py` | 程序化生成菜单板、转让牌、咖啡+纸星静物 |
| `tools/remove_transfer_sign.py` | 生成无「转让」牌的店铺背景变体 |

## 音乐

### 已有

| 文件 | 时长 | 用途 |
|---|---|---|
| `audio/piano_touch_the_starlight.ogg` | 0:57 | **只在女主弹琴时**（教琴、结局回忆）；Funton - Touch the starlight，从 NCM 解码 |

### 新入库（已转 OGG，-18 LUFS，已接入脚本，待试听微调）

源文件在 `assets/audio_src/new_tracks/`，成品在 `game/audio/bgm/`。

| 文件 | 原名 | 时长 | 类型 | 建议场景 |
|---|---|---|---|---|
| `rain_air.ogg` | 春野杉卉 - 雨に濡れた空気 | 2:34 | 纯音乐 | 雨天日常、葬礼开场、雨里的伞、门口 |
| `autumn_sleep.ogg` | MoreanP - 暮秋沉眠 | 3:13 | 纯音乐 | 深夜、凌晨 3:47、底座解谜、琴盖合上 |
| `qingyi_piano.ogg` | 九鸢Pro,在下河帛 - 青衣（Piano Solo） | 2:29 | 钢琴独奏 | 模型葬礼、完成葬礼、告别 |
| `sunset_galaxy.ogg` | 赵大鼾 - 落日星河不及你 | 3:18 | 纯音乐 | 一起开、星图、结局后的余韵 |
| `love_letter.ogg` | やなぎなぎ - 恋文 | 6:28 | 日文歌曲 | 片尾/真结局/她和他走（有歌词，慎用，建议只放一次） |

> 已按上表接入：`game/audio.rpy` 的 `BGM` 字典 + `bgm()`。试听后如果哪首不合适，改字典里的映射即可。

## 背景

| 名称 | 文件 | 状态 |
|---|---|---|
| `bg shop day` | `images/bg shop day.png` | 已有；`sign_removed` 后切无牌变体 |
| `bg shop night` | `images/bg shop night.png` | 已有；`sign_removed` 后切无牌变体 |
| `bg back room` | `images/bg back room.png` | 已有 |
| `bg piano corner` | `images/bg piano corner.png` | 已有 |
| `bg street rain` | `images/bg street rain.png` | 已有 |
| `bg starry sky` | `images/bg/bg_starry_sky.png` | 已有（星图） |
| `bg shop day no sign` | `images/bg shop day no sign.png` | 已生成（记录 4 摘牌后） |
| `bg shop night no sign` | `images/bg shop night no sign.png` | 已生成（记录 4 摘牌后） |

## CG

| 名称 | 文件 | 用途 |
|---|---|---|
| `cg piano lesson` | `images/cg piano lesson.png` | 教琴全景（沈岚短发已对齐立绘） |
| `cg 347` | `images/cg/cg_347.png` | 凌晨 3:47，陆遥睡在柜台（无挂钟，咖啡为美式） |
| `cg base inside` | `images/cg/cg_base_inside.png` | 底座内部：钥匙 + 信（蓝色墓园纸盒，与道具一致） |
| `cg ending together` | `images/cg/ending_together.png` | 一起开（模型已统一为蓝色墓园纸盒） |
| `cg ending xiaoman` | `images/cg/ending_xiaoman.png` | 朋友一个人开（架上的模型已统一为蓝色墓园纸盒） |
| `cg ending depart` | `images/cg/ending_with_him.png` | 她和他走（沈岚发型已对齐立绘） |
| `cg ending alone` | `images/cg/ending_alone.png` | 没有回头（沈岚造型已对齐立绘） |
| `cg ending funeral` | `images/cg/ending_funeral.png` | 完成葬礼（模型已统一为蓝色墓园纸盒） |
| `cg ending together`（冷色调复用） | `images/cg/ending_together.png` | 白夜（暂不新出图） |
| `cg ending told` | `images/cg/cg_ending_told.png` | 如果那天我说了（三个人在柜台，清晨；模型已改为墓园） |
| `cg coffee star` | `images/cg/cg_coffee_star.png` | 美式 + 纸星近景（记录 2） |
| `cg exhibition` | `images/cg/cg_exhibition.png` | 小展：模型、纸星罐、星图册（一起开 / 朋友一个人开） |

## 文档 / 屏幕特写（程序化生成）

| 名称 | 文件 | 用途 |
|---|---|---|
| `prop layoff mail` | `images/props/layoff_mail.png` | 裁员邮件（记录 2、二周目序章） |
| `prop lease doc` | `images/props/lease_doc.png` | 续约合同（记录 10） |
| `prop offer letter` | `images/props/offer_letter.png` | 录用通知书（二周目记录 9） |
| `prop letter xiaoman` | `images/props/letter_xiaoman.png` | 底座里给小满的信 |
| `prop letter luyao` | `images/props/letter_luyao.png` | finale 柜台上没有署名的信 |
| `prop screen 347` | `images/props/screen_347.png` | 3:47 店铺后台 |
| `prop notebook page` | `images/props/notebook_page.png` | 小满的本子 |
| `prop menu board` | `images/props/menu_board.png` | 菜单（美式 18 / 拿铁 22 / 手冲 28） |
| `prop transfer sign` | `images/props/transfer_sign.png` | 玻璃门上的「转让」牌 |

> `prop coffee star` 与 `cards.rpy` 的头像卡系统已移除；咖啡近景统一用 `cg coffee star`。

> 这些图由 `tools/make_documents.py` 生成，中文由 `SourceHanSansLite.ttf` 渲染，避免 AI 出字糊字。数字以上海陆家嘴 2025 年租金/薪资为参考：58 平方米、原租 10,000 → 续租 18,000，offer 32,000×15 薪，N+1 约 96,000。

## 立绘

| 角色 | 表情 | 备注 |
|---|---|---|
| 沈岚 | quiet / hurt / angry | 半身，透明底；对话统一用半身 |
| 陆遥 | awkward / guilty / sad / warm / quiet | 半身，透明底，眼镜 |
| 小满 | neutral_bust / worried / pout / crying | 半身，透明底；neutral_bust 与表情同一构图 |
| 房东 | neutral_half | 半身，夹着文件袋 |

源图在 `game/images/sprites/raw/`，处理后的成品在 `game/images/sprites/`。

## 语音

- 引擎：Breeze-TTS 2（MLX，本机），voice design + voice direction，**不用 `tts_her` 克隆**。
- 参考音：`assets/voice_refs/`（沈岚 / 陆遥 / 小满 / 房东 / 老周各一条合成参考音，seed 42）。
- 生成脚本：`tools/make_voice.py`；只给角色对白配音，旁白不配音。
- 成品：`game/audio/voice/<file>_<line>.ogg`，清单 `game/audio/voice/manifest.json`，统一 -18 LUFS。
- 生成时在对白前插入 `voice "..."`；同一角色 + 同一句文本复用同一段音频。

## UI / 星图

| 文件 | 用途 |
|---|---|
| `images/ui/paper_tag_idle.png` / `hover` | 主菜单按钮、选项按钮、名字牌 |
| `images/ui/paper_window.png` | 对话框纸张 |
| `images/ui/paper_card.png` | 章节卡纸片 |
| `images/ui/paper_card_small.png` | 时间卡纸片 |
| `images/ui/vignette.png` | 主菜单暗角 |
| `images/ui/menu_left_shade.png` | 主菜单左侧压暗 |
| `images/ui/paper_mask.png` | `paperdissolve` 翻页转场 |
| `images/ui/star_lit.png` / `star_dim.png` | 星图星星 |
| `images/ui/glow_warm.png` | 记忆物件暖光晕 |

## 记忆物件（星图）

信封+钥匙、兔子、纸星星、模型、手机、琴盖、咖啡、钥匙、车票、花束、螺丝刀、猫、书、伞、本子、租约、笔记本电脑，共 17 个，统一 1024x1024，文件在 `game/images/mem/`。

## 待补资源（按 PLAN Milestone 1）

- 记录 9 所需的背景/道具：小满的本子。猫（年糕）直接复用 `mem cat` + `cat_sit` 变换。
- 记录 10–11 的 CG 或特写（3:47 的屏幕、睡着的陆遥）。
- 老周、房东、阿哲的立绘（或先用剪影/背影）。