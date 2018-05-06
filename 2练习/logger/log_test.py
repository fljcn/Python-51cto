#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

import logging
# logging.warning('user [alex] attempted wrong password more than 3 times')
# logging.critical('server is down')
# logging.c

import logging

logging.basicConfig(filename='example.log',
                    level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s %(thread)d %(message)s',
                    datefmt='%y-%m-%d %I:%M:%S %p')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')