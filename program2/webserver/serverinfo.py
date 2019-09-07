#!/usr/bin/env bash
#
#author:
#date:
#usage:

def puv(logpath):
    puv=[]
    with open(file=logpath,mode='r',encoding='utf8')as log:
        for lines in log:
            x = lines.split(' ')[0]
            puv.append(x)
        pv = len(puv)
        uv = len(set(puv))
        # print(pv,uv)
    return pv,uv
# puv('../local/log/loginfo.log')
# ips = {}
# with open(file='../local/log/loginfo.log',mode='r',encoding='utf8')as file:
#     for lines in file:
#         x = lines.split(' ')[0]
#         if x not in ips:
#             ips.setdefault(x,1)
#         else:
#             ips[x] += 1
#     ips = sorted(ips.items(),key=lambda x: x[1],reverse=True)[0:5]
# print(ips)
def ips(logpath):
    ips = {}
    with open(file=logpath,mode='r',encoding='utf8')as log:
        for lines in log:
            y = lines.split(' ')[0]
            if y not in ips:
                ips.setdefault(y ,1 )
            else:
                ips[y] += 1
        ips = sorted(ips.items(),key=lambda x: x[1],reverse=True)[0:3]
        # print(ips)
    return ips


code = {'200': 0, '404': 0, '502': 0, '503': 0}
def stat(logpath):
    global code
    stats,code = ['200', '404', '502', '503'],{'200': 0, '404': 0, '502': 0, '503': 0}
    with open(file=logpath,mode='r',encoding='utf8')as log:
        for lines in log:
            z = lines.split(' ')[8]
            if z in stats:
                if z not in code:
                    code.setdefault(z,1)
                else:
                    code[z] += 1
        # print(code)
    return code

# stat('../local/log/loginfo.log')


#获取往钉钉推送的 code信息
def dingding(logpath):
    stat(logpath)

    dingcode = {}
    for x in code.keys():
        y = code[x]
        if y != 0:
            dingcode.setdefault(x,y)
    # print(dingcode)
    return dingcode
# dingding('../local/log/loginfo.log')