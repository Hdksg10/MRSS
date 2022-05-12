#-*- coding:utf-8 -*-
import time
import os
class wlanprofile(object):
    def __init__(self, ssid, pwk) -> None:
        self.ssid = ssid
        self.pwk = pwk
    #获取wifi的ssid
    def getssid(self, ssid):
        self.ssid = ssid
    #获取wifi密码
    def getpwk(self, pwk):
        self.pwk = pwk
    #设置wifi并检查是否联网
    def setwlan(self) -> bool:
        #向树莓派配置中写入wifi
        wpa_config = open("/etc/wpa_supplicant/wpa_supplicant.conf", mode='a+')
        config = f"""network={{
	ssid="{self.ssid}"
	psk="{self.pwk}"
	priority=10
}}\n"""
        wpa_config.write(config)
        wpa_config.close()
        #重载配置
        os.system("wpa_cli -i wlan0 reconfigure")
        #等待重载时间180s
        time.sleep(180)
        #ping一下测试网络连通性
        exit_code = os.system("ping www.baidu.com -c 10")
        if( exit_code == 0):
            return True
        else:
            return False