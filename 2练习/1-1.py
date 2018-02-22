#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

# 扩展需求：
#
# 1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
# 2、允许查询之前的消费记录

# 思路：
# 1、默认 用户名、密码，上次消费的余额都存在一个列表中。
# 2、之前的消费记录也存在一个字典中。

goods = [
    {"name":
         "电脑", "price": 1999},
    {"name":
         "鼠标", "price": 10},
    {"name":
         "游艇", "price": 20},
    {"name":
         "美女", "price": 998},
]

user_info =[
    {'user':'user1','password':'user1.1','balance':12991},
    {'user':'user2','password':'user2.2','balance':13982},
    {'user': 'user2', 'password': 'user2.2', 'balance': 12003},
     ]
#
xiaofei_list={
    'user1':
         [{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}],
    'user2':
         [{'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}],
    'user3':
         [{'name': '电脑', 'price': 1999}, {'name': '美女', 'price': 998}]
     }

_user1 = input('请输入用户名：')
aa = 0
print(xiaofei_list[_user1])
for index, k in enumerate(xiaofei_list[_user1]):  # 打印
    print(index, ' ', (xiaofei_list[_user1][index]).get('name'), "  ", (xiaofei_list[_user1][index]).get('price'))
    aa= aa+(xiaofei_list[_user1][index]).get('price')
print ('aa=',aa)

print (type(user_info))
print (user_info[1]['password'])