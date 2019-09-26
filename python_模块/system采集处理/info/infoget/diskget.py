import psutil

def diskinfo():
    diskinfo1 =psutil.disk_usage('/')
    diskinfo = str(diskinfo1.percent)
    # print(diskinfo)
    return diskinfo
# diskinfo()