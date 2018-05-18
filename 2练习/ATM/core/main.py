# -*- coding:utf-8 -*-
import re

from .logger import set_logger
from .db_handler import make_transaction
from .auth import (
    login, auth_login
)

access_logger = set_logger('access')


@auth_login
def checkout(account_info, money):
    # 购买商品之后 结账
    account_data = make_transaction(money, account_info, 'consume')
    if account_data:
        print('账户：%s ->> 消费 \033[1;34m%s\033[0m -> 余额 \033[1;31m%s\033[0m' % (account_info['account'], money, account_data['balance']))
        exit()
    else:
        print('\033[1;31m结账失败！\033[0m')


def judge_num(num):
    # 判断 int float
    str_num = re.sub('\.', '', num, count=1)    # 使用空，替换"."并只替换一次， 为isdigit()服务，如果有“.”不是数字
    if str_num.isdigit():
        return float(num)


@auth_login
def view_account(account_info):
    # 查看账户信息
    msg_info = '''\033[1;34m
    -----账户：%s 的信息：-----
    balance: %10s
    credit:  %10s
    pay_day: %10s\033[0m
    ''' % (account_info.get('account'),
           account_info['account_data']['balance'],
           account_info['account_data']['credit'],
           account_info['account_data']['pay_day'])
    print(msg_info)


@auth_login
def withdraw(account_info):
    # 提现
    while True:
        money = input('withdraw_money(q表示退出)>>>:').strip()
        if not money:
            continue
        if money == 'q':
            break
        float_money = judge_num(money)
        if float_money:
            account_data = make_transaction(float_money, account_info, 'withdraw')
            if account_data:
                print('账户：%s -> 提现成功 -> 提现 \033[1;34m%s\033[0m -> 余额 \033[1;31m%s\033[0m' % (account_info['account'], money, account_data['balance']))
            else:
                print('\033[1;31m提现失败！\033[0m')
        else:
            print('请输入\033[1;34m正确的\033[0m并\033[1;31m大于0\033[0m的金额'.center(45, '-'))


@auth_login
def pay_back(account_info):
    # 还款
    while True:
        money = input('pay_back_money(q表示退出)>>>:').strip()
        if not money:
            continue
        if money == 'q':
            break
        float_money = judge_num(money)
        if float_money:
            account_data = make_transaction(float_money, account_info, 'pay_back')
            if account_data:
                print('账户：%s -> 还款成功 -> 还款 \033[1;34m%s\033[0m -> 余额 \033[1;31m%s\033[0m' % (account_info['account'], money, account_data['balance']))
            else:
                print('\033[1;31m还款失败！\033[0m')
        else:
            print('请输入\033[1;34m正确的\033[0m并\033[1;31m大于0\033[0m的金额'.center(45, '-'))


@auth_login
def transfer(account_info):
    # 转账
    while True:
        transfer_account = input('transfer_account(q表示退出)>>>:').strip()
        if not transfer_account:
            continue
        if transfer_account == 'q':
            break
        while True:
            money = input('transfer_money(q表示退出)>>>:').strip()
            if not money:
                continue
            if money == 'q':
                return
            float_money = judge_num(money)
            if float_money:
                account_data = make_transaction(float_money, account_info, 'transfer', transfer_account)
                if account_data:
                    print('账户：%s -> 转账成功 -> 转账 \033[1;34m%s\033[0m -> 余额 \033[1;31m%s\033[0m' % (account_info['account'], money, account_data['balance']))
                else:  # 交易失败余额不足的 或者 账号不存在的 或者 同一账号的 会直接退出
                    print('\033[1;31m转账失败！\033[0m')
                    return
            else:
                print('请输入\033[1;34m正确的\033[0m并\033[1;31m大于0\033[0m的金额'.center(45, '-'))


def quit_func(account_info):
    # 退出
    exit('bye bye ...')


def controller(account_info):
    # 功能分发器
    print('账户\033[0;34m%s\033[0m登录成功'.center(35, '*') % account_info.get('account'))
    msg_num = '''\033[1;33m
    --------start--------
    1. 账户信息
    2. 提现
    3. 还款
    4. 转账
    5. 退出
    ---------end---------
    \033[0m
    '''
    num_func = {'1': view_account,
                '2': withdraw,
                '3': pay_back,
                '4': transfer,
                '5': quit_func}  # 字典的值可存放 地址
    while True:
        print(msg_num)
        choice_num = input('num>>>:').strip()
        if not choice_num:
            continue
        if choice_num in num_func:
            num_func[choice_num](account_info)
        else:
            print('\033[1;31m请输入正确的序号\033[0m')


def run():
    account_info = login(access_logger)
    print("account_info_f:",account_info)   #获取到账户信息
    if access_logger:
        controller(account_info)