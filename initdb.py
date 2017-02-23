#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@python_version: python_x86 3.5.2
@site: octowahle@github
@software: PyCharm Community Edition
@file: initdb.py
@time: 2017/2/23 12:13
"""

import os
import sys
import sqlite3


def init_db(dbname, sqlfile):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    with open(sqlfile, mode='r') as f:
        cursor.executescript(f.read())
        conn.commit()
    conn.close()


def main():
    pass


if __name__ == '__main__':
    main()
