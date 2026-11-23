# 选择爱 · 制作笔记

用 Ren'Py 做的视觉小说。剧本、素材、打包全在这一个文件夹里。

## 目录结构

```
choose_love/
├── game/
│   ├── script.rpy       ← 剧本入口（label start 从这里开始）
│   ├── story/           ← 自己新建的分章剧本，放 .rpy 文件即可自动加载
│   ├── options.rpy      ← 游戏名、版本号、存档目录等配置
│   ├── gui.rpy          ← 界面配色、字体、字号
│   ├── screens.rpy      ← 对话框、主菜单、存读档界面
│   ├── images/          ← 背景 / 立绘 / CG
│   ├── audio/           ← 音乐 / 音效
│   └── gui/             ← 界面用的图片素材
└── NOTES.md             ← 这个文件
```

## 怎么运行

```bash
~/Applications/renpy-8.6.2-sdk/renpy.sh ~/Documents/choose_love
```

想改完立刻看到效果：游戏窗口开着时按 `Shift+R` 重载脚本，不用重启。

## 剧本速查

| 写法 | 含义 |
|---|---|
| `label 名字:` | 一个剧情节点，用 `jump 名字` 跳过去 |
| `"旁白文字"` | 不带名字的旁白 |
| `me "台词"` | 角色说话 |
| `menu:` + 选项 | 分支选择 |
| `$ 变量 = 值` | 记录选择结果（好感、flag） |
| `if 条件:` | 根据变量走不同剧情 |
| `scene bg 名字 with fade` | 换背景 |
| `show 角色 at center` | 显示立绘 |
| `play music "xxx.ogg"` | 放音乐 |
| `renpy.input("你叫什么？")` | 让玩家输入名字 |

## 素材放法

- 背景图放 `game/images/bg_咖啡店.png`，剧本里写 `scene bg 咖啡店`
- 立绘放 `game/images/她_微笑.png`，剧本里写 `show 她_微笑`
- 音乐放 `game/audio/theme.ogg`，剧本里写 `play music "audio/theme.ogg"`
- 中文已配置思源黑体，不会出现方块字

## 打包送人

Ren'Py 启动器里选项目 → `Build Distributions` → 勾选 PC (Windows/Mac/Linux)。
生成的 zip 发给对方，解压双击就能玩，不用装任何东西。

## 待办

- [ ] 确定故事设定和主角名字
- [ ] 写第一章剧本
- [ ] 找/画背景和立绘
- [ ] 加好感度分支和多结局
- [ ] 做「回忆相册」收集
- [ ] 加音乐
