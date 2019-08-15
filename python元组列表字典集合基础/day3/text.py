


#
# with open(file='../day3/txtFile/access_log', mode='r', encoding='utf8') as log:
#     a = log.readlines()
#     print(len(a))
# ips = {}
# with open(file='./txtFIle/access_log',mode='r',encoding='utf8')as file:
#     for lines in file.readlines():
#         if lines.split()[0] not in ips:
#             ips.setdefault(lines.split()[0],1)
#         else:
#             ips[lines.split()[0]] +=1
#     ips = sorted(ips.items(),key=lambda x: x[1],reverse=True)
#     ips1 = ips[0:10]
# print(ips1)
# import json
# with open(file='./txtFile/pv.json',mode='w',encoding='utf8')as file:
#     json.dump(ips1,file,ensure_ascii=False)

# stats = {}
# stats1 = {}
# with open(file='./txtFile/access_log', mode='r', encoding='utf8')as file:
#     for line in file.readlines():
#         if line.split()[8] not in stats.keys():
#             stats.setdefault(line.split()[8], 1)
#         else:
#             stats[line.split()[8]] += 1
#     stats = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))
#     list01 = ['200', '404', '502', '503']
#     for i in stats.keys():
#         if i in list01:
#             stats1[i] = stats[i]
# print(stats1)
# import json
# with open(file='./txtFile/scode.json',mode='w',encoding='utf8')as file:
#     json.dump(stats1,file,ensure_ascii=False)

# zy= {}
#     # = {}
# with open(file='./txtFile/access_log', mode='r', encoding='utf8')as file:
#     for line in file.readlines():
#         if line.split()[6] not in zy.keys():
#             zy.setdefault(line.split()[6], 1)
#         else:
#             zy[line.split()[6]] += 1
#
# zy = (sorted(zy.items(), key=lambda x: x[1], reverse=True))
# zy1 = zy[0:10]
# print(zy1)
# import json
# with open(file='./txtFile/ipaddr.json',mode='w',encoding='utf8')as file:
#     json.dump(zy1,file,ensure_ascii=False)
#
# ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
# ips1 = sorted(ips.items(),key=lambda x: x[1], reverse=True)
# print(ips1)

# def PUVL (path):
#     with open(file=path, mode='r', encoding='utf8') as log:
#         a = log.readlines()
#         print('PV量:',len(a))
#
#     ips = {}
#     with open(file=path, mode='r', encoding='utf8') as log:
#         for lines in log.readlines():
#             if lines.split()[0] not in ips.keys():
#                 ips.setdefault(lines.split()[0], 1)
#             else:
#                 ips[lines.split()[0]] += 1
#
#         ips = (sorted(ips.items(), key=lambda x: x[1], reverse=True))
#
#         print('UV量:',(len(list(ips))))
# PUVL('./txtFile/access_log')

with open(file='../day3/txtFile/access_log', mode='r', encoding='utf8') as log:
    a = log.readlines()
    print(len(a))
ips = {}
with open(file='./txtFIle/access_log',mode='r',encoding='utf8')as file:
    for lines in file.readlines():
        if lines.split()[0] not in ips:
            ips.setdefault(lines.split()[0],1)
        else:
            ips[lines.split()[0]] +=1
    ips = sorted(ips.items(),key=lambda x: x[1],reverse=True)
    ips1 = ips[0:10]
print(ips1)

