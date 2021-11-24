#采用多进程方式合成并播放语言，提高在多核机器上的运行速度
import multiprocessing  #多进程包
import tts
mysql = {'1234' : [0, '复方', '厄贝沙坦', '片', '', '']}
info = []
if True:
    drug = input()
    info = mysql[drug]
    if __name__ == '__main__':
        p1 = Process(target=tf.say, args=(info[1],))
        p2 = Process(target=tf.say, args=(info[2],))
        p3 = Process(target=tf.say, args=(info[3],))