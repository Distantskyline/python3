import time
from python3do import yuancheng
import pymysql

yuancheng()
client = pymysql.connect(
    host = '192.168.52.134',
    user = 'zgh',
    password = '(123!@#)',
    db = 'sysinfo'
)

with client.cursor() as cursors:
    select = "select {} from {};"
    database = (('cpu','cpuinfo'),('memory','memoryinfo'),('disk','diskinfo'))
    for y,x in database:
        cursors.execute(select.format(x,y))
        z = cursors.fetchall()
        # print(z)
        if y =='cpu':
            if float(z[-1][0])>15:
                print('报警')
                print(z)
        if y =='memory':
            if float(z[-1][0])>10:
                print('报警 ')
        if y =='disk':
            if float(z[-1][0])>20:
                print('报警')
client.close()