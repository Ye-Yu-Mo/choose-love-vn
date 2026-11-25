# TODO-M8: 语音、打磨与打包

## 声线

- 使用本机 Breeze-TTS 2（MLX）的 **voice design**，不用 `tts_her` 克隆。
- 每个角色先生成一条 2-6 秒的合成参考音，放在 `assets/voice_refs/`；之后所有台词用参考音 + 语气指令做 **voice direction**，保持同一条声线。
- 声线设定：
  - 沈岚：偏低、温柔的年轻女声，语速慢，气息轻，像很累但仍在照顾别人。
  - 陆遥：温和低沉的年轻男声，语速中等，克制，咬字清楚。
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

- [ ] 生成全部 293 句对白。
- [ ] lint 通过。
- [ ] 用户试听三条声线，确认不像 AI、角色可区分。
- [ ] 如需调整：改 `assets/voice_refs/refs.json` 的 instruct 或 seed，重新生成对应角色。
- [ ] 打包：Mac/Windows 构建、存档说明、制作名单。
