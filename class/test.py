# def PUV (path):
#     with open(file=path, mode='r', encoding='utf8') as log:
#         a = log.readlines()
#         print('PV量:',len(a))
#
#     ips = {}
#     with open(file=path, mode='r', encoding='utf8') as log:
#         for lines in log.readlines():
#             if lines.split()[0] not in ips.keys():
#                 ips.setdefault(lines.split()[0], 1)
#             else:
#                 ips[lines.split()[0]] += 1
#
#         ips = (sorted(ips.items(), key=lambda x: x[1], reverse=True))
#
#         print('UV量:',(len(list(ips))))
#         ips = dict((ips)[0:10])
#     # print((ips))
# PUV('./log/access_log')


#装饰器
users = ['tom','jack','alice']
password = {'tom': '1','jack': '2','alice': '3'}

def waibu(func):
    def neibu(user,passwd):
        if user in users and password[user] == passwd:
            print('密码验证正确')
            func(user,passwd)
        else:
            print('账号或密码不正确')
    return neibu

@waibu
def login(user,passwd):
    print('登录页面')

@waibu
def index(user,passwd):
    print('验证页面')

x = input('请输入去的页面： ')
user = input('user: ')
passwd = input('passwd: ')
if x == 'login':
    login(user=user,passwd=passwd)
elif x== 'index':
    index(user=user,passwd=passwd)
else:
    print('页面输入错误')

