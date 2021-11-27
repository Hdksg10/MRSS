# MEDICATION REMINDER SYSTEM FOR SENIORS
# database: SQLite 3
# Modules required: sqlite3
# -*- coding: utf-8 -*-
# Author: TOMYUE(tang yue) in DASE_ECNU 2021
import sqlite3
def fetch():
    try:
        # scan gun input the barcode of the medicine,barcode_scan is a string
        barcode_scan = input()
        # connect the database to query the medication
        conn = sqlite3.connect('medicine.db')
        cur = conn.cursor()

        sql ="SELECT rowid,* FROM medicine_chengyao WHERE Barcode='"+barcode_scan+"';"

        cur.execute(sql)
        data = cur.fetchone()
        # ---------------------------
        medication_name = data[1] # tansmit the name of the product to the TTS
        # ---------------------------
        print(data[1])
        print()
        print(data)

        conn.commit()

        conn.close()
        return medication_name

    except TypeError as error:
        # print("Error while executing:", error)
        return "None" # the medication,which not be found,will be audio boardcst the name of the medication

    finally:
        if conn:
            conn.close()
            # print("sqlite connection is closed")

