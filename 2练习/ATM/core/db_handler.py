# -*- coding:utf-8 -*-
import os
import json

from .logger import set_logger
from .auth import judge_account
from conf.settings import(
    DATABASE, TRANSACTION_TYPE
)

trans_logger = set_logger('transactions')


def account_data_save(account, account_data):
    # 修改文件的 公共方法
    path = os.path.join(DATABASE['path'], account + '.json')
    path_tmp = os.path.join(DATABASE['path'], account + '_tmp' + '.json')
    if os.path.isfile(path):
        with open(path_tmp, 'w', encoding='utf-8') as f:
            json.dump(account_data, f)
        os.replace(path_tmp, path)
        return account_data


def save_json_common(account, new_balance, account_data):
    # 内存中 替换余额
    account_data['balance'] = round(new_balance, 2)
    return account_data_save(account, account_data)


def transaction_logger(account, new_balance, account_data, arguments):
    # 记录 日志的 公共方法
    account_data_new = save_json_common(account, new_balance, account_data)
    if account_data_new:
        trans_logger.info('account: %s - account_type: %s - action: %s - interest: %s' % (account, arguments[0], arguments[1]['action'], arguments[1]['interest']))
        return account_data_new


def split_account(new_balance, account_info, *args, **kwargs):
    # 区分开 是两个账号间的操作 还是一个账号
    account = account_info['account']
    if len(kwargs) != 0:  # 转账 两个账号 间的操作
        transfer_data = save_json_common(kwargs['transfer_account'], kwargs['transfer_new_balance'], kwargs['transfer_data'])
        if transfer_data:
            return transaction_logger(account, new_balance, account_info['account_data'], args)
    else:  # 一个 账号 的操作
        return transaction_logger(account, new_balance, account_info['account_data'], args)


def make_transaction(money, account_info, account_type, *args):
    # 提现 还款 转账 公共方法
    if account_type in TRANSACTION_TYPE:
        transaction_type = TRANSACTION_TYPE[account_type]
        interest = money * transaction_type['interest']
        old_balance = account_info['account_data']['balance']
        # 减钱的 操作
        if transaction_type['action'] == 'minus':
            if len(args) == 0:  # 提现 或者 消费 没有附加的参数
                new_balance = old_balance - money - interest
                if new_balance < 0:
                    print('\033[1;31m交易失败，余额不足\033[0m')
                else:
                    return split_account(new_balance, account_info, account_type, transaction_type)
            else:  # 转账
                if args[0] == account_info['account']:
                    print('\033[1;31m注：同一账号，不允许转账\033[0m')
                else:
                    transfer_data = judge_account(args[0])
                    if transfer_data:
                        if transfer_data['status'] == 1:
                            print('\033[1;31m账号:%s 被冻结！\033[0m'.center(30, '-') % args[0])
                        else:
                            new_balance = old_balance - money - interest
                            if new_balance < 0:
                                print('\033[1;31m交易失败，余额不足\033[0m')
                            else:
                                transfer_new_balance = transfer_data['balance'] + money
                                return split_account(new_balance, account_info, account_type, transaction_type, transfer_account = args[0], transfer_new_balance = transfer_new_balance, transfer_data = transfer_data)
                    else:
                        print('\033[1;31m账号:%s 不存在\033[0m' % args[0])
        # 加钱的 操作
        elif transaction_type['action'] == 'plus':
            new_balance = old_balance + money + interest
            return split_account(new_balance, account_info, account_type, transaction_type)

    else:
        print('\033[1;31m%s 交易类型不存在！\033[0m' % account_type)