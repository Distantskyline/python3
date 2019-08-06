# print('''
# cpu:{}
# men:{}
# disk{}
# '''.format('70%','50%','20%'))
#

# list01=[1,1.2,2.23,"hello","world",True,]
# tuple=(1,2.33,4.2,'hello','world',False)

# print(list01.append(2123),list01)
#
# print(list01[2:5])
#
# print(list01[2:4])
#
# print(tuple[1:2])
#
# for index in range(len(tuple)):
#     print(tuple[index])

# a=len(list01)
# print(a)
#
#
# print(tuple.count("hello"))
#
# index = list01.index(1.2,0,len(list01))

# str="hello world"
# for index in range(len(str)):
#     print(str[index])

#######  直接遍历字符串
# for i in str:
#     print(i)

# str04 = str[1:] + 'A'
# print(str04)
#
# ID, name = 998, "bavduer"
# print('no data available for person with id: {}, name: {}'.format(ID, name))

######  反转 句子
# str = "this is my house"
# list01 = str.split()
# list01.reverse()
# print(list01)
# str02 = ''
# for i in range(len(list01)):
#     str01 = list01[i]
#     if i != len(list01):
#         str02 += (str01 + ' ')
# print(str02)


# i = 0
# str02 = ''
# while i < len(list01):
#     str01 = list01[i]
#     str02 += str01 + ' '
#     i += 1
#     if i == len(list01):
#         print(str02)
# str03=str02.rstrip()
# print(str03)



######  敏感字符替换，如果存在敏感词混，直接替换为*
# str = 'hello world for you'
# str01 = 'ol'
# n = list(str01)
# if 'o' in str:
#         str02 = str.replace('o','*')
#         print(str02)
# else:
#     print(str02)

######  把数字提交到列表中
# tuple = ('string','world',1,2,3,4,5,6,9,10)
# i = 0
# n = len(tuple)
# list01 = []
# while i < n :
#     a = tuple[i]
#     b = int
#     i += 1
#     if type(a) == b:
#         q = tuple[i-1]
#         list01.append(q)
#         if i == n:
#             print(list01)

######  转换列表中的元组为普通形式
# list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# tuple01 = list01[3]
# i = 0
# list02 = list01[4]
# list01.pop(3)
# list01.pop(3)
# while i < len(tuple01):
#     n=tuple01[i]
#     n = i
#     i += 1
#     list01.append(n)
#     if i == len(tuple01):
#         # print(list01)
#         pass
# u = 0
# while u < len(list02):
#     m = list02[u]
#     list01.append(m)
#     u += 1
#     if u == len(list02):
#         print(list01)
#


######  for 循环数字排序
list01 = [23,12,15,11,29,24,57,21,80,99,45]
# for i in range(len(list01)):
#     for j in range(len(list01) -i -1):
#         if list01[j] > list01 [j+1]:
#             list01[j],list01[j+1] = list01[j+1],list01[j]
# print(list01)

# for i in range(len(list01)):
#     for j in range(len(list01)-i-1):
#         if list01[j] > list01[j+1]:
#             list01[j],list01[j+1] = list01[j+1],list01[j]
# print(list01)