#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

user_status = False  # 用户登录了就把这个改成True

def login(func):

    def inner():
        _username = "1"  # 假装这是DB里存的用户信息
        _password = "11"  # 假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:").strip()
            password = input("pasword:").strip()

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")
        else:
            print("用户已登录，验证通过...")

        if user_status:
            func()
    return inner


def home():
    print("---首页----")


def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")

@login
def henan():
    print("----河南专区----")

# henan = login(henan)
henan()
