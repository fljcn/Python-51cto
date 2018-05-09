#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng
from .auth import authenticate
# from .utils import print_error
from .logger import logger
from atm import logics

transaction_logger = logger("transaction")
access_logger = logger("access")

features = [
    ('账户信息',logics.view_account_info),
    ('取现',logics.with_draw),
    ('还款',logics.pay_back),
]


def controller(user_obj):
    """功能分配"""
    while True:
        for index,feature in enumerate(features):
            print(index,feature[0])
        choice = input("ATM>>:").strip()
        if not choice:continue
        if choice.isdigit():
            choice = int(choice)
            if choice < len(features) and choice >= 0:
                features [choice][1](user_obj, transaction_logger = transaction_logger, access_logger = access_logger)
        if choice == 'exit':
            exit("Bye.")

def entrance():
    """ATM程序交互入口"""

    user_obj = {
        'is_authenticated':False,  # 用户是否已认证
        'data':None
    }

    retry_count = 0
    while user_obj['is_authenticated'] is not True: #没认证
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth_data = authenticate(account,password)  #验证  调用auth.py 中 authenticate函数
        if auth_data:
            # 已经拿到账户数据 auth_data
            user_obj['is_authenticated'] = True
            user_obj['data'] = auth_data
            print("welcome")
            access_logger.info("user %s just logged in " % user_obj['data']['id'])   #logger

            controller(user_obj)

        else:
            print_error('Wrong username or password!')
        retry_count += 1