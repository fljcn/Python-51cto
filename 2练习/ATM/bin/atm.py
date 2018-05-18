# -*- coding:utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import(
    main, manager, shopper
)


def main_run():
    main.run()


def manager_run():
    manager.run()


def shopper_run():
    shopper.run()


def quit_func():
    exit('bye bye ...')


def choice():
    choice_msg = '''
    -----start-----
    1.普通账户
    2.管理员
    3.购物者
    4.退出
    ------end------
    '''
    dict_choice = {'1': main_run,
                   '2': manager_run,
                   '3': shopper_run,
                   '4': quit_func}
    while True:
        print(choice_msg)
        choice_num = input('num>>>:').strip()
        if choice_num in dict_choice:
            dict_choice[choice_num]()
        else:
            print('请输入正确的序号！')


if __name__ == '__main__':
    choice()