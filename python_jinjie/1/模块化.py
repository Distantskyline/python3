#!/usr/bin/env python3
#
#date:190819
#author:Distantskyline
#usage:

# variable = __import__('python_jinjie.wheel.log_analysis',fromlist=True)
#
# gongneng = input('gongneng: ')
# # fangfa = input('')
#
# if hasattr(variable,gongneng):
#     func = getattr(variable,gongneng)
#     ips1 = func('../wheel/access_log')
#     print(ips1)

from python_jinjie.wheel import log_analysis

ipslist = log_analysis.loganalysis('../wheel/access_log')
print(ipslist)