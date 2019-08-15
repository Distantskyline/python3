# #!/usr/bin/env python3
# #
# #author:Distantskyline
# #date:1908090
# #usage:
#
#
# import os
# # a = os.getcwd()
# # print(a)
# #
# # b = os.listdir('G:\pycharm学习\day4')
# # print(b)
# #
#
dictC = fileC = 0
def getCount(path):
    for file in os.listdir(path):
        fileabs = os.path.join(path,file)
        if os.path.isdir(fileabs):
            global dictC
            dictC += 1
            getCount(fileabs)
        else:
            global fileC
            fileC += 1
    return dictC,fileC
dictC,fileC = getCount('G:\pycharm')
print('{} D,{} F'.format(dictC,fileC))

df = f = 0
def fff (path):
    for ff in os.listdir(path):
        fabs = os.path.join(path,ff)
        if os.path.isdir(fabs):
            global df
            df += 1
            fff(fabs)
        else:
            global f
            f += 1
    return df,f
df,f = fff('G:\pycharm学习')
print('{}目录,{}文件'.format(df,f))


# listA = [1,2,3,4,5,'string','hello',True]
#
# for element in listA:
#     if type(element) in {int,str}:
#         print(element)
#     else:
#         print('ERROR')

list = [1,2,3,4]
# list01 = []
# def addr(list,index):
#     list01.append(list[index])
#     if index == 0:
#         print(list01)
#     return addr(list,index-1)
# addr(list,len(list)-1)
list02 = [5,6,7]
list.extend(list02)
print(list)
a = list02[2]
print(a)