#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng
# https://www.luffycity.com/python-book/di-4-zhang-python-ji-chu-2014-chang-yong-mo-kuai/logging-mo-kuai.html  教材

#默认级别按全局的确定后，再按handler中设置的
#如果没有全局，默认按WARNING级别
#全局设置DEBUG后，console handler设置为INFO,如果输出的日志级别是debug，那就不会在屏幕上显示

import logging
from logging import handlers

#启用filter，很少用
class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return "db backup" in record.getMessage()    #not in 指日志中不包含的记录，in指日志中包括的记录

# 1.生成logger对象  每个程序在输出信息之前都要获得一个Logger。Logger通常对应了程序的模块名
logger = logging.getLogger("web")  #对应程序模块名
logger.setLevel(logging.DEBUG)     #定义级别--全局

# 1.1 把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

# 2.生成handler对象，handler对象负责发送相关的信息到指定目的地
ch = logging.StreamHandler()    #屏幕
ch.setLevel(logging.DEBUG)       #
# fh = logging.FileHandler("web.log")    #文件
#按文件大小截断
# fh = handlers.RotatingFileHandler( "web.log", maxBytes=10, backupCount=3)

#按时间截断
fh = handlers.TimedRotatingFileHandler("web.log", when="S", interval=5, backupCount=3)
# handlers.TimedRotatingFileHandler(filename=log_file, when="S", interval=5, backupCount=3)

fh.setLevel(logging.WARNING)

# 2.1把handler对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

# 3.生成formatter对象
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d- %(message)s')   #屏幕
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')    #文件

# 3.1把formatter对象绑定handleler对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)



logger.debug("test log db backup 3 ")
logger.warning("test log db backup 3")   # 默认日志级别warning
logger.info("test log db backup 4")
logger.error("test log")