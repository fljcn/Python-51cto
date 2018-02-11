#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

'''作业题目：编写登陆认证程序
作业需求：
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序

升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）'''

import os
username = {'user1':{'password':'user1.1'},
            'user2':{'password':'user2.2'},
            'user3':{'password':'user3.3'},
            'user4':{'password':'user4.4'},
            'user5':{'password':'user5.5'},
            }
#判断锁定用户文件没有存在，如果没有，打开时新建
if not os.path.isfile('black_user.txt'): #判断当前目录中没有‘black_user.txt’ 锁定用户文件
    f=open('black_user.txt','w')  #如果没有，打开时创建一个‘black_user.txt’
f=open('black_user.txt','r')    #再以读取方式打开‘black_user.txt’
_black_user=f.readlines()      #以行的形式读取‘black_user.txt’，赋值给_black_user
f.close()

#创建空列表，把_black_user追加到进去
lock_user = []
for i in _black_user:
    i = i.strip()
    lock_user.append(i)
print ('已被锁定用户名单：',lock_user)

count = 0
count1 = 0
while True:
    #输入用户名，并验证用户名是否正在列表lock_user中，如果在提示“已被锁定”，退出
    _username = input('请输入用户名：')
    if _username in lock_user:
        print ('已被锁定！')
        exit(0)

    #判断输入的用户名是否在字典username中，如果没有，3次重新输入机会
    if not _username in username:
        print ('请输入正确用户名，共3次机会：')
        if count == 2:
            print ("已输入3次,退出程序！")
            # exit_flag = True
            exit(0)
        count += 1
    else:
       while True:
            #输入密码，并判断是否正确，如果不正确输入3次，将被锁定
            _password = input('请输入用户密码：')
            if _password == username[_username] ['password']:
                print ('欢迎 %s 用户！' % (_username))
                exit(0)
            else:
                print ('密码输入错误')
            if count1 == 2:
                print ("已输入3次，即将锁定!")
                f=open('black_user.txt','a')
                f.write('%s\n' % (_username))
                f.close()
                exit(0)
            count1 += 1
