#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

import

def view_account_info(account_data,*args,**kwargs):
    """查看账户状态"""
    print("view_account_info",account_data,kwargs)
    trans_logger = kwargs.get("transaction_logger")
    print("ACCOUNT INFO".center(50,'-'))
    for k,v in account_data['data'].items():
        if k not in ('password',):
            print("%15s:%s"%(k,v))
        print("END".center(50,'-'))

# def with_draw(account_data,*args,**kwargs):

# def pay_back(account_data,*args,**kwargs):