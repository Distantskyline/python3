#!/usr/bin/env python3

#author: Distantskyline
#date: 190806
#usage: study
#
# list01 = [1,2,3,1,1,23,414.1,False,'string']
# tuple01 = [2.3,42,12,True,'singing']
# # print(len(list01))
# for i in range(len(list01)):
#     print(list01[i])
#
# # for i in range(len(tuple01)):
# #     print(tuple01[i])
# for hh in list01:
#     print(hh)
# for aa in tuple01:
#     print(aa)

# a = list01.count(0)
# print(a)
#
# b = tuple01.count(0)
# print(b)

# list01 = [1,2,3,1,1,23,414.1,False,'string']
# tuple01 = [2.3,42,12,True,'singing']
# list01.insert(4,True)
# print(list01)
# list02 = [1,2,3,4,5,6,7,1,2,3,4,5]
# list01.extend(list02)
# print(list01)
# print(list01)
# list01.remove(1)
# print(list01)
# print(list01.remove(1),list01)
# list01.reverse()
# print(list01)
# list01.count(1)
# a = list01.count(1)
# print(a)
# a = list01.index(23)
# print(a)

sl = ( '猴','鸡','狗','🐖','鼠','🐮','虎','兔','🐉','🐍','🐴','羊','（⊂((・⊥・))⊃）','鸡','狗','🐖')

a = int(input('请输入年份：'))
b = int(input('请输入月份：'))
c = int(input('请输入日期：'))
print(sl[ a % 12])
