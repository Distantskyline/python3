#!/usr/bin/env python3
#
#author:Distantskyline
#date；190821-19:15
#usage:

import logging.config    ##加载自定义的配置文件

logging.config.fileConfig('logging_conf')  ##自定义配置文件的路径地址

try:
    var01, var02 = 'hello', 18
    print(var01 + var02)
except Exception as error:
    logger = logging.getLogger('rotateSize')
    logger.error(error)
finally:
    pass

print('go on...')