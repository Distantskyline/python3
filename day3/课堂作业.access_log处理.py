#!/usr/bin/env python3
#
#date:
#usage:
#author:

# 5.请统计access_log中访问量前十的IP地址,并生成json格式数据,保存至文件中.
# (用python代码实现)
# 6.请统计access_log中所有的状态码(200, 404, 502, 503)各自出现的数量,
# 并把统计好的数据json格式化,存储到文件中
# 7.请统计access_log中访问最大的资源,前十名,并把统计好的数据json格式化,
# 存储到文件中(被访问资源如下所示)

# 185.173.224.24 - - [30/Jun/2019:11:48:52 +0800] "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" 404 0 "-" "-" "-"
# "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" - 这就是被访问的资源整体(包括了请求方法、所用协议)
# /wordpress/wp-includes/wlwmanifest.xml - 这就是其中的资源


# 170.83.202.0 - - [30/Jun/2019:03:19:51 +0800] "GET / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7" "-"
# 167.71.176.25 - - [30/Jun/2019:04:22:30 +0800] "HEAD / HTTP/1.1" 200 0 "https://www.netcraft.com/survey/" "Mozilla/4.0 (compatible; Netcraft Web Server Survey)" "-"
# 88.248.13.15 - - [30/Jun/2019:04:43:20 +0800] "GET / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36" "-"
# 27.147.187.158 - - [30/Jun/2019:05:14:15 +0800] "GET / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36" "-"
# 101.132.151.69 - - [30/Jun/2019:05:32:47 +0800] "GET /TP/public/index.php HTTP/1.1" 404 27 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6)" "-"
# 101.251.242.238 - - [30/Jun/2019:05:54:53 +0800] "GET / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0" "-"

# with open(file='./txtFile/hardwareInfo.json', mode='w', encoding='utf8') as file:
#     file.write(json.dumps(info))
#
# with open(file='./txtFile/hardwareInfo.json', mode='r', encoding='utf8') as file:
#     content = file.read()
#     print(content, type(content))
#     dictA = json.loads(content, encoding='utf8')
#     print(dictA, type(dictA))

import json
with open(file='./txtFile/access_log',mode='r',encoding='utf8')as file:
    hang = file.readlines()
    list01,dict01 = [], {}
    for n in hang:
        hang_ip=n.split('- -')[0].rstrip()
        list01.append(hang_ip)
    for x in list01:
        y = list01.count(x)
        dict01[x] = y
dict02,list02= {},[]
for i in dict01.items():
    list02.append(i[1])
list02.sort()
list02.reverse()
for q in list02:
    for p in dict01.items():
        if q == p[1]:
            dict02[p[0]] = q
answer = dict(list(dict02.items())[:10])
print(answer)
with open(file='./txtFile/前十个IP.txt',mode='w',encoding='utf8')as file1:
    file1.write(json.dumps(answer,ensure_ascii=False))





#状态码处理

# 170.83.202.0 - - [30/Jun/2019:03:19:51 +0800] "GET / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7" "-"
# 167.71.176.25 - - [30/Jun/2019:04:22:30 +0800] "HEAD / HTTP/1.1" 200 0 "https://www.netcraft.com/survey/" "Mozilla/4.0 (compatible; Netcraft Web Server Survey)" "-"

# with open(file='./txtFile/access_log',mode='r',encoding='utf8')as file2:
#     hang01 = file2.readlines()
#     list03 = []
#     dict03 = {}
#     for nn in hang01:
#         stats = nn.split('1.1"')[1]
#         stats_true = stats.split(' ')[0]
#         print(stats)