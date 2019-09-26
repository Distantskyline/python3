import paramiko
def yuancheng():
    key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport(('192.168.52.134',22))
    transport.connect(username='root',pkey=key)

    client = paramiko.SSHClient()
    client._transport= transport
    _,stdout,_ = client.exec_command('python3 /root/info/main.py')
    transport.close()


