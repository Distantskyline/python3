#!/usr/bin/env python3
#
#author:Distantskyline
#date:190821-20:44
#usage:

# ##                        密码链接远程服务器
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname='192.168.52.135',
    port=22,
    username='root',
    password='1'
)

stdin , stdout , stderr = client.exec_command(command='ls',timeout=2)
print(stdout.read().decode('utf-8'))
client.close()

##                            密钥对链接远程
import paramiko
key = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname='192.168.52.135',
    port=22,
    username='root',
    pkey=key
)

stdin , stdout , stderr = client.exec_command('ls')
print(stdout.read().decode('utf-8'))
client.close()


##                                 通过通道链接远程主机
import paramiko
key = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')
transport = paramiko.Transport(('192.168.52.135',22))
transport.connect(username='root',pkey=key)
client = paramiko.SSHClient()
client._transport = transport
stdin , stdout, stderr = client.exec_command('ls')
print(stdout.read().decode('utf-8'))
transport.close()

## 传输文件，目标地址要 对应起名  命名
import paramiko
key = paramiko.RSAKey.from_private_key_file('')
transport = paramiko.Transport('',22)
transport.connect(username=' ',pkey=key)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('','')
sftp.get('','')
transport.close()


