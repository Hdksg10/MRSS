#-*- coding:utf-8 -*-
import subprocess
import time
#开一个子进程，打开蓝牙并取消pin
p = subprocess.Popen("bluetoothctl --agent=NoInputNoOutput", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#初始化蓝牙代理
p.stdin.write(bytes("default-agent\n", encoding='utf8'))
p.stdin.flush()
#设置可被发现
p.stdin.write(bytes("discoverable on\n", encoding='utf8'))
p.stdin.flush()
#设置允许配对
p.stdin.write(bytes("pairable on\n", encoding='utf8'))
p.stdin.flush()
#等待连接时间3分钟
time.sleep(180)
p.stdin.write(bytes("exit\n", encoding='utf8'))
p.stdin.flush()
print(str(p.stdout.read(), encoding='utf8'))
p.stdout.flush()
print("end")