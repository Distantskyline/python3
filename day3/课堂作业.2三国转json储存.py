#!/usr/bin/env python3
#
#usage：
#date：
#author：

# 4.请将上述的字典生成json格式的数据,并保存至文件中
# 5.请统计access_log中访问量前十的IP地址,并生成json格式数据,保存至文件中.(用python代码实现)
# 6.请统计access_log中所有的状态码(200, 404, 502, 503)各自出现的数量,并把统计好的数据json格式化,存储到文件中
# 7.请统计access_log中访问最大的资源,前十名,并把统计好的数据json格式化,存储到文件中(被访问资源如下所示)
# 185.173.224.24 - - [30/Jun/2019:11:48:52 +0800] "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" 404 0 "-" "-" "-"
# "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" - 这就是被访问的资源整体(包括了请求方法、所用协议)
# /wordpress/wp-includes/wlwmanifest.xml - 这就是其中的资源


# with open(file='./txtFile/hardwareInfo.json', mode='r', encoding='utf8') as file:
#     content = file.read()
#     print(content, type(content))
#     dictA = json.loads(content, encoding='utf8')
#     print(dictA, type(dictA))
#     file.write(json.dumps(info))
dict01 = {'曹操': 946, '孙权': 320, '刘备': 298, '卧龙': 42, '赤兔马': 24, '曹孟德': 9, '丈八蛇矛': 4, '青龙偃月刀': 3, '雌雄双股剑': 0}
import json
with open(file='./txtFile/json存储.json', mode= 'w',encoding ='utf8') as file:
    file.write(json.dumps(dict01,ensure_ascii=False))

