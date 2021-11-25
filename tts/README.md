# MRSS
## 文字转语言模块

### 安装

- 使用Annaconda创建新的虚拟环境

  ```
  conda create ttsdemo
  ```

- 安装TensorflowTTS

  ```
  cd ./TensorflowTTs
  python ./setup.py install
  ```

  

### 使用

- 解压./tacotron2.zip

- 运行

  ```
  conda activate ttsdemo
  python ./sound.py
  ```

  输入全中文字符串，正常会完成合成并播放。

  合成文件保存为./demo.wav

  代码封装在./tts.py文件内。

- 调用

  ```
  import tts
  tts.say(string)
  ```

  注:string必须为全中文字符串。

## Text to Sound Module

### Install

- Create a virtual environment by Annaconda

  ```
  conda activate ttsdemo
  ```

- Install TensorflowTTS

  ```
  cd ./TensorflowTTs
  python ./setup.py install
  ```

### Usage

- Unzip ./tacotron2.zip

- Run

  ```
  conda activate ttsdemo
  python ./sound.py
  ```

  The input characters must be CHINESE.

  Normally, the file will be saved as ./demo.wav

  The  code is in ./tts.py
  
- APIs

  ```
  import tts
  tts.say(string)
  ```
  
  String must be FULL-CHINESE
