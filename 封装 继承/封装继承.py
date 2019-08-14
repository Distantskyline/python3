#!/usr/bin/env python3
#
#date:190814
#author:Distantskyline
#usage:


# import os
#
#
# class Document:
#     version = 'Version: {}'
#
#     def __init__(self, path):
#         print(self.version.format('1.0'))
#         self.__path = path  ## 封装后类外不能用，类内可以调用   外部不能 调用
#
#
# x = Documeng(. /)
# x.path  ##不能调用
#
#
# class Cfile(Document):  ##子类可以访问，不能改变其值
#     def __init__(self, path, serviceName):  ##path 是私有属性 不能更改
#         super(Cfile, self).__init__(path)
#         self.serviceName = serviceName
#
#     def modify(self, oldContent, newContent):
#         os.system('sed -ri s/{}/{}/g {}'.format(oldContent, newContent, self.path))
#
#     def tfContent(self):  ##方法名，也可以封装 __  无法调用
#         with open(self.path, 'r', encoding='utf8') as file:
#             return file.read()
#
# test = Cfile()
# test.

# class Tfile(Document):
#     def __init__(self, path, content):
#         super(Tfile, self).__init__(path)
#         self.content = content
#
#     def write(self):
#         with open(self.path, 'a', encoding='utf8') as file:
#             file.write(self.content)
#
#     def tfContent(self):
#         with open(self.path, 'r', encoding='utf8') as file:
#             return file.read()


# #声明父类
# class Box:
#     def __init__(self,l,w,h):
#         self.l = l
#         self.w = w
#         self.__h = h
#
#     def getAera(self):
#         mj1 = self.l * self.w
#         mj2 = self.w * self.__h
#         mj3 = self.l * self.__h
#         mj = (mj1 + mj2 + mj3) * 2
#         return mj
#
#     def gettiji(self):
#         tj = self.__h * self.w * self.l
#         return tj
#
# class zhibox(Box):
#     def __init__(self,l,w,h,ys):
#         super(zhibox,self).__init__(l,w,h)
#         self.ys = ys
#
#     def gettj(self):
#         tj,ys = self._h * self.l * self.w , self.ys
#         return tj ,ys
#
#
# zbox = Box(1,2,3)
# print(zbox.getAera())
# zbox1 = zhibox(1,4,2,'yellow')
# print(zbox1.)



# #@property  调用装饰器
#
# class Box:
#     def __init__(self,l,w,h):
#         self.__l = l
#         self.__w = w
#         self.__h = h
#
#     @property
#
#     def MJ(self):
#         mj1 = self.__l * self.__w
#         mj2 = self.__w * self.__h
#         mj3 = self.__l * self.__h
#         mj = (mj1 + mj2 + mj3) * 2
#         return mj
#
#     @MJ.setter
#     def MJ(self,tatil):
#         self.__h, self.__l, self.__w = tatil
#
#
#     @MJ.deleter
#     def MJ(self):
#         print('del')
#
# zhibox = Box(1,1,1)
# print(zhibox.MJ)
#
# zhibox.MJ = 1,2,3
# print(zhibox.MJ)


class Webopera:

    VERSION = '1.0'

    def __init__(self, url, token):
        self.url = url   #url 统一资源定位符 （唯一性）
        self.token = token #身法验证用，必须要有的

    def login(self):
        print('{}/{} login page'.format(self.url, self.token))

    def logout(self):
        print('{}/{} logout page'.format(self.url, self.token))

    @staticmethod
    def welcome(content):
        print('''Welcome to Webopera
        {}'''.format(content))


# hasattr()查询对象中的方法,返回bool值
web = Webopera('www.qfcloud.com', 'login')
result = hasattr(web, 'logout')    ##检查实例中有没有匹配的方法
print(result)        ##布尔值输出

# getattr()获取对象中的方法,利用字符串获取其中的方法,用变量接收
variable = getattr(web, 'welcome')			##获得值   实例名，方法名
variable('execute successfully')
#
# setattr()设置对象中的属性
setattr(web, 'content', 'opera setattr method successfully')  ##实例名，属性名，属性值
print(web.content)

# # delattr()删除对象中的属性
# delattr(web, 'content')
# print(web.content)

