# BUILD · 满天星 1.1

## 分发文件

- Mac：`build/ChooseLove-1.1-mac.zip`（解压后得到 `ChooseLove.app`）
- Windows / PC：`build/ChooseLove-1.1-pc.zip`（解压后运行 `ChooseLove.exe`；Mac/Linux 也可用 `ChooseLove.sh`）

`build/` 不进入 git，只保留在本机。开发用文件（`assets/`、`tools/`、`docs/`、`*.md`）不会被打进发行包。

## 重新打包

```bash
cd ~/Applications/renpy-8.5.2-sdk
./renpy.sh launcher distribute /Users/jasxu/Documents/choose_love \
  --destination /Users/jasxu/Documents/choose_love/build \
  --package pc --package mac
```

## 说明

- 版本号在 `game/options.rpy` 的 `config.version`。
- 角色语音在 `game/audio/voice/`；换声线后重跑 `tools/revoice_speaker.py`，不需要重新插入 `voice` 语句。
- 当前构建未做 Apple 公证；本机直接打开即可，若从网络下载后被 Gatekeeper 拦截，右键「打开」。
- 还没做实际运行通关测试；测试清单见 `TODO-M8.md`。

## Android APK（GitHub Actions）

- 仓库：<https://github.com/Ye-Yu-Mo/choose-love-vn>
- 工作流：`.github/workflows/android.yml`
- 打开 Actions → Build Android APK → Run workflow；跑完在 Artifacts 里下载 `ChooseLove-1.1-apk`。
- 包名：`com.yeyumo.chooselove`；图标：`game/android-icon_foreground.png` / `background.png`。
- CI 里会生成一个临时 debug 签名 keystore，不会提交。
