#!/usr/bin/env
#date:190808
#author:Distantskyline
#usage:

# 5.请统计access_log中访问量前十的IP地址,并生成json格式数据,保存至文件中.
# (用python代码实现)

# 170.83.202.0 - - [30/Jun/2019:03:19:51 +0800] "GET  / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7" "-"
# 167.71.176.25 - - [30/Jun/2019:04:22:30 +0800] "HEAD / HTTP/1.1" 200 0 "https://www.netcraft.com/survey/" "Mozilla/4.0 (compatible; Netcraft Web Server Survey)" "-"
# 88.248.13.15 - - [30/Jun/2019:04:43:20 +0800] "GET / HTTP/1.1" 200 152 "-" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36" "-"

def PUV (path):
    with open(file=path, mode='r', encoding='utf8') as log:
        a = log.readlines()
        print('PV量:',len(a))

    ips = {}
    with open(file=path, mode='r', encoding='utf8') as log:
        for lines in log.readlines():
            if lines.split()[0] not in ips.keys():
                ips.setdefault(lines.split()[0], 1)
            else:
                ips[lines.split()[0]] += 1

        ips = (sorted(ips.items(), key=lambda x: x[1], reverse=True))

        print('UV量:',(len(list(ips))))
    print(dict((ips)[0:10]))
PUV('../day3/txtFile/access_log')



# 6.请统计access_log中所有的状态码(200, 404, 502, 503)各自出现的数量,
# 并把统计好的数据json格式化,存储到文件中

# def stats(path):
#     stats = {}
#     stats1 = {}
#     with open(file=path,mode='r',encoding='utf8')as file:
#         for line in file.readlines():
#            if line.split()[8] not in stats.keys():
#                stats.setdefault(line.split()[8],1)
#            else:
#                stats[line.split()[8]] +=1
#         stats = dict(sorted(stats.items(),key=lambda x: x[1],reverse=True))
#         list01 = ['200','404','502','503']
#         for i in stats.keys():
#             if i in list01:
#                 stats1[i] = stats[i]
#         return stats1
#         # for i in stats.items():
#         #     if i[0] in list01:
#         #         stats1[i[0]] = stats[i[0]]
#         # return stats1
# print(stats('../day3/txtFile/access_log'))