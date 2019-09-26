# list01 = [1,2,3,4,5]
# list02 = [8,9]
# # list01.append(list02)
# print(list01)
#
# list01.insert(2,'hh')
# print(list01)
# list02.extend(list01)
# print(list02)

##         ips 匿名函数排序

# ips = [('1.1.1.1', 12), ('2.2.2.2', 43), ('3.3.3.3', 11), ('4.4.4.4', 76), ('5.5.5.5', 16)]
# ips.sort(key=lambda x: x[1])
# print(ips)
#
# ips = [('1.1.1.1', 12), ('2.2.2.2', 43), ('3.3.3.3', 11), ('4.4.4.4', 76), ('5.5.5.5', 16)]
# ipsOpera = sorted(dict(ips).items(), key=lambda x: x[1], reverse=False)
# print(ipsOpera)


##          装饰器
#
# import functools
# def waibu(func):
#     @functools.wraps(func)
#     def neibu(*args,**kwargs):
#         print('hello world')
#         func(*args,**kwargs)
#         print('nice to meet you')
#     return neibu
#
# @waibu
# def test(x,y):
#     print(x+y)
#
# # Test = waibu(test)
# test(15,20)


##           类的创建

# class Box:
#     def __init__(self,x,y):
#         self.x= x
#         self.y= y
#
#     def jisuan(self,):
#         z = self.x*self.y
#         return z
# test01 = Box(2,4)
# print(test01.jisuan())
# ##     属性值的修改   如果要私有化，则把定义属性时加下划线
# test01.x = 3
# test01.y = 3
# print(test01.jisuan())


##  @staticmethod  静态方法，作为最内部的属性的装饰作用，不会影响其他的方法
##  @classmethod   类方法，比实例化更加清晰的创建属性，



##                 子类

# class Js:
#     def __init__(self,x,y):
#         self.x =x
#         self.y= y
#
#     def js(self):
#         z = self.x*self.y
#         return z
#
# class Test(Js):
#     def __init__(self,x,y,q):
#         super(Test, self).__init__(x, y)
#         self.q =q
#
#     def js(self):
#         c = self.x+self.y+self.q
#         return c
#
# test = Test(1,2,3)
# result = test.js()
# print(result)

##                 new  魔术方法

# class Document:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'x'):	## 判断cls(类)中含不含有instance参数实例不存在就建 新的
#             cls.x = super().__new__(cls) ##开辟一段内存地址，用来存后面生成的实例
#         return cls.x
#
#     def __init__(self, path):
#         self.path = path

    # def write(self, content):
        # with open(self.path, 'a', encoding='utf8') as file:
        #     file.writelines(content)


# cfile = Document('file.txt')
# cfile.write('''
#     this is my first line.\n
#     this is second line.\n
#     this is third line.''')

# 不管实例化几次,内存的地址都是不会变的.(这种方式通常是节约内存开销的)
# file01 = Document('file01.txt')
# file02 = Document('file02.txt')
#
# print(id(file01))
# print(id(file02))  ##新建的实例，内存ID都是一样的了，因为  __new__创建了新的内存统一存


##                     自定义跑出异常
#
# class Myinputerror(Exception):
#     def __init__(self,q):
#         self.q =q
#     def __str__(self):
#         return '{} is cuowu input'.format(self.q)
#
# try:
#     x = input(':')
#     if 'abcd' in x:
#         raise Myinputerror(x)
# except Myinputerror as error :
#     print('hhh')


##                        os.walk
# import os
# for x,y,z in os.walk('../2.面向对象'):
#     print('''
#         文件名：{}
#         文件夹个数：{}
#         文件个数：{}
#         '''.format(x,len(y),len(z)))


##                      findall 寻找符合条件的数据
import re
# a = 'abcdefghigklmnopqrstuvwxyz'
# result = re.findall(pattern='^a',string=a)
# print(result)

# import subprocess
# x = subprocess.Popen(['ls ','/root'],stdout=subprocess.PIPE)
# x.stdout.read()
# print(x)

# import redis
# pool = redis.ConnectionPool(host = '192.168.52.134',port = 6379,db=0)
# client = redis.Redis(connection_pool=pool)



##
# list01 = [1, 7, 2, 5, 3, 4]
# list01.reverse()							# 把列表中的元素位置反转
# print(list01)
#
# string = "long with me play game"
# strlist = string.split()
# strlist.reverse()
# result = ""
# for i in strlist:
#     result += i + " "
# print(result.rstrip())

# ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
# print(ips.items())

# 方式一: 使用冒泡排序进行字典中键值对排序
list01 = [23, 14, 12, 21, 45, 99, 34, 42]
access = []
for item in list01:
    access.append(item)
print(access)
for i in range(len(list01)):
    for j in range(len(list01) - i ):
        if access[j] > access[j+1]:
            access[j], access[j+1] = access[j+1], access[j]
access = dict(access)
print(access, type(access))


# 方式二: 国盛法(针对字典的值排序)
# listA, dictA = [], {}
# for item in ips.items():
#     listA.append(item[1])
# listA.sort(reverse=True)
# for values in listA:
#     for item in ips.items():
#         if values == item[1]:
#             dictA[item[0]] = values
# print(dictA)
