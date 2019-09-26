import json
import requests


token = 'cbbd08495fc062a277f92478bc16b3cfc7738912c75b9d1619f1797e822a1d46'
api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
header = {'Content-Type': 'application/json'}
data = {
    "msgtype": "text",
    "text": {
        "content": "测试发送测试信息至钉钉群"
    },
    'at': {
        'atMobiles': [
            '13153315260',
            '15779847379'
        ]
    },
    'isAtAll': True,
}

sendData = json.dumps(data).encode('utf-8')
requests.post(url=api, data=sendData, headers=header)