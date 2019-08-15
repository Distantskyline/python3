# 请统计access_log中访问最大的资源,前十名,并把统计好的数据json格式化,存储到文件中(被访问资源如下所示)
# 185.173.224.24 - - [30/Jun/2019:11:48:52 +0800] "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" 404 0 "-" "-" "-"
# "GET /wordpress/wp-includes/wlwmanifest.xml HTTP/1.1" - 这就是被访问的资源整体(包括了请求方法、所用协议)
# /wordpress/wp-includes/wlwmanifest.xml - 这就是其中的资源

source = {}
with open(file='../txtFile/access_log', mode='r', encoding='utf8') as log:
    for lines in log.readlines():
        if lines.split()[6] not in source.keys():
            source.setdefault(lines.split()[6], 1)
        else:
            source[lines.split()[6]] += 1
    source = sorted(source.items(), key=lambda x: x[1], reverse=True)
print(source)
head10 = dict(source[0:10])
print(head10)



