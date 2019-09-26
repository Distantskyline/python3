#!/usr/bin/env python3
#
#date:190813
#author:Distantskyline
#usage:log_class




class Logfile:                       # log处理类
    def __init__(self,path):
        self.path = path
    def PUV(self):                  #PV 和 UV  量的 检测
        with open(file=self.path, mode='r', encoding='utf8') as log:
            a = log.readlines()
            b = len(a)

        ips = {}
        with open(file=self.path, mode='r', encoding='utf8') as log:
            for lines in log.readlines():
                if lines.split()[0] not in ips.keys():
                    ips.setdefault(lines.split()[0], 1)
                else:
                    ips[lines.split()[0]] += 1
            ips = (sorted(ips.items(), key=lambda x: x[1], reverse=True))
            # print('UV量:', (len(list(ips))))
            c = len(list(ips))
            # print(c)
            return b,c                    ##输出 PV 量 UV 量

    def STATS(self):                         ##状态码函数
        ips = {}
        with open(file=self.path, mode='r', encoding='utf8') as log:
            for lines in log.readlines():
                if lines.split()[8] not in ips.keys():
                    ips.setdefault(lines.split()[8], 1)
                else:
                    ips[lines.split()[8]] += 1
            ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))
            # print(ips)
            statusCode, codes = ['200', '404', '502', '503'], {}
            for code in ips.keys():
                if code in statusCode:
                    codes[code] = ips[code]
            return codes     ##返回状态码列表

    def SOURCE(self):               ##最热资源处理函数
        source = {}
        with open(file=self.path, mode='r', encoding='utf8') as log:
            for lines in log.readlines():
                if lines.split()[6] not in source.keys():
                    source.setdefault(lines.split()[6], 1)
                else:
                    source[lines.split()[6]] += 1
            source = sorted(source.items(), key=lambda x: x[1], reverse=True)
        # print(source)
            head10 = dict(source[0:10])
            return head10


logclass = Logfile('./log/access_log')      ##创建实例，实例化
logPUV = logclass.PUV()               ##使用实例调用雷中的方法
logSTATS = logclass.STATS()
logSOURCE = logclass.SOURCE()
while True:
    x = input('请输入想要的log结果：')
    if x == 'PUV':
        print(logPUV)
    elif x == 'STATS':
        print(logSTATS)
    elif x == 'SOURCE':
        print(logSOURCE)
    elif x == 'EXIT':
        break
    else:
        print('请输入正确的结果')