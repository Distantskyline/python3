#!/usr/bin/env python3
#
#author:Distantskyline
#date:190815
#usage:魔术方法


# class Box:
#     def __init__(self,l,w,h):
#         self.l = l
#         self.w = w
#         self.h = h
#
#     def __del__(self):
#         print('已经被删除了')
#
# del1 = Box(1,2,4)


##### __str__

# class Box:
#     def __init__(self,l,w,h):
#         self.l = l
#         self.w = w
#         self.h = h
#
#     def __str__(self):
#         return ('str has been used')
#
#     def hhh(self):
#         print('123')
#
# test01 = Box(1,2,4)
# print(test01)


##### __new__

class Document:
    def __new__(cls,*args,**kwargs):
        # print('new has been used')
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,path):
        print('init has been used')
        self.path = path

    def write(self,content):
        with open(self.path,'w',encoding='utf8')as file:
            file.writelines(content)

cfile = Document('file.txt')
cfile.write('''
    this is my first line.\n
    this is second line.\n
    this is third line.''')

file01 = Document('file01.txt')
file02 = Document('file02.txt')

print(id(file01))
print(id(file02))



#### __call__

class Document:
    def __init__(self,path):
        self.path = path

    def __call__(self, *args, **kwargs):
        print('call method execute successfully')

    def println(self):
        print('println method: {}'.format(self.path))

# book = Document('file.txt')
# book.println()

book = Document('file.txt')
book.println()
book()


# class Document:
#     def __init__(self, path):
#         print('Document class __init__ magic method.')
#         self.path = path
#
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def getContent(self):
#         with open(self.path, 'r', encoding='utf8') as file:
#             content = file.read()
#             return content
#
#
# class File(Document):
#     def __init__(self, path):
#         super(File, self).__init__(path)
#         print('File class __init__ magic method.')
#
#
# class Dir(File):
#     def __init__(self, path):
#         super(Dir, self).__init__(path)
#         print('dir class __init__ magic method.')
#
#
# class Configfile(Dir):
#     def __init__(self, path):
#         super(Configfile, self).__init__(path)
#         print('Configfile class __init__ magic method.')
#
#
# nginxFile = Configfile('file.txt')
# # content = nginxFile.getContent()
# # print(content)
# nginxFile.



