# -*- coding:utf-8 -*-
import os
import json
from hashlib import md5

from conf.settings import DATABASE


def auth_login(func):
    # 装饰器
    def inner(*args, **kwargs):
        if args[0]['is_auth']:
            return func(*args, **kwargs)
        else:
            exit('您还未登录！')
    return inner


def hash_password(password, salt):
    # 用户输入的密码 + salt 得到hash值 ,salt 增加密码安全性
    hash_value = md5()
    hash_value.update((password+salt).encode('utf-8'))
    return hash_value.hexdigest()


def judge_account(account):
    # 判断用户是否存在 存在返回json数据
    path_json = DATABASE['path']
    file_path = os.path.join(path_json, account+'.json')
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            account_data = json.load(f)
            print("account_data_judge_f:", account_data)
            f.close()
            return account_data


def login(logger, *args):
    # 判断账号密码是否正确
    account_info = {
        'is_auth': False,
        'account': None,
        'account_data': None
    }
    login_count = 0
    while login_count < 3:
        account = input('\033[1;32maccount>>>:\033[0m').strip()
        password = input('\033[1;32mpassword>>>:\033[0m').strip()
        account_data = judge_account(account)   #取得账户信息
        print("account_data_login_f:", account_data)
        if account_data:
            if account_data.get('password') == hash_password(password, account_data['salt']):
                # print('\033[1;33m登录成功！\033[0m'.center(25, '-'))
                account_info['is_auth'] = True
                account_info['account'] = account
                account_info['account_data'] = account_data    # 获取到账户数据
                if account_data['status'] == 1:  # 表示账号 被冻结
                    print('\033[1;31m账号:%s 被冻结！\033[0m'.center(30, '-') % account)
                else:
                    if len(args) != 0:  # 管理员
                        if args[0] == account:
                            logger.info('管理员account: %s - 登录成功' % account)
                            return account_info
                        else:
                            print('\033[1;31m您不是管理员！\033[0m'.center(25, '-'))
                    else:  # 普通账号
                        logger.info('account: %s - 登录成功' % account)
                        return account_info
            else:
                print('\033[1;31m密码错误！\033[0m'.center(25, '-'))
        else:
            print('\033[1;31m账号:%s 不存在\033[0m' % account)
        login_count += 1
    else:
        logger.critical('account: %s - 登录失败次数超过3次' % account)
        exit()