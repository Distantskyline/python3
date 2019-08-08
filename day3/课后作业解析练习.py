#!/usr/bin/env python3
#
#date:
#author:
#usage:
#
# 1.统计kingdoms.txt中"曹操"、"刘备"、"卧龙"、"孙权"各出现的次数？并将其生成字典持久化存储
# 2.统计kingdoms.txt中"青龙偃月刀"、"丈八蛇矛"、"赤兔马"、"雌雄双股剑"各出现的次数？并将其生成字典持久化存储
# 3.请将上述生成的两个字典,按照其中的出现次数进行从大到小排序？
# 4.请将上述的字典生成json格式的数据,并保存至文件中
# 5.请统计access_log中访问量前十的IP地址,并生成json格式数据,保存至文件中.(用python代码实现)
# 6.请统计access_log中所有的状态码(200, 404, 502, 503)各自出现的数量,并把统计好的数据json格式化,存储到文件中
# 7.请统计access_log中访问最大的资源,前十名,并把统计好的数据json格式化,存储到文件中(被访问资源如下所示)
# 185.173.224.24 - - [30/Jun/2019:11:48:52 +0800] "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" 404 0 "-" "-" "-"
# "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" - 这就是被访问的资源整体(包括了请求方法、所用协议)
# /wordpress/wp-includes/wlwmanifest.xml - 这就是其中的资源

name,dict01 = ('曹操','刘备','卧龙','孙权'),{}
with open(file='./txtFile/kingdoms.txt',mode='r',encoding='utf8') as file01:
    wenzhang = file01.read()
    wenzhang01 = wenzhang.replace(' ','').replace('\n','')
    for name in name:
        dict01.setdefault(name,wenzhang01.count(name))
    print(dict01)

import json
with open(file='./txtFile/json存储.json',mode='w',encoding='utf8') as file02 :
    json.dump(dict01,file02,ensure_ascii=False)

name02,dict02 = ('青龙偃月刀','丈八蛇矛','赤兔马','雌雄双股剑'),{}
with open(file='./txtFile/kingdoms.txt',mode='r',encoding='utf8') as file:
    wz = file.read()
    wz1 = wz.replace(' ','').replace('\n','')
    # print(wz1)
    for name02 in name02:
        dict02.setdefault(name02,wz1.count(name02))
    print(dict02)
with open(file='./txtFile/json存储.json',mode='a',encoding='utf8')as file:
    file.write('\n')
    json.dump(dict02,file,ensure_ascii=False)
print(type(dict02))

# # 3.请将上述生成的两个字典,按照其中的出现次数进行从大到小排序？

print(type(dict01))

with open(file='./txtFile/json存储.json',mode='r',encoding='utf8')as file:
    for lines in file.readlines():
        abc = json.loads(lines)
        print(abc)