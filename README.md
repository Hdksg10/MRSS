# Medication reminder system for seniors

## 基于SQL与TTS技术的视障人士用药辅助提醒系统

## 背景

本项目基于SQLlite存储药品数据，借助[TensorflowTTS](https://github.com/TensorSpeech/TensorFlowTTS)模型实现文字转语音功能。

已经在树莓派4b(armv7l)上通过测试

## 内容

- 在树莓派上部署的TensorflowLite模型(Fastspeech2 & MulitbandMelGan)
- 在树莓派上部署的SQLite及相关API
- 树莓派蓝牙控制，与智能手机连接，信息传输