#!/usr/bin/env python3
#
#date:190813
#author:Distantskyline
#usage:

                                                  #纸盒子
# class Box:
#     def __init__(self,length,width,height):
#         print('was called...')
#         self.length = length
#         self.width = width
#         self.height = height
#
#     def getvolue(self):
#         volue = self.length * self.width * self.height
#         return volue
#
#
# paperBox = Box(1,5,8)
#
# papervolue = paperBox.getvolue()
# print(papervolue)



                                          # # 计算盒子的体积 长* 宽* 高
# class Box:
#     def __init__(self,chang,kuan,gao):
#         self.chang = chang
#         self.kuan = kuan
#         self.gao = gao
#
#     def jisuan(self):
#         jieguo = self.chang * self.kuan * self.gao
#         return jieguo
#
# tieBox = Box(10,10,11)
#
# JG = tieBox.jisuan()
# print(JG)




                                         # # 计算三角形面积
                                         # #三角形有初始值
# class three:
#     def __init__(self):
#         self.di = 10
#         self.gao = 16
#
#     def jisuan(self):
#         mianji = (self.di *self.gao)/ 2
#         return mianji
# Three = three()
#
# JG = Three.jisuan()
# print(JG)



                                              # #计算梯形面积
# class tixing:
#     def __init__(self,xiadi,shangdi,gao):
#         self.xiadi = xiadi
#         self.shangdi = shangdi
#         self.gao = gao
#     def jisuan(self):
#         mianji1 = (self.xiadi + self.shangdi) * self.gao
#         mianji2 = mianji1 /2
#         return mianji2
#
# tx = tixing(10,5,10)
# mj = tx.jisuan()
# print(mj)
                                    # #更改梯形的值重新计算
# tx.shangdi = 100
# tx.xiadi = 50
# tx.gao = 100
# mj2 = tx.jisuan()
# print(mj2)



#                                 # # 系统常量
# class Box:
#     VERSION = 'TEXT 专用:'
#     def __init__(self,chang,kuan,gao):
#         self.chang = chang
#         self.kuan = kuan
#         self.gao = gao
#
#     def JSM(self):
#         MJ1 = self.chang * self.gao + self.kuan * self.gao
#         MJ2 = self.chang * self.kuan
#         MJ3 = (MJ1 +MJ2)*2
#         return MJ3
#     def JST(self):
#         TJ = self.chang * self.kuan * self.gao
#         return TJ
#
# paperBox = Box(10,15,20)
# MJ = paperBox.JSM()
# TJ = paperBox.JST()
# print('面积：' ,MJ)
# print('体积：', TJ)


ips = []
with open('./log/access_log', 'r', encoding='utf8') as logfile:
    for lines in logfile:
        ips.append(lines.split("=")[3].split()[0])

print('PV is {}'.format(len(ips)))
print('UV is {}'.format(len(set(ips))))