#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '12/10/2017'"""

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python-local-test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "insert into user (email,password) values(%s,%s)"
        cursor.execute(sql,("admin@python.org","very-secret"))
        connection.commit()

    with connection.cursor() as cursor:
        # select id,password from user where email='admin@mysql.com'
        sql = "select id,password from user where email=%s"
        cursor.execute(sql,("admin@python.org",))
        result = cursor.fetchone()
        print(result)

    with connection.cursor() as cursor:
        # select id,password from user where email='admin@mysql.com'
        sql = "update user set email=%s where password=%s"
        cursor.execute(sql,("admin@python.org","very-secret"))
        connection.commit()

    with connection.cursor() as cursor:
        sql = "delete from user where email=%s"
        cursor.execute(sql,("admin@python.org"))
        connection.commit()


finally:
    connection.close()