from program2.webserver import serverinfo
from program2.webserver import shouji
import logging.config
import pymysql
import time
import json
import requests

# 获取远程 主机log信息
def getlog(logpath):
    shouji.shouji(logpath)

#log 本地文件 添加
def log(logpath,logconfpath):
    logging.config.fileConfig(logconfpath)
    logger = logging.getLogger('rotate')
    ips = serverinfo.ips(logpath)
    stats = []
    stat = serverinfo.stat(logpath)
    for x in stat.values():
        stats.append(x)
    pv,uv =serverinfo.puv(logpath)
    logger.warning('ip前三名- {} - {} -- {} - {} -- {} - {} --状态码出现次数 200: {} -- 404: {} -- 502： {} -- 503： {} --pv量： {} --uv量： {}'.format(ips[0][0],ips[0][1],ips[1][0],ips[1][1],ips[2][0],ips[2][1],stats[0],stats[1],stats[2],stats[3],pv,uv))

#远程主机添加数据库
def mysql(logpath):
    client = pymysql.connect(
        host = '192.168.52.134',
        user = 'zgh',
        password = '(123!@#)',
        db = 'loginfo')
    #ips 前4
    ips = serverinfo.ips(logpath)
    ips1 = str(ips[0][0]) + '-' + str(ips[0][1])
    ips2 = str(ips[1][0]) + '-' + str(ips[1][1])
    ips3 = str(ips[2][0]) + '-' + str(ips[2][1])
    #状态码
    stats = []
    stat = serverinfo.stat(logpath)
    for x in stat.values():
        stats.append(x)
    #puv
    pv, uv = serverinfo.puv(logpath)

    with  client.cursor() as cursors:
        insert = "insert into ips values ({},'{}','{}','{}');"
        cursors.execute(insert.format(time.strftime('%Y%m%d%H%M%S'),ips1,ips2,ips3))
        cursors.close()
    with client.cursor() as cursors:
        insert = 'insert into stats values ({},{},{},{},{});'
        cursors.execute(insert.format(time.strftime('%Y%m%d%H%M%S'),stats[0],stats[1],stats[2],stats[3]))
        cursors.close()
    with client.cursor() as cursors:
        insert = 'insert into puv values ({},{},{});'
        cursors.execute(insert.format(time.strftime('%Y%m%d%H%M%S'),pv,uv))
        cursors.close()
    client.commit()
    client.close()
    print('successfull')

#钉钉
def dingding(logpath):
    # ips 前4
    ips = serverinfo.ips(logpath)
    ips1 = str(ips[0][0]) + '-' + str(ips[0][1])
    ips2 = str(ips[1][0]) + '-' + str(ips[1][1])
    ips3 = str(ips[2][0]) + '-' + str(ips[2][1])
    # 状态码
    code = serverinfo.dingding('./log/loginfo.log')


    # puv
    pv, uv = serverinfo.puv(logpath)

    token = 'cbbd08495fc062a277f92478bc16b3cfc7738912c75b9d1619f1797e822a1d46'
    api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
    header = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "ipstop1-{}\nipstop2-{}\nipstop3-{}\nstat-{}\npv: {}\nuv: {}".format(ips1,ips2,ips3,code,pv,uv)
        },
        'at': {
            'atMobiles': [
                '13153315260'
            ]
        },
        'isAtAll': False
    }
    sendData = json.dumps(data).encode('utf-8')
    requests.post(url=api, data=sendData, headers=header)



# getlog('./log/access.log')
# log('./log/loginfo.log','./logging.conf')
# mysql('./log/loginfo.log')
# dingding('./log/loginfo.log')

# code = serverinfo.dingding('./log/loginfo.log')
# print(code)