import pymysql
import subprocess
import json
import requests
import time
## 获取远程监控信息，从数据库中读取并判断是否超过警戒线，然后钉钉报警
def mysql(path):
    client = pymysql.connect(
        host=path,
        user='zgh',
        password='(123!@#)',
        db='sysinfo')

    with client.cursor() as cursors:
        select = "select {},{},{} from {};"
        database = (( 'time','name','cpuinfo','cpu'),
                    ('time','name','memoryinfo','memory'),
                    ('time','name','diskinfo','disk')
                    )
        for date,name,info,table  in database:
            cursors.execute(select.format(date,name,info,table))
            z =(cursors.fetchall())
            # print(z)

            if table == 'cpu':
                a = float(z[-1][2])
                nowtime = float(z[0][0])
                hostname = str(z[0][1])
                if a > 0.5:
                    infocpu = [z[-1][0],hostname,'memory',b]
                    with open(file='..\one\log\log.txt',mode='a',encoding='utf8')as file:
                        file.write(json.dumps(infocpu))
                        file.write('\n')
                # print(a)
            if table =='memory':
                b = float(z[-1][2])
                if b > 25:
                    infomem = [z[-1][0],hostname,'memory',b]
                    with open(file='..\one\log\log.txt',mode='a',encoding='utf8')as file:
                        file.write(json.dumps(infomem))
                        file.write('\n')

                # print(b)
            if table == 'disk':
                c = float(z[-1][2])
                if c > 15:
                    infodisk = [z[-1][0],hostname,'disk',c]
                    with open(file='..\one\log\log.txt',mode='a',encoding='utf8')as file:
                        file.write(json.dumps(infodisk))
                        file.write('\n')
                # print(c)
        cursors.close()

    print(a,b,c,nowtime,hostname)
    daytime = time.strftime('%a')
    print(daytime)
    def dingding(x,y):
        token = 'cbbd08495fc062a277f92478bc16b3cfc7738912c75b9d1619f1797e822a1d46'
        api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
        header = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "text",
            "text": {
                "content": "{}机器在{}时刻报警:"
                           "{}达到了{}!，快去处理，不然工资扣光！".format(hostname,
                                                         nowtime,
                                                         x,
                                                         y)
            },
            'at': {
                'atMobiles': [
                '15079957171'

                ]
            },
            'isAtAll': True,
        }

        sendData = json.dumps(data).encode('utf-8')
        requests.post(url=api, data=sendData, headers=header)


    # if a> 0.5:
    #     dingding('cpu',a)
    # if b > 25:
    #     dingding('memory',b)
    # if  c > 15:
    #     dingding('disk',c)



mysql('192.168.52.134')



