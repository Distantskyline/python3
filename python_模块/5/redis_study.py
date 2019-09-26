import redis
##                              建立连接池
##
pool = redis.ConnectionPool(host='192.168.52.132',port = 6379,db=0)
client = redis.Redis(connection_pool=pool)

# #                             字符串类型的创建删除
client.set(name='pycloud',value=17)
client.set(name=15,value=5)
client.mset({'a': 1,'b': 'hhh','c': 3})

x = client.get('15')
z = client.get('b')
y = client.mget('a','b','c')
print(x)
print(type(x))
client.delete('a','c')
z = client.get('b')
print(str(z,'utf8'))


##                           哈希表类型创建删除

pool = redis.ConnectionPool(host='192.168.52.132', port=6379, db=0)
client = redis.Redis(connection_pool=pool)

client.hset('pycloud1','user', 'phone')
info = client.hget('pycloud1', 'user')
print(str(info, 'utf8'))

# client.hmset('pycloud', {'user': 'bavduer', 'password': 123456, 'ipAddress': '192.168.161.10'})
# info = client.hmget('pycloud', 'user', 'password', 'ipAddress')
# print(info)



# 直接清除所有的缓存

client.flushdb(number-1)    #清除当前所指定的数据库(缓存位置)内的数据
#print()				    # - redis.conf里面记录的database number
client.flushall()	        #清除所有的数据(不分位置)