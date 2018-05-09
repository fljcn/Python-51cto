#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

import logging,os
from conf import settings


def logger(log_type):

    #建立logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    log_file = os.path.join(settings.LOG_PATH, settings.LOG_TYPES[log_type]) #结合目录与文件名，写到对应文件
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    formatter = settings.LOG_FORMAT

    # 增加格式到fh
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger