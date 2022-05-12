import os
import re

import fetchinfo

def listenBarCode() -> str:
    medicineName = fetchinfo.fetch()
    pattern = (re.sub("\\(.*\\)", "", medicineName))
    pattern.rstrip()
    res = ''.join(re.findall('[\u4e00-\u9fa5]',pattern))
    print(res)
    #print(pattern) 
    print(f"{res}")
    waveFile = res+".wav"
    print(res)
    os.system("cd ../tts_on_raspberry/build/ && ./demo {} med.wav".format("\"#3"+res+"#3\""))
    os.system("play ../tts_on_raspberry/build/med.wav ")

while True:
    os.system("rm ../tts_on_raspberry/build/med.wav")
    listenBarCode()