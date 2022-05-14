# Medication reminder system for seniors

## 基于SQL与TTS技术的视障人士用药辅助提醒系统

## 背景

本项目基于SQLlite存储药品数据，借助[TensorflowTTS](https://github.com/TensorSpeech/TensorFlowTTS)模型实现文字转语音功能。

~~该demo目前仅在Windows-x64与Linux-x64平台上完成运行，尚未移植到IoT平台。~~

tts_on_raspberry已经在树莓派4b(armv7l)上通过测试

## 安装(基于tts_on_raspberry)

### 需求：

- numpy==1.21.4
- scipy==1.7.3
- scikit-learn==1.0.1

- SoundFile==0.10.3.post1
- numba==0.48.0
- llvmlite==0.31.0
- librosa==0.8.1

使用pip安装上述包。

注意：在安装llvmlite之前，需要先安装LLVM

```bash
sudo apt-get install llvm7
```

### 构建：

./tts_on_raspberry/build 目录是在Linux-x64下的demo，构建前需要删除。

```bash
cd ./tts_on_raspberry
sudo rm -r build
mkdir build
cd build
cmake .. -DMAPPER=BAKER
make
```

### 使用：

```bash
./demo "你好#3世界" hello.wav
```

输出音频文件会保存在build目录下。

在输入字符串中插入#3可以制造停顿。
