# 1.统计kingdoms.txt中"曹操"、"刘备"、"卧龙"、"孙权"各出现的次数？并将其生成字典持久化存储
# 2.统计kingdoms.txt中"青龙偃月刀"、"丈八蛇矛"、"赤兔马"、"雌雄双股剑"各出现的次数？并将其生成字典持久化存储
# 3.请将上述生成的两个字典,按照其中的出现次数进行从大到小排序？

#!/usr/bin/env python3

# with open(file='./txtFile/king.txt', mode='r+', encoding='utf8') as file:
#     content = file.readline()
#     print(content)
#

with open(file='./txtFile/kingdoms.txt',mode='r+',encoding='utf8') as file:
    content = file.read()
    i = 0
    j = 0
    k = 0
    l = 0
    z = 0
    x = 0
    while i < len(content):
        if '曹操' == content[i-1] + content[i]:
                j += 1

        if '刘备' == content[i-1] + content[i]:
                k += 1
        if '卧龙' == content[i-1] + content[i]:
                l += 1
        if '孙权' == content[i-1] + content[i]:
                z += 1
        if '曹孟德' == content[i-2] + content[i-1] + content[i]:
                x += 1
        i += 1
    # print('曹操:',j)
    # print('刘备:',k)
    # print('卧龙:',l)
    # print('孙权:',z)
    # print('曹孟德:',x)
    dict01 = {}
    dict01.update({'曹操': j,'刘备': k,'卧龙': l,'孙权': z,'曹孟德': x})
    print(dict01)
    # q = 0
    # w = 0
    # e = 0
    # r = 0
    # t = 0
    # y = 0
    # while q < len(content):
    #     if '青龙偃月刀' == content[q-4] + content[q-3] + content[q-2] + content[q-1] + content[q]:
    #         w += 1
    #     if '雌雄双股剑' == content[q-4] + content[q-3] + content[q-2] + content[q-1] + content[q]:
    #         t += 1
    #     if '丈八蛇矛' == content[q - 3] + content[q - 2] + content[q - 1] + content[q]:
    #         e += 1
    #     if  '赤兔马' == content[q - 2] + content[q - 1] + content[q]:
    #         r += 1
    #     q += 1
    # # print('青龙偃月刀:',w)
    # # print('丈八蛇矛:',e)
    # # print('赤兔马:',r)
    # # print('雌雄双股剑:',t)
    # dict02 = {}
    # dict02.update({'青龙偃月刀': w,'丈八蛇矛': e,'赤兔马': r,'雌雄双股剑': t})
    # print(dict02)
    #
    # ####---大小排序
    # ####---
    # #  dict03 = {'曹操': 946, '刘备': 298, '卧龙': 42, '孙权': 320, '曹孟德': 9, '青龙偃月刀': 3, '丈八蛇矛': 4, '赤兔马': 24, '雌雄双股剑': 0}
    # dict03 = {}
    # dict03.update(dict01)
    # dict03.update(dict02)
    # list04,dict04 = [],{}
    # for qq in dict03.items():
    #     list04.append(qq[1])
    # list04.sort()
    # list04.reverse()
    # for shuzi in list04:
    #     for jianzhi in dict03.items():
    #         if shuzi == jianzhi[1]:
    #             dict04[jianzhi[0]] = shuzi
    # print(dict04)
    #
    #
    #

































