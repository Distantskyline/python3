import paramiko


def gets():
    key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport(('192.168.52.134',22))
    transport.connect(username='root',pkey=key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get('/var/log/monitor.log','./monitor.log')
    transport.close()

def put1():
    key =  paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport(('192.168.52.134',22))
    transport.connect(username='root',pkey=key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('./jihua.sh','/root/jihua.sh')
    transport.close()

def put2():
    key =  paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport(('192.168.52.134',22))
    transport.connect(username='root',pkey=key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('./info.sh','/tasks/info.sh')
    transport.close()

def jihua():
    key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport(('192.168.52.134',22))
    transport.connect(username='root',pkey=key)

    client = paramiko.SSHClient()
    client._transport =transport
    client.exec_command('bash /root/jihua.sh')
    client.close()


put1()

