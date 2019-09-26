#!/usr/bin/env python3
#
#author:Distantskyline
#date:190812
#usage:zhuangshiqitest
#


# #验证登录界面
username = ['tom','jerry','jack']
password = {'tom': '123','jerry': 'abc','jack': 'qwe'}

def load(func):
    def wrapper(user,passwd):
        if user in username and password[user] == passwd:
            print('验证成功')
            func(user,passwd)
        else:
            print('Flase')
    return wrapper

@load
def denglu(user,passwd):
    print('登录页面')


@load
def yanzheng(user,passwd):
    print('验证页面')


shuru = input('页面几？' )
u = input('user: ' )
p = input('passwd:' )

if shuru == 'denglu':
    denglu(user=u,passwd=p)
elif shuru =='yanzheng':
    yanzheng(user=u,passwd=p)
else:
    print('False')


#实现加法 乘法
# def addr(n):
#     if n==0:
#         return n
#     return n+addr(n-1)
# b = addr(15)
# print(b)
#
# def eddr(n):
#     if n==1:
#         return n
#     return n * eddr(n-1)*1000
#
# a = eddr(517)
# print(a)



# #页面寻找
#
users = ['tom','jack','alice']
passwd = {'tom': '123','jack': 'qwe','alice': 'zxc'}

def waibu(cj):
    def neibu(user,password):
        if user in users and passwd[user] == password:
            print('账号密码验证成功')
            cj(user,password)
        else:
            print('验证失败')
    return neibu

@waibu
def login(user,password):
    print('登录页面')

@waibu
def check(user,password):
    print('验证页面')

a = input('请输入页面:')
b = input('user:')
c = input('password:')

if a == 'login':
    login(user=b,password=c)
elif a == 'check':
    check(user=b,password=c)
else:
    print('页面输入错误')




# ##
# #who are you？
# import functools
# def dectorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('decorator this {}()',format(func))
#         func(*args,**kwargs)
#         print('end.')
#     return wrapper
#
# @dectorator
# def test1(parm,location):
#     print('i come from {} or {}'.format(parm,location))
#
# print(test1.__name__)
# print(help(test1))


##
# #计算系统工作的时间差
#
# import time
# def wb(func):
#     def nb(*args,**kwargs):
#         a = time.perf_counter()
#         func(*args,**kwargs)
#         b = time.perf_counter()
#         print('时间差是：{:f}'.format( b - a ))
#     return nb
#
# @wb
# def test001(bl):
#     if bl > 1:
#         list001 = [(lambda x: x**2)(x) for x in range(1-bl)]
#         return list001
#     else:
#         print('bl错误')
#
# test001(5)
#
#
# def myDecorator(func):
#     def wrapper(7):
#         print('use decorator...')
#         func(message)
#     return wrapper
#
#
# @myDecorator
# def greet(info):
#     print(info)
#
#
# greet('hello world')