#!/usr/bin/env python3
#
#authro:Distantskyline
#date:190815
#usage:

####链式继承

# class Document:
#     def __init__(self,path):
#         print('Document class __init__ magic method')
#         self.path =path
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'instance'):
#             cls.instance = super().__new__(cls)
#         return  cls.instance
#
#     def getContent(self):
#         with open(self.path,'r',encoding='utf8')as file:
#             content = file.read()
#             return content
#
#
# class File(Document):
#     def __init__(self,path):
#         super(File, self).__init__(path)
#         print('file class __init__ magic method')
#
# class dir(File):
#     def __init__(self,path):
#         super(dir, self).__init__(path)
#         print('dir ......')
#
# class Configfile(dir):
#     def __init__(self,path):
#         super(Configfile, self).__init__(path)
#         print('Configfile class .....')
#
# nginxFile = Configfile('file.txt')
# content = nginxFile.getContent()
# print(content)


####菱形继承结构
#
# class A:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def getinfo(self):
#         return self.name
#
# class B(A):
#     def __init__(self,name,age,sex,length):
#         A.__init__(self,name,age)
#         self.sex = sex
#         self.length = length
#
#     def getinfo(self):
#         return self.name
#
# class C(A):
#     def __init__(self,name,age,length):
#         A.__init__(self,name,age)
#         self.length = length
#
#     def getinfo(self):
#         return self.name
#
# class D(B,C):
#     def __init__(self,name,age,sex,length,width):
#         B.__init__(self,name,age,sex,length)
#         C.__init__(self,name,age,length)
#         self.width = width
#
# person =  D(name='wenzhisheng', age=900, sex='WM', length='2CM', width='0.5CM')
# print(D.mro())



# ####攻击
# import random
# class person:
#     BUFF = random.randint(0,10)
#     def __init__(self,xie,gongji,lan,xiaohao):
#         self.xie = xie
#         self.gongji = gongji
#         self.lan = lan
#         self.xiaohao = xiaohao
#
#     @classmethod
#     def createuser(cls,xie,gongji,lan,xiaohao):
#         return cls(xie = xie,gongji = gongji ,lan = lan ,xiaohao = xiaohao )
#
#     def dadou(self,instance):
#         instance.xie -= self.gongji + self.BUFF
#         self.lan -= self.xiaohao
#
#     def getxie(self,zhi):
#         self.xie += int(zhi)
#
#     def getinfo(self):
#         info = {
#             'xie': self.xie,
#             'lan': self.lan
#         }
#         return info
#
# wj1 = person.createuser(xie = 100 , gongji = 50 , lan = 100 , xiaohao = 20)
# wj2 = person.createuser(xie = 200,gongji = 30 , lan = 100 , xiaohao = 35)
#
# for bout in range(10):
#     if bout % 2 == 0 :
#         wj1.dadou(wj2)
#     else:
#         wj2.dadou(wj1)
# else:
#     if wj1.getinfo()['xie'] <= 0:
#         print('wj1死了')
#
#     elif wj2.dadou()['xie'] <= 0:
#         print('wj2死了')
#
#
# print('wj1 info: {}'.format(wj1.getinfo()))
# print('wj2 info. {}'.format(wj2.getinfo()))
# # print(wj2.getinfo())



# ##两个类攻击
# import random
# class wanjia1:
#     buff = random.randint(0,10)
#     def __init__(self,x,gjl,l,xh):
#         self.x = x
#         self.gjl = gjl
#         self.l = l
#         self.xh = xh
#     def gongji(self,instance):
#         instance.x -= self.gjl + self.buff
#         self.l -= self.xh
#     def getinfo(self):
#         info = {
#             'xie': self.x,
#             'lan': self.l
#         }
#         return info
#
#
# class wanjia2:
#     buff = random.randint(0, 10)
#     def __init__(self, x, gjl, l, xh):
#         self.x = x
#         self.gjl = gjl
#         self.l = l
#         self.xh = xh
#
#     def gongji(self,instance):
#         instance.x -= self.gjl + self.buff
#         self.l = self.xh
#
#     def getinfo(self):
#         info = {
#             'xie': self.x,
#             'lan': self.l
#         }
#         return info
# wj1 = wanjia1( x = 100 , gjl = 100 , l = 100 , xh = 30 )
#
# wj2 = wanjia2( x = 200 , gjl = 30 , l = 100 , xh = 40 )
#
# for x in range(40):
#     wj1.gongji(wj2)
#     if random.randint(0,9) %2 == 0 :
#         wj2.gongji(wj1)
# else:
#     if wj1.x <= 0:
#         print('wj1死了')
#     elif wj2.x <= 0:
#         print('wj2死了')


def waibu(func):
    def neibu():
        print('zhuangshiqi')
        func()
        print('hhh')
    return neibu

@waibu
def test():
    print('123')


# zsq = waibu(test)
test()
