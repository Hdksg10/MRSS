# Medicine Infomation Spider
# Spider: requests
# parser: XPath
# database: ?
# Modules required: requests,lxml,(database connection)
# -*- coding: utf-8 -*-
# author:Ghostlikei from DASE_ECNU 2021

import requests
from lxml import etree
import time
import sqlite3


class Medicine:
    def __init__(self):
        self.head = "https://www.315jiage.cn/"
        self.user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        self.headers = {
            "User-agent": self.user
        }
        self.flag = 0
        self.failed_num = 0
        self.conn = sqlite3.connect('medicine.db')
        self.cur = self.conn.cursor()


    def get_data(self, type, page):
        self.flag = 0
        url = f"https://www.315jiage.cn/mc{type}p{page}.aspx"
        response = requests.get(url, headers=self.headers, timeout=30)
        self.content = response.content.decode("utf-8")
        html = etree.HTML(self.content)
        if html.xpath("//head/title/text()")[0][0] == "您":
            self.flag += 1
            return
        results = html.xpath("""//div[@class="col-2"]/a[@target="_blank"]/@href""")
        print(f"Browsing page {page}")
        count = 0
        for each_id in results:
            try:
                new_url = self.head + each_id
                resp = requests.get(new_url, headers=self.headers)
                content = resp.content.decode("utf-8")
                ehtml = etree.HTML(content)

                info = {}

                name = ehtml.xpath("""//span[@itemprop="name"]/text()""")[0]
                info["产品名称"] = name

                base_info = ehtml.xpath("""//div[@class = "block-info-prop text-oneline"]//text()""")
                titles = ['规格：', '剂型：', '包装单位：', '批准文号：', '生产厂家：', '条形码：', '主治疾病：']
                for each in base_info:
                    if each in titles:
                        if each == '规格：' or each == '剂型：':
                            for every_info in base_info[base_info.index(each) + 1:]:
                                if every_info in titles:
                                    break
                                else:
                                    info[each[:-1]] = every_info[:-3]
                                    break
                        elif each == '主治疾病：':
                            for every_info in base_info[base_info.index(each) + 1:]:
                                if every_info in titles:
                                    break
                                else:
                                    illness = ""
                                    info[each[:-1]] = illness.join(every_info.replace("\xa0", "").split())
                                    break
                        else:
                            for every_info in base_info[base_info.index(each) + 1:]:
                                if every_info in titles:
                                    break
                                else:
                                    info[each[:-1]] = every_info
                                    break
                info["主治疾病"]="测试"
                info["批准文号"] = ehtml.xpath("//td/div/u/a/text()")[0]

                info["是否处方"] = bool(ehtml.xpath("""//td/div/span[@class="cRed"]"""))

                temp = ehtml.xpath("""//ul[@class="property"]//text()""")
                contents = []
                for content in temp:
                    if content not in contents:
                        contents.append(content)

                contents.pop(contents.index(" "))

                # info["说明书"] = contents
                SMS = ""

                info["说明书"] = SMS.join(contents)

                count += 1
                print(f"Saving infomation {page}-{count}")
                time.sleep(0.65)
                # All infomation has been downloaded and preprocessed!
                # -----------------------------------------
                print(info)
                try:
                    self.cur.execute("INSERT INTO medicine_chengyao VALUES(?,?,?,?,?,?,?,?,?,?)",
                                     (info.get("产品名称", "NULL"), info.get("规格", "NULL"), info.get("剂型", "NULL"),
                                      info.get("包装单位", "NULL"), info.get("生产厂家", "NULL"),
                                      info.get("条形码", "NULL"), info.get("主治疾病", "NULL"), info.get("批准文号", "NULL"),
                                      info.get("是否处方", "NULL"), info.get("说明书", "NULL")))
                    self.conn.commit()
                except(sqlite3.Error):
                    self.conn.rollback()
                    print("saving error!")
                # 'info' is going to be saved in one database
                # Writing saving codes below......
            except(IndexError,requests.HTTPError,TimeoutError,requests.exceptions.ConnectionError):
                print("Failed to download data!")
                self.failed_num += 1
                continue




def main():
    medicine = Medicine()
    types = [118, 119, 131]
    a = [119]
    for type in a:
        for i in range(0,5000):
            medicine.get_data(type, i + 1)
            time.sleep(0.1)
            if medicine.flag == 1:
                break
    print("下载失败的条目数量：", medicine.failed_num)
    medicine.conn.close()


if __name__ == "__main__":
    main()
