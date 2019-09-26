import paramiko

def transport(path):
    key = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport((path,22))
    transport.connect(username='root',pkey=key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(r'two\info.py','/root/info.py')
    transport.close()

# transport('192.168.52.134')

def cron(path):
    key = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')
    transport = paramiko.Transport((path,22))
    transport.connect(username='root',pkey=key)
    client = paramiko.SSHClient()
    client._transport = transport

    _,stdout,_ = client.exec_command( "echo ' */5 * * * *  /usr/local/bin/python3.7 /root/info.py &' >> /var/spool/cron/root")
    transport.close()

# cron('192.168.52.134')