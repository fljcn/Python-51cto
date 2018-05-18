# -*- coding:utf-8 -*-
import os
import logging
import time
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine:': 'file_storage',
    'path': os.path.join(BASE_DIR, 'db/accounts')  #路径组合
}

LOG_LEVEL = logging.INFO
LOG_FORMATTER = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')

TRANSACTION_TYPE = {
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'pay_back': {'action': 'plus', 'interest': 0},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0}
}

GOODS = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

MANAGER_ID = '999'

datetime_tmp = datetime.datetime.now().replace(year=2050, month=1, day=1)
DEFAULT_ACCOUNT = {
    'id': 0,
    'password': '',
    'salt': '',
    'balance': 15000,
    'credit': 15000,
    'enroll_date': time.strftime('%Y-%m-%d', time.localtime()),
    'expire_date': '%s-%s-%s' % (datetime_tmp.year, datetime_tmp.month, datetime_tmp.day),
    'pay_day': 22,
    'status': 0
}