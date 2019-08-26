import fnmatch
# import os
# list = []
# for a,b,c in os.walk('../python_jinjie'):
#     list.extend(c)
# print(list)


import psutil

print('CPU的核心数： '.format(psutil.cpu_count(logical=True)))
