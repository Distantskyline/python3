from infoget import cpu
from infoget import diskget
from infoget import memoryget
import pymysql
import time
import subprocess

client = pymysql.connect(
    host = '192.168.52.134',
    user = 'zgh',
    password = '(123!@#)',
    db = 'sysinfo'
)
with client.cursor() as cursors:
    hostname = subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
    insert = "insert into cpu values({},'{}',{});"
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        cpu.cpuinfo())
    )
    client.commit()
with client.cursor() as cursors:
    hostname = subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
    insert = "insert into memory values({},'{}',{});"
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        memoryget.memoryinfo())
    )
    client.commit()
with client.cursor() as cursors:
    hostname = subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
    insert = "insert into disk values({},'{}',{});"
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        diskget.diskinfo())
    )
    client.commit()
client.close()
