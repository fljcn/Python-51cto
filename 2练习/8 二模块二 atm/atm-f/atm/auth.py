#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

from .db_handler import load_account_data
# from .utils import print_error

def authenticate(account,password):
    """对用户信息进行验证"""
    account_data = load_account_data(account)
    if account_data['status'] == 0:  #账户文件加载成功
        account_data = account_data['data']  #真正的用户数据
        if password == account_data['password']:   #认证成功
            return account_data
        else:
            return None
    else:
        return None