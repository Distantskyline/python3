#!/usr/bin/env python
#
#author:Distantskyline
#date:19812
#usage:zhuangshiqi



# def myDecorator(func):
#     def wrapper ():
#         print('wrapper of decorator')
#         func()
#     return wrapper
#
# @myDecorator
# def greet():
#     print('hello world')
#
# Greet = myDecorator(greet)
# Greet()


# def jsq(func):
#     def dy(*args,**kwargs):
#         print('+-------+')
#         func(*args,**kwargs)
#         print('+-------+')
#     return dy
#
# @jsq
# def greet(name,class1):
#     print('|',name,class1,'|')
#
# greet('zgh',7)

# import functools
#
# def myDecorator(greet):
#     @functools.wraps(greet)
#     def wrapper(*args,**kwargs):
#         print('hello nihao')
#         func(*args,**kwargs)
#     return wrapper
# @myDecorator
# def greet(name,class2):
#     print(name,class2)
#
# print(greet.__name__)
# print(help(greet))

# import time
# import datetime

# altime = datetime.datetime.now()
# print(altime)
# print(altime.year,altime.month,altime.day,altime.hour,altime.minute,altime.second)

# first = time.perf_counter()
# listA = [x for x in range(10)]
# print(listA)
#
# end = time.perf_counter()
# print('时间差: {:f}'.format(end - first))

# with open(file='err0r.log',mode='w',encoding='utf8')as log:
#     log.write('{} [Error]:this opera must be allow''administrator'.format(datetime.datetime.now()
#     ))

# import time
# # a = time.time()
# # print(a)


#装饰器判断函数执行时间


import time
import functools

#
def waibu(func):
    @functools.wraps(func)
    def neibu(*args,**kwargs):
        a = time.perf_counter()
        func(*args,**kwargs)
        b = time.perf_counter()
        print('时间差: {:f}'.format(b - a))
    return neibu

@waibu
def jisuan(parm):
    a = parm + 11
    return a
    # print(a)
jisuan(100)
print(time.strftime('%Y'))

