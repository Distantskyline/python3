# 请统计access_log中所有的状态码(200, 404, 502, 503)各自出现的数量,并把统计好的数据json格式化,存储到文件中

ips = {}
with open(file='../txtFile/access_log', mode='r', encoding='utf8') as log:
    for lines in log.readlines():
        if lines.split()[8] not in ips.keys():
            ips.setdefault(lines.split()[8], 1)
        else:
            ips[lines.split()[8]] += 1
    ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))
    print(ips)
    statusCode, codes = ['200', '404', '502', '503'], {}
    for code in ips.keys():
        if code in statusCode:
            codes[code] = ips[code]
    print(codes)

