from program2.local import infohandle



##获取远程log文件存储到  指定目录

# infohandle.getlog('./log/access.log')

##将远程获取的log文件把过滤后的信息存储到本地文件中，前日志文件，后日志处理器文件

# infohandle.log('./log/loginfo.log','./logging.conf')

##将处理后的信息存储到数据库中，路径为日志文件

# infohandle.mysql('./log/loginfo.log')

##发送钉钉报警机器人

infohandle.dingding('./log/loginfo.log')