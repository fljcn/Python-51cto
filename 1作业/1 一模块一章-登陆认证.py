#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

'''作业题目：编写登陆认证程序
作业需求：
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
'''

user = 'user1'
password = 'user1.1'
count = 0
while count < 3:
    _user = input('请输入用户名：')
    _password = input("请输入密码：")
    if _user == user and _password == password:
        print('-----欢迎%s登录系统!------' % (user))
        break
    count += 1

