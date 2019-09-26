import psutil
import time
import json
import pymysql
import subprocess
def cpu():
    cpu = psutil.cpu_times_percent(interval=1,)
    cpuinfo = str(cpu.user+cpu.system)
    return cpuinfo


def memory():
    memory = psutil.virtual_memory()
    meminfo = str(memory.percent)
    return meminfo


def disk():
    disk = psutil.disk_usage('/')
    diskinfo = str(disk.percent)
    return diskinfo

date = time.strftime('%Y%m%d-%H%M%S')
data = {'time': date,'cpu': cpu(),'memory': memory(),'disk': disk()}
print(data)
with open(file='/root/log.json',mode='a',encoding='utf8')as file:
    file.write(json.dumps(data))
    file.write('\n')


client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '(123!@#)',
    db = 'sysinfo')

date = time.strftime('%Y%m%d.%H%M%S')

with client.cursor() as cursor:
    hostname = subprocess.run('hostname', shell=True, stdout=subprocess.PIPE)
    insert = "insert into cpu values ({},'{}',{})"
    cursor.execute(insert.format(
        date,hostname.stdout.decode('utf-8').rstrip('\r\n'),cpu()
    ))
    cursor.close()
with client.cursor() as cursor:
    hostname = subprocess.run('hostname', shell=True, stdout=subprocess.PIPE)
    insert = "insert into memory values ({},'{}',{})"
    cursor.execute(insert.format(
        date,hostname.stdout.decode('utf-8').rstrip('\r\n'),memory()
    ))
    cursor.close()
with client.cursor() as cursor:
    hostname = subprocess.run('hostname', shell=True, stdout=subprocess.PIPE)
    insert = "insert into disk values ({},'{}',{})"
    cursor.execute(insert.format(
        date,hostname.stdout.decode('utf-8').rstrip('\r\n'),disk()
    ))
    cursor.close()
client.commit()
client.close()


