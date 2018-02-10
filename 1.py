#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

user_info = {
 'mary': {'password': '123456'},
 'tom': {'password': '12356'},
 'jerry': {'password': '123456'},
'user1': {'password': 'user1.1'},
'user2': {'password': 'user2.2'}
}
f = open('black_user.txt')          #如果文件存在直接打开
user = f.readlines()     #以行的方式读取，返回的是一个字符串对象，赋值给 user
f.close()
print ('user:',user)
lock_user=[]
for user1 in user:
    user1 = user1.split()
    lock_user.append(user1)
print ('lock_user:',lock_user)
username = input('请输入用户名:')
if not username in user_info:  # username不在字典user_info中，
    print('请输入正确的用户名')