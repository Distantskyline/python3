#!/usr/bin/env python3
#
#date:190819
#author:Distantskyline
#usage:


# import fnmatch
# import os
#
# files, picture = [], ('*.jpeg','*.png','*.gif','*.jpg')
# for test in picture:
#     reslut = fnmatch.filter(os.listdir('file'),test)
#     files.extend(reslut)
# print(files)
#
# for files in os.listdir('file'):
#     for test in picture:
#         if fnmatch.fnmatch(files,test):
#             print(files)




# # ##                                        os.walk
# import fnmatch
# import os
# files, picture = [], ('*.jpeg','*.png','*.gif','*.jpg')
# for x,y,z in os.walk('file'):
#     for images in picture:
#         result = fnmatch.filter(z,images)
#         files.extend(result)
# print(x,y,z)

# ##                                            显示每个路径下的文件夹和文件个数
# files, picture = [], ('*.jpeg','*.png','*.gif','*.jpg')
# for x,y,z in os.walk('file'):
#     print(x,y,z)
#     print('''
#     x: {}
#     y: {}
#     z: {}'''.format(x,len(y),len(z)))


##                         学sysexit
# import sys
#
# sys.exit(97)
# print(123)
#
# sysExit.py

##                         例子 退出码换成15
# import sys
#
# n = 0
# while n < 100:
#     if n == 5:
#         sys.exit(15)
#     print(n)
#     n += 1

