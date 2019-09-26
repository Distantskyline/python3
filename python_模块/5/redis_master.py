from redis import sentinel
import redis
import logging.config


logging.config.fileConfig('./logging_conf')
stinel = sentinel.Sentinel([('192.168.52.134',26379)])

try:
    master = stinel.discover_master('mymaster')
    print(master)
except redis.sentinel.MasterNotFoundError as error:
    logging.getLogger('rotate')
    logging.error(error)
finally:
    master = stinel.discover_master('mymaster')
    if master != ('192.168.52.134',6380):
        logging.warning('master on {}'.format(master))