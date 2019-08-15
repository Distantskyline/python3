# 请统计access_log中访问量前十的IP地址,并生成json格式数据,保存至文件中.

ips = {}
with open(file='../txtFile/access_log', mode='r', encoding='utf8') as log:
    for lines in log.readlines():
        if lines.split()[0] not in ips.keys():
            ips.setdefault(lines.split()[0], 1)
        else:
            ips[lines.split()[0]] += 1
    ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))

print(ips)


def log(path):
    ips = {}
    with open(file=path, mode='r', encoding='utf8') as log:
        for lines in log.readlines():
            if lines.split()[0] not in ips.keys():
                ips.setdefault(lines.split()[0], 1)
            else:
                ips[lines.split()[0]] += 1
        ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))
    return ips


dicts = log('../txtFile/access_log')
print(dicts)
