# ASSETS · 满天星

## 基本规范

- 分辨率 1280x720；所有全屏背景/CG 都裁成 16:9 再缩到 1280x720。
- 字体：`game/fonts/SourceHanSansLite.ttf`，**缺 U+00B7（·）**，章节/结局标题统一用「—」；也缺 ★☆，星图星星是 PNG 贴图，不要用字符。
- 图片名可以带空格，但不能用 Ren'Py 关键字（例如 `with`）；`cg ending with him` 会解析失败，已改成 `cg ending depart`。
- 对话立绘：`expr_left` / `expr_right`（zoom 0.32）；小图半身：`half_left` / `half_right`（zoom 0.40）。
- 记忆物件统一画布 560x560，星图里直接叠加。

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
| `bg shop day` | `images/bg shop day.png` | 已有 |
| `bg shop night` | `images/bg shop night.png` | 已有 |
| `bg back room` | `images/bg back room.png` | 已有 |
| `bg piano corner` | `images/bg piano corner.png` | 已有 |
| `bg street rain` | `images/bg street rain.png` | 已有 |
| `bg starry sky` | `images/bg/bg_starry_sky.png` | 已有（星图） |

## CG

| 名称 | 文件 | 用途 |
|---|---|---|
| `cg piano lesson` | `images/cg piano lesson.png` | 教琴全景 |
| `cg 347` | `images/cg/cg_347.png` | 凌晨 3:47，陆遥睡在柜台 |
| `cg shenlan piano` | `images/cg shenlan piano.png` | 沈岚弹琴 |
| `cg luyao piano` | `images/cg luyao piano.png` | 陆遥学琴 |
| `cg ending together` | `images/cg/ending_together.png` | 一起开 |
| `cg ending xiaoman` | `images/cg/ending_xiaoman.png` | 朋友一个人开 |
| `cg ending depart` | `images/cg/ending_with_him.png` | 她和他走 |
| `cg ending alone` | `images/cg/ending_alone.png` | 没有回头 |
| `cg ending funeral` | `images/cg/ending_funeral.png` | 完成葬礼 |
| `cg ending together`（冷色调复用） | `images/cg/ending_together.png` | 白夜（暂不新出图） |
| `cg ending told`（待生成） | `images/cg/cg_ending_told.png` | 如果那天我说了；暂用 `cg ending together` + 柔光占位 |

## 立绘

| 角色 | 表情 | 备注 |
|---|---|---|
| 沈岚 | neutral / tired / quiet / hurt / angry | 半身，透明底 |
| 陆遥 | neutral / awkward / guilty / sad | 半身，透明底，眼镜 |
| 小满 | neutral / worried / pout / crying / kneel | 半身，透明底 |

源图在 `game/images/sprites/raw/`，处理后的成品在 `game/images/sprites/`。

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

信封+钥匙、兔子、纸星星、模型、手机、琴盖、咖啡、钥匙、车票、花束、螺丝刀、猫、书、伞、本子、租约、笔记本电脑，共 17 个，统一 560x560，文件在 `game/images/mem/`。

## 待补资源（按 PLAN Milestone 1）

- 记录 9 所需的背景/道具：小满的本子。猫（年糕）直接复用 `mem cat` + `cat_sit` 变换。
- 记录 10–11 的 CG 或特写（3:47 的屏幕、睡着的陆遥）。
- 老周、房东、阿哲的立绘（或先用剪影/背影）。