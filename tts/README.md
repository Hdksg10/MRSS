# MRSS
## 文字转语言模块

### 使用

- 运行

  ```
  ./sound.py
  ```

  输入全中文字符串，正常会完成合成并播放。

  合成文件保存为./demo.wav

  代码封装在./tts.py文件内，调用方法:

  ```
  import tts
  tts.say(string)
  ```

  注:string必须为全中文字符串。
