#!/usr/bin/env python3
#
#author:Distantskyline
#date:190822-11:34
#usage:


##                                      mysql 建立连接
import pymysql

# client = pymysql.connect(
#     host='192.168.52.133',
#     user='zgh',
#     password='(123!@#)',
#     db='grade'
# )
# cursors = client.cursor()
# with open(file='grade.txt', mode='r', encoding='utf8') as file:
#     id = 0
#     for lines in file.readlines():
#         name, oldgrade, newgrade, gradecha = lines.split()
#         sql = "insert into grade values ({}, '{}', {}, {}, {});"
#         id += 1
#         cursors.execute(sql.format(id, name, int(oldgrade), int(newgrade), int(gradecha)))
# client.commit()
# client.close()

##                                 从mysql里读取数据出来，默认元组，增加参数为字典
client = pymysql.connect(
    host='192.168.52.133',
    user='zgh',
    password='(123!@#)',
    db='grade',
    cursorclass=pymysql.cursors.DictCursor     ##什么也不写的时候为默认元组，现在是字典
)
try:
    cursors = client.cursor()
    sql = "select * from {}"
    cursors.execute(sql.format('grade'))
    result = cursors.fetchall()
    print(result)
finally:
    client.close()