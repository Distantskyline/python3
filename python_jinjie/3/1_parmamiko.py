#!/usr/bin/env python3
#
#author:Distantskyline
#date:190821-11:21
#usage:

###                            基于密码链接
# import paramiko
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(
#     hostname= '192.168.52.135',
#     port=22,
#     username= 'root',
#     password= '1'
# )
#
# stdin, stdout ,stderr = client.exec_command(command='ls',timeout=0.03)
# print(stdout.read().decode('utf-8'))
# client.close()


###                            基于私钥链接
# import paramiko
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# private = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')
# client.connect(
#     hostname='192.168.52.135',
#     port=22,
#     username='root',
#     pkey=private
# )
# stdin, stdout, stderr = client.exec_command('hostname')
# print(stdout.read().decode('utf-8'))
#
# client.close()


##                            基于加密通道的形式传输
import paramiko

#  私钥的位置
private = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
transport = paramiko.Transport(('192.168.52.135',22))   #  链接的地址和端口
transport.connect(username='root', pkey=private)   #  链接的用户名和私钥
client = paramiko.SSHClient()    #  建立链接客户端
client._transport = transport   # 客户端通道 = 地址和端口 变量

stdin, stdout, stderr = client.exec_command('ls')
print(stdout.read().decode('utf-8'))
#关闭通道"
transport.close()


####                        使用通道的sftp服务下载上传文件
# import paramiko
# #  私钥的位置
# private = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
# transport = paramiko.Transport(('192.168.52.135',22))  #  链接的地址和端口
# transport.connect(username='root', pkey=private)       #  链接的用户名和私钥
# sftp = paramiko.SFTPClient.from_transport(transport)   #  链接的用户名和私钥
#
# sftp.put(r'本地路径', '远程路径加名字') #上传
# sftp.get('远程文件名字', r'本地路径')#下载
# #关闭通道"
# transport.close()