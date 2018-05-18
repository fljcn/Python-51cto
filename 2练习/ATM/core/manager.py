# -*- coding:utf-8 -*-
import os
import json
import string
import random
from hashlib import md5

from .logger import set_logger
from .main import judge_num
from .db_handler import account_data_save
from .auth import(
    login, judge_account, auth_login
)
from conf.settings import(
    MANAGER_ID, DATABASE, DEFAULT_ACCOUNT
)

manager_logger = set_logger('manager')


def set_salt():
    # 每个用户的salt值不一样 库中的password就不一样
    salt = ''.join(random.sample(string.digits + string.ascii_letters + string.punctuation, 8))  # 随机的8位盐 使得相同的密码 也有不同md5()值
    md5_value = md5()
    md5_value.update(b'123' + salt.encode('utf-8'))
    return salt, md5_value.hexdigest()


def get_account():
    # 输入 id 得到账户信息
    while True:
        id_account = input('id>>>:').strip()
        if id_account.isdigit():
            account_date = judge_account(id_account)
            if account_date:
                return account_date, id_account
            else:
                print('\033[1;31m账号：%s 不存在\033[0m' % id_account)
        else:
            print('\033[1;31m请输入整数的 id 账户\033[0m')


@auth_login
def add_acount(m_account_info):
    # 添加账户
    print('\033[1;34m管理员 %s 开始添加账户\033[0m'.center(30, '-') % m_account_info['account'])
    while True:
        id_account = input('id>>>:').strip()
        if id_account.isdigit():
            account_date = judge_account(id_account)
            if account_date:
                print('\033[1;31m账号：%s 已存在\033[0m' % id_account)
            else:
                salt_pass = set_salt()
                DEFAULT_ACCOUNT['id'] = int(id_account)
                DEFAULT_ACCOUNT['password'] = salt_pass[1]
                DEFAULT_ACCOUNT['salt'] = salt_pass[0]
                with open(os.path.join(DATABASE['path'], id_account + '.json'), 'w', encoding='utf-8') as f:
                    json.dump(DEFAULT_ACCOUNT, f)
                print('\033[1;32m账号：%s 添加成功\033[0m' % id_account)
                manager_logger.info('管理员account：%s - 添加账户account：%s' % (m_account_info['account'], id_account))
                break
        else:
            print('\033[1;31m请输入整数的 id 账户\033[0m')


@auth_login
def credit_account(m_account_info):
    # 设定用户 额度
    account_tuple = get_account()
    if account_tuple:
        credit = input('new_credit>>>:').strip()
        float_credit = judge_num(credit)
        if float_credit:
            account_tuple[0]['credit'] = round(float_credit, 2)
            account_data = account_data_save(account_tuple[1], account_tuple[0])
            if account_data:
                print('修改账号: \033[1;33m%s\033[0m 额度成功，现在额度为：\033[1;34m%s\033[0m' % (account_tuple[1], account_data['credit']))
                manager_logger.info('管理员account：%s - 修改账号account：%s - 修改额度credit：%s' % (m_account_info['account'], account_tuple[1], float_credit))
            else:
                print('账号：%s 文件修改失败！' % account_tuple[1])
        else:
            print('\033[1;31m注意：用户额度须为整数或小数\033[0m')


@auth_login
def freeze_account(m_account_info):
    # 冻结账户
    account_tuple = get_account()
    if account_tuple:
        if account_tuple[1] == m_account_info['account']:  # 是管理员 本人
            print('\033[1;31m您是管理员，不能冻结自己！\033[0m')
        else:
            if account_tuple[0]['status'] == 1:
                print('账号是 \033[1;32m冻结\033[0m 状态，将 \033[1;34m解冻\033[0m')
                account_tuple[0]['status'] = 0
            else:
                print('账号是 \033[1;32m解冻\033[0m 状态，将 \033[1;34m冻结\033[0m')
                account_tuple[0]['status'] = 1
            account_data = account_data_save(account_tuple[1], account_tuple[0])
            if account_data:
                print('\033[1;33m修改账号的 冻结状态：%s 成功！\033[0m' % (account_tuple[1]))
                manager_logger.info('管理员account：%s - 修改账号account：%s - 修改冻结状态成功' % (m_account_info['account'], account_tuple[1]))
            else:
                print('账号：%s 文件修改失败！' % account_tuple[1])


def quit_func(m_account_info):
    # 退出
    exit('bye bye ...')


def controller(m_account_info):
    # 功能分发器
    print('\033[1;33m欢迎管理员 %s 登录\033[0m'.center(35, '-') % m_account_info.get('account'))
    manager_choice = '''
    ------start------
    1. 添加账户
    2. 用户额度
    3. 冻结账户
    4. 退出
    ------end------
    '''
    dict_manager_info = {'1': add_acount,
                         '2': credit_account,
                         '3': freeze_account,
                         '4': quit_func}
    while True:
        print(manager_choice)
        num = input('num>>>:').strip()
        if not num:
            continue
        if num in dict_manager_info:
            dict_manager_info[num](m_account_info)
        else:
            print('\033[1;31m请重新选择\033[0m')


def run():
    manager_account_info = login(manager_logger, MANAGER_ID)
    if manager_account_info:
        controller(manager_account_info)