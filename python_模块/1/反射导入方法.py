#!/usr/bin/env python3
#
#date:190819
#author:Distantskyline
#usage:


###                                     f反射导入方法
variable = __import__('python_模块.wheel.log_analysis',fromlist=True)

gongneng = input('gongneng: ')
# fangfa = input('')

if hasattr(variable,gongneng):
    func = getattr(variable,gongneng)
    ips1 = func('../wheel/access_log')
    print(ips1)

###                                   from导入模块方法
from python_模块.wheel import log_analysis

ipslist = log_analysis.loganalysis('../wheel/access_log')
print(ipslist)