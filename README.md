# Medication reminder system for seniors

## 基于SQL与TTS技术的视障人士用药辅助提醒系统

## 背景

本项目基于SQLlite存储药品数据，借助[TensorflowTTS](https://github.com/TensorSpeech/TensorFlowTTS)模型实现文字转语音功能。

该demo目前仅在Windows-x64与Linux-x64平台上完成运行，尚未移植到IoT平台。

TTS_on_ARM理论上可在树莓派4b(ARMv7l架构)上使用，尚未通过测试。

## 安装

由于github文件存储大小限制，使用前需先解压`./tts/tacotron2.zip`

### 依赖

- Tensorflow>=2.4.0
- TensorflowTTS
- 
