import  psutil
def cpuinfo():
    cpuinfo1 = psutil.cpu_times_percent(interval=1, )
    # print(cpuinfo1)
    cpuinfo = str(cpuinfo1.system+cpuinfo1.user)
    print(cpuinfo)
    return cpuinfo

# cpuinfo()