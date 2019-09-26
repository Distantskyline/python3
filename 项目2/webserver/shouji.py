import paramiko

def shouji(logpath):
    key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport(('192.168.52.134',22))
    transport.connect(username='root',pkey=key)
    sftp= paramiko.SFTPClient.from_transport(transport)
    sftp.get('/root/access_log',logpath)
    transport.close()


# shouji()