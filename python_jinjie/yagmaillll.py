import yagmail


# 建立发送客户端
sendClient = yagmail.SMTP(user='zhanggengheng@qq.com',
                          password='pisyxyormpblgbei',
                          host='smtp.qq.com')
# 创建邮件正文
contents = [
    'this is test message.',
    'please ~ not use callback.'
]
# 发送邮件并添加附件
sendClient.send(to=['hfxzhanggengheng@163.com'],
                subject='[python]Test email send',
                contents=contents
               )