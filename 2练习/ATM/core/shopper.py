# -*- coding:utf-8 -*-
from conf.settings import GOODS
from .auth import login
from .main import (
    access_logger, checkout
)


def show_buy_goods(goods_buyed):
    # 展示购买的商品
    all_money = 0
    if len(goods_buyed) == 0:
        return all_money
    else:
        print('您已购买以下商品：'.center(20, '-'))
        for index, i in enumerate(goods_buyed, 1):
            print('%s. %s  %s' % (index, i['name'], i['price']))
            all_money += int(i['price'])
        return all_money


def buy_goods(dict_goods):
    # 购买商品
    goods_buyed = []
    while True:
        choice = input('num(q退出并结算)>>>:').strip()
        if not choice:
            continue
        if choice == 'q':
            return show_buy_goods(goods_buyed)
        if choice in dict_goods:
            goods_buyed.append(dict_goods[choice])
            print('\033[1;34m%s\033[0m 加入购物车' % dict_goods[choice]['name'])
        else:
            print('\033[1;31m重新选择\033[0m')


def show_goods():
    # 展示商品列表
    dict_goods = {}
    print('展示商品列表'.center(20,'-'))
    for index, i in enumerate(GOODS):
        dict_goods[str(index)] = i
        print('%d. %s   %d' % (index, i['name'], i['price']))
    return dict_goods


def run():
    account_info = login(access_logger)
    if account_info['is_auth'] is True:
        all_money = buy_goods(show_goods())
        checkout(account_info, all_money)