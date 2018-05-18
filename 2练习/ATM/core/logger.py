# -*- coding:utf-8 -*-
import os
import logging
from logging import handlers

from conf.settings import(
    LOG_LEVEL, BASE_DIR, LOG_FORMATTER
)


def set_logger(name):
    # 配置logger对象
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # fh = logging.FileHandler(os.path.join(BASE_DIR, 'log/'+name+'.log'), encoding='utf-8')
    # fh = handlers.RotatingFileHandler(filename = os.path.join(BASE_DIR, 'log/'+name+'.log'), maxBytes=10, backupCount=2, encoding='utf-8')
    fh = handlers.TimedRotatingFileHandler(filename = os.path.join(BASE_DIR, 'log/'+name+'.log'), when='S', interval=2, backupCount=2, encoding='utf-8')
    logger.addHandler(fh)

    fh_formatter = LOG_FORMATTER
    fh.setFormatter(fh_formatter)

    return logger