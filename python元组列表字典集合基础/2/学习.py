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

# sl = ( '猴','鸡','狗','🐖','鼠','🐮','虎','兔','🐉','🐍','🐴','羊','（⊂((・⊥・))⊃）','鸡','狗','🐖')
#
# a = int(input('请输入年份：'))
# b = int(input('请输入月份：'))
# c = int(input('请输入日期：'))
# print(sl[ a % 12])
# str = "this is '''" \
#       "my house'''" \
#       "hhh"
# print(str)

# warn = '''System monior messages:
#             CPU rate:{}%
#             MEM rate:{}%
#             DISK rate:{}%
#             NETWORK mbps:{}m
#      @{}'''.format('80','20','50','1000','ZZZZ')
# print(warn)

# str = 'hello word for you'
# if 'word' in str:
#         print('find')


#--------------------------------------------------------

# 字符串------

#定义
# str01 = 'hello word'
# str02 = 'this is my book'
# print(str01)
# print(str02)

#索引切片
# str01 = 'this is my book not you please not take it'
# #        012345678901234567890123456789012345678901
# #                  1         2         3         4
# print(str01[1:4])
# print(str01[11:19])

#-'索引'-遍历字符串
# str01 = 'this is my book'
# for x in range(len(str01)):
#     y = str01[x]
#     print(y)

#直接遍历字符串
# str01 = 'this is my book'
# for i in str01:
#     print(i)

#用空格作为分隔符进行分割,生成一个列表
# str01 = 'this is my book'
# str02 = str01.split()
# print(str02)

#替换旧字符为新字符
# str01 = 'this is my book'
# str02= str01.replace('o','A')
# print(str02)

#去掉开头结尾某个字符
# str01 = 'this is my book'
# str02 = str01.lstrip('t')
# print(str02)
# str01 = 'this is my book'
# str02 = str01.strip('k')
# print(str02)
# str03 = str01.rstrip('k')
# print(str02)

#判断字符是否在字符串中
# str01 = 'this is my book'
# if 'this' in str01:
#     print(1)

#--------------------------------------------------------------

#列表


#遍历索引列表
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# for i in range(len(list01)):
#     print(list01[i])

#直接对元素进行索引
# for i in list01:
#     print(i)
#统计元素 1 的个数
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# a = list01.count(1)
# print(a)

#查找元素的索引号
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# a = list01.index(2)
# print(a)

#指定索引添加元素
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list01.insert(1,12)
# print(list01)

#把列表扩充到另一个列表中
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list02 = [5,5,5,4]
# list01.extend(list02)
# print(list01)
#指定元素删除
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list01.remove(2)
# print(list01)
#指定元素索引号删除
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list01.pop(4)
# print(list01)

#清空列表
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list01.clear()
# print(list01)

#反转元素
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list01.reverse()
# print(list01)

#从小大排序
# list01 = [1,2,3,4,5,1.2,2.2,]
# list01.sort()
# print(list01)

#指定索引号上的元素直接更改
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# list01[2] = 100
# print(list01)

#统计特定元素个数
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# a = list01.count(1)
# print(a)

#按照给顶元素范围查找元素索引号
# list01 = [1,2,3,4,5,1.2,2.2,'哈哈']
# a = list01.index(2.2,1,8)
# print(a)
#元组
#遍历索引元组

# 直接对元组进行索引

# 统计元素 1 的个数

# 查找元素的索引号

# 指定索引添加元素

# 把列表扩充到另一个列表中

# 指定元素删除

# 指定元素索引号删除

# 清空元组

# 反转元素

# 从小大排序

# 指定索引号上的元素直接更改

# 统计特定元素个数

# 按照给顶元素范围查找元素索引号













































