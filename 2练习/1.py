#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

# 扩展需求：
#
# 1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
# 2、允许查询之前的消费记录
#   注意：创建文件，需要记录：1、用户名、密码、余额。2、上次购物清单

import os,json

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

# 思路：
# 两个文件分别记录：一是用户名、密码、余额（user_info.json）；二是记录上次购物清单(shopping_list)
# 判断 user_info.json是否存在，不存在以w方式，读取出来
# 输入用户名、密码，验证通过，显示上次消费余额
# 输入 是否查看上次的消费记录，是查看，否继续购物
# 打印商品清单，继续购物
# 将户名、密码、余额记录到文件user_info.json，购物清单记录到shopping_list
#
# shopp_car = []  #初始购物车
# shopp_car_price = 0 #购物车商品金额

#判断锁定用户文件没有存在，如果没有，打开时新建

user = 'feng'
password = 'jun'
balance_result = []
shopp_car = []
shopp_car_price = 0
shopping_new_list_result = []

#读取上次购物余额
if not os.path.isfile('balance.txt'):
    f=open('balance.txt','w')
f=open('balance.txt','r')
balance_newlist = f.readlines()
for x in balance_newlist:
    balance_result.append(x.strip())
f.close()
if len(balance_result) != 0:  #为空不取余额
    balance_result = int(balance_newlist[-1])       #取出余额

#读取上次购物清单
if not os.path.isfile('shopping_list.json'):
    f=open('shopping_list.json','w')
f=open('shopping_list.json','r')
# 读取数据并分割。 最后一个为空，所以去除
shopping_new_list = f.read().split('\n')[:-1]
for x in shopping_new_list:
    json_x = json.loads(x)
    shopping_new_list_result.append(json_x)
f.close()
if len(shopping_new_list_result) != 0:
    print ('上次购物车清单：',shopping_new_list_result)



while True:
    _user = input('请输入用户名：').strip()
    _password = input('请输入密码：').strip()
    _salary = int(input('请输入工资：').strip())

    if _user == user and _password == password:
        print ('\033[1;37;44m''您的消费余额：%s元,'% (balance_result),'\033[0m')
        # 打印上次购物清单
        if len(shopping_new_list_result) != 0:
            print('\n----------上次购物商品清单----------')
            for index, k in enumerate(shopping_new_list_result):  # 打印
                print(index, ' ', (shopping_new_list_result[index]).get('name'), "  ", (shopping_new_list_result[index]).get('price'))
            shopp_car_price = shopp_car_price + (shopping_new_list_result[index]).get('price')
            print('已选商品总金额： %s元 ' % (shopp_car_price))



    else:
        print ('用户名、密码不正确！')
        continue
    # choice0 = input('是否显物购物（Y/N）')

    while True:
        print ('----------商品清单----------')
        for index,k in enumerate(goods):    #通过枚举打印出商品清单
            print (index,' ',(goods[index]).get('name'),"  ",(goods[index]).get('price'))

        choice = input("请输入商品序号,'q'退出：").strip()
        if not choice: continue
        if choice.isdigit():  # 判断输入是否是数据
            choice = int(choice)
            if choice >= 0 and choice < len(goods):  # 判断输入序号
                shopp_car.append(goods[choice])  # 选择的商品加入购物车列表

                print('\033[1;37;44m', '%s 已经加购物车' % ((goods[choice]).get('name')), '\033[0m')  # 高亮资显示
                shopp_car_price = shopp_car_price + (goods[choice]).get('price')  # 汇总购物车商品价格
                balance = _salary - shopp_car_price  # 余额=工资-商品汇总价
                if balance < 0:  # 余额为负数显示不足
                    print("余额不足")
        elif choice == 'q':  # 输入q 退出，显示 已选择商品清单
            print('\n----------已选择商品----------')
            for index, k in enumerate(shopp_car):  # 打印
                print(index, ' ', (shopp_car[index]).get('name'), "  ", (shopp_car[index]).get('price'))
            print('已选商品总金额： %s元 ' % (shopp_car_price))
            print('\033[1;37;44m', '工资余额： %s元' % (balance), '\033[0m')  # 高亮显示
            break