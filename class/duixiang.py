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