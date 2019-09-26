# import json
#
# ips = {}
# with open(file='./access_log',mode='r',encoding='utf8')as log:
#     for lines in log:
#         ip = lines.split(" ")[0]
#         if ip not in ips.keys():
#             ips.setdefault(ip,1)
#         else:
#             ips[ip] += 1
#     ips = sorted(ips.items(),key=lambda x : x[1],reverse=True)
#     ips = dict(ips[0:10])
# with open(file='./pv.json',mode='a',encoding='utf8')as pv:
#     json.dump(ips,pv,ensure_ascii=True)
#     pv.write('\n')



# import json
# stat = ['200','404','502','503']
# code = {}
# with open(file='./access_log',mode='r',encoding='utf8')as log:
#     for lines in log:
#         if lines.split(' ')[8] in stat:
#             code.setdefault(lines.split(' ')[8],1)
#             code[lines.split(' ')[8]] += 1
# with open(file='./scode.json',mode='a',encoding='utf8')as log:
#     json.dump(code,log,ensure_ascii=False)
#     log.write('\n')



# import json
# source = {}
# with open(file='./access_log',mode='r',encoding='utf8')as log:
#     for lines in log:
#         ipaddr = lines.split(' ')[6]
#         if ipaddr not in source:
#             source.setdefault(ipaddr,1)
#         else:
#             source[ipaddr] += 1
#     source = dict(sorted(source.items(),key=lambda x : x[1],reverse=True)[0:10])
# with open(file='./ipaddr.json',mode='a',encoding='utf8')as log:
#     json.dump(source,log,ensure_ascii=False)
#     log.write('\n')



# ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
# ips = sorted(ips.items(),key=lambda x : x[1],reverse=True)
# print(ips)



# ips = []
# with open(file='./access_log',mode='r',encoding='utf8')as log:
#     X = log.readlines()
#     PV = len(X)
#     for y in X:
#         ip = y.split(' ')[0]
#         if ip not in ips:
#             ips.append(ip)
#     UV = len(ips)
#     print(PV)
#     print(UV)



