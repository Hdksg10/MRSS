# MEDICATION REMINDER SYSTEM FOR SENIORS
# database: SQLite 3
# Modules required: sqlite3
# -*- coding: utf-8 -*-
# Author: TOMYUE(tang yue) in DASE_ECNU 2021
import sqlite3
import sqlite_database

def show_all(info):
# connect to a database
    conn=sqlite3.connect('medicine.db')
# Create a cursor
    cur = conn.cursor()
# Query the database
    cur.execute("SELECT rowid,*FROM medicine_chengyao")
    items = cur.fetchall()
    for item in items:
        print(item)

# commit my command
    conn.commit()
# close our connect
    conn.close()

def add_one(info):
    conn = sqlite3.connect('medicine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO medicine_chengyao VALUES(?,?,?,?,?,?,?,?,?,?)",
                (info.get("产品名称", "NULL"), info.get("规格", "NULL"), info.get("剂型", "NULL"), info.get("包装单位", "NULL"),
                 info.get("生产厂家", "NULL"),
                 info.get("条形码", "NULL"), info.get("主治疾病", "NULL"), info.get("批准文号", "NULL"), info.get("是否处方", "NULL"),
                 info.get("说明书", "NULL")))
    conn.commit()
    conn.close()


def add_many(info):
    conn = sqlite3.connect('medicine.db')
    cur= conn.cursor()
    cur.executemany("INSERT INTO medicine_chengyao VALUES(?,?,?,?,?,?,?,?,?,?)",(info.get("产品名称","NULL"),info.get("规格","NULL"),info.get("剂型","NULL"),info.get("包装单位","NULL"),info.get("生产厂家","NULL"),
                                                                               info.get("条形码","NULL"),info.get("主治疾病","NULL"),info.get("批准文号","NULL"),info.get("是否处方","NULL"),info.get("说明书","NULL")))
    conn.commit()
    conn.close()

def delete_select_item(info):
    conn = sqlite3.connect('medicine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM medicine_chengyao WHERE Barcode=(?)",info["条形码"])
    conn.commit()
    conn.close()

def delete_all(info):
    conn = sqlite3.connect('medicine.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE medicine_chengyao")
    conn.commit()
    conn.close()


