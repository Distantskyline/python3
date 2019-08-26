import psutil
def memoryinfo():
    memoryinfo1 = psutil.virtual_memory()
    memoryinfo = str(memoryinfo1.percent)
    return memoryinfo
