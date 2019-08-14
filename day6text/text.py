# !/usr/bin/env python3
#
# author:
# date:
# usage:
#
# list01 = [1,2,3,4]
# list01.append(14)
# print(list01)
# for i in list01:
#     print(i)
# for ii in range(len(list01)):
#     print(list01[ii])
#
# #快速生成一个字典
#
# dict01 = {}.fromkeys([('tom',5),('12',156)])
# print(dict01)

ips = {}
def puip (path):
    # with open(file=path,mode='r',encoding='utf8')as file:
    #     lines = file.readlines()
    #     len1 = len(lines)
    # print(len1)
        # a = file.readlines()
        # print('PV量:', len(a)

    with open(file=path,mode='r',encoding='utf8')as file:
        # ips = {}
        global ips
        for lines in file.readlines():

            if lines.split()[0] not in ips.keys():
                ips.setdefault(lines.split()[0],1)
            else:
                ips[lines.split()[0]] += 1
        ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)
        # print(ips[0:10])
    # print(ips)
# print(ips)
puip('../day3/txtFile/access_log')
# ##
#
# --------------------------------------+
# |                                     |
# |                                     |
# |   统计 txtFile中的ip 的数量以及访问次数  |
# |                                     |
# +-------------------------------------|
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
        ips = dict((ips)[0:10])
    print((ips))
PUV('../day3/txtFile/access_log')

#
# ####计算
# #
# def text(x,y,z):
#     var01 = int(input(x))
#     print(var01)
#     var02 = int(input(y))
#     print(var02)
#     var03 = int(input(z))
#     print(var03)
# text(4,6,7)

#######################################
##                                   ##
##                                   ##
##                                   ##
##               周考                 ##
##                                   ##
##                                   ##
##                                   ##
#######################################

#6.
print(dict(ips))

def guolv():
    for i in ips:
        print(i)
        if i[1] > 100:
            return True
x = filter(guolv,ips)
print(list(x))

#7.
# def jibu(step):
#     def stepCount():
#         nonlocal step
#         step += 1
#         print(step)
#     return stepCount
#
# step = jibu(10)
# print(step())
# print(step())
# print(step())

#