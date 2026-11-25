# TODO-M8: 语音、打磨与打包

## 声线

- 使用本机 Breeze-TTS 2（MLX）的 **voice design**，不用 `tts_her` 克隆。
- 每个角色先生成一条 2-6 秒的合成参考音，放在 `assets/voice_refs/`；之后所有台词用参考音 + 语气指令做 **voice direction**，保持同一条声线。
- 声线设定：
  - 沈岚：偏低、温柔的年轻女声，语速慢，气息轻，像很累但仍在照顾别人。
  - 陆遥：二十五岁普通年轻男声，放松、口语化，不磁性、不低沉，像日常和朋友说话（`c_plain_seed7`）。
  - 小满：明亮轻快的年轻女声，语速偏快，带一点笑意。
  - 房东：四十多岁中年男声，客气、实际。
  - 老周：六十多岁老年男声，慢、低、话不多。
- 参考音和 seed 记录在 `assets/voice_refs/refs.json`。

## 接入方式

- 只给角色对白配音，不给旁白配音；旁白保留阅读节奏。
- `tools/make_voice.py` 扫描 `shenlan / luyao / xiaoman / landlord / zhou` 的对白，逐句生成 `game/audio/voice/<file>_<line>.ogg`，并在对白前插入 `voice "..."`。
- 同一角色 + 同一句文本只生成一次，其余复用。
- 音频统一 `loudnorm=I=-18:TP=-1.5:LRA=11`，OGG q5。
- 生成清单：`game/audio/voice/manifest.json`。

## 待做

- [x] 生成全部 293 句对白（`game/audio/voice/`，6.0 MB）。
- [x] 插入 `voice` 语句；`voice` 与下一句对白逐条校验，0 条错位。
- [x] 陆遥声线改为 `c_plain_seed7`，重新生成 116 条。
- [x] lint 通过。
- [x] 用户试听候选，选定陆遥声线（C 自然口语 / seed7）。
- [x] 试听最终版五角色样带，确认放在一起不串。
- [x] 打包：Mac `build/ChooseLove-1.0-mac.zip`，PC `build/ChooseLove-1.0-pc.zip`；开发文件已排除出发行包。
- [ ] 用户实际通关测试（一周目 / 二周目 / 真话 / 白夜 / 底座五分支 / 星图）。
