# TensorflowTTS on ARM

该demo已经在树莓派4b上通过测试，使用时需删除build文件夹并重新使用cmake构建

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