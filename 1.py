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

for user1 in user_info:
    print(user1)
username = input('请输入用户名:')
if not username in user_info:  # username不在字典user_info中，
    print('请输入正确的用户名')