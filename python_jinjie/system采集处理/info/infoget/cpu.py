import  psutil
def cpuinfo():
    cpuinfo1 = psutil.cpu_times_percent(interval=1,)
    cpuinfo = str(cpuinfo1.system+cpuinfo1.user)
    return cpuinfo


