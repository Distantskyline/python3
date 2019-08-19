#!/usr/bin/env python

#author:
#date
#usage:
#

# dict01 = {'name': 1,'age': 2,}
# print(dict01)
# dict02 = dict({1: 2,3: 4,4: 5})
# print(dict02)
# dict03 = dict([(1,2),(2,3),(3,4)])
# print(dict03)
# dict04 = dict(name=1,age=3,height=4)
# print(dict04)

#增删改查
# ips = {'192.168.161.10': 34,'39.100.110.135': 385,'1.1.1.1': 234,'8.8.8.8': 55}
# # list01 = []
# print(ips['192.168.161.10'])

#取字典中的键
# for keys in ips.keys():
#     print(keys)
#     list01.append(keys)
# tuple01 = tuple(list01)
# print(tuple01)

#去字典中的值
# for values in ips.values():
#     print(values)

#取键值对
# ips = {'192.168.161.10': 34,'39.100.110.135': 385,'1.1.1.1': 234,'8.8.8.8': 55}
# list01 = []
# def abc(elem):
#     return elem[1]
# for item in ips.items():
#     list01.append(item)
# list01.sort(key=abc)
# list02 = list01
# print(list02)
# #
# list001 = []
# for x in ips.items():
#     list001.append(x)
# for i in range(len(ips)):
#     for j in range(len(list001)-i-1):
#         if list001[j][1] > list001[j+1][1]:
#             list001[j],list001[j+1] = list001[j+1],list001[j]
# print(list001)

#国盛法
# ips = {'192.168.161.10': 34,'39.100.110.135': 385,'1.1.1.1': 234,'8.8.8.8': 55}
# list01 = []
# dict01 = {}
# for i in ips.items():
#     list01.append(i[1])
# list01.sort()
# c = list01
# print(c)
# for j in list01:
#     for m in ips.items():
#         print(m)
#         if m[1] == j:
#             dict01[m[0]] = m[1]
# print(dict01)


# dict01 = {'name': 'bavduer', 'age': 18, 'gender': 'male'}

set01 = {0,1,2,3,4,5,6,7,8,9}
set02 = {3,4,5,6,7}
set03 = {'a','b','c','d','e','f','g'}
# set03.pop()
# print(set03)
# set04 = set01 | set03
# print(set04)
# set01.update(())
# set05 = set01
# print(set05)
# set01.add('asda')
# # print(set01)



dict01 = {'name': 'bavduer', 'age': 18, 'gender': 'male'}
dict02 = dict({'name': 'bavduer', 'age': 18, 'gender': 'male'})
dict03 = dict([('name', 'bavduer'), ('age', 18), ('gender', 'male')])
dict04 = dict(name='bavduer', age=18, gender='male')
# if dict01 == dict02 == dict03 == dict04:
#     print(111)

# print(dict01['name'])
# print(dict01['age'])

# #遍历字典键
# for keys in dict01.keys():
#     print(keys)
# #遍历字典值
# for values in dict01.values():
#     print(values)

#字典的增删改查
# dict01['age'] = 19
# print(dict01)
# dict01['class'] = 7
# print(dict01)
# dict01.pop('name')
# print(dict01)
# dict01.update([('class',7)])
# print(dict01)
# dict01.items()
# print(dict01)
# dict01.fromkeys('class')
# a = dict01
# print(a)
dict01 = {'name': 'bavduer', 'age': 18, 'gender': 'male'}
#添加新的键和值，一次只能填一个，只写键时值默认为none
# dict01.setdefault('class',7)
# print(dict01)

#使用 .keys获取字典的keys
a = dict01.keys()
print(a)




























