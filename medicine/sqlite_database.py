# MEDICATION REMINDER SYSTEM FOR SENIORS
# database: SQLite 3
# Modules required: sqlite3
# -*- coding: utf-8 -*-
# Author: TOMYUE(tang yue) in DASE_ECNU 2021
import sqlite3

try:
    conn = sqlite3.connect("medicine.db")

    sql_query_1 = '''CREATE TABLE medicine_chengyao(
                    Products_name TEXT,
                    Specfications TEXT,
                    Formulation TEXT ,
                    Packing_unit TEXT ,
                    Company TEXT ,
                    Barcode TEXT ,
                    Main_treat_disease TEXT ,
                    Approval_number TEXT ,
                    OTC_test TEXT ,
                    Instructions TEXT);
                    '''
    cur = conn.cursor()
    print("Successfully Connected to SQLite")
    print()

    cur.execute(sql_query_1)
    conn.commit()
    print("SQLite table created")

    cur.close()

except sqlite3.Error as error:
    print("Error while executing:", error)

finally:
    if conn:
        conn.close()
        print("sqlite connection is closed")



