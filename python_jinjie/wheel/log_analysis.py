#!/usr/bin/env python3
#date:190819
#author:Distantskyline
#usage:log analysis


def loganalysis(path):
    ips = {}
    with open(file=path,mode='r',encoding='utf8')as log:
        for lines in log.readlines():
            ips.setdefault(lines.split()[0],0)
            ips[lines.split()[0]] += 1
        return ips
# test = loganalysis('access_log')
# print(test)
#

