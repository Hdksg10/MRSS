import os
import pipes
import threading
import re

def listenBarCode() -> str:
    medicineName = input()
    pattern = str(re.sub("\\(.*\\)", "", medicineName))
    #print(pattern) 
    print(f"{pattern}")
    os.system(f"./demo {pattern} {pattern}.wav")
    os.system(f"play {pattern}.wav")


listenBarCode()