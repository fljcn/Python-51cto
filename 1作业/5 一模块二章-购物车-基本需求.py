#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng
# 基础要求：
#
# 1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
#
# 2、允许用户根据商品编号购买商品
#
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#
# 4、可随时退出，退出时，打印已购买商品和余额
#
# 5、在用户使用过程中，
# 关键输出，如余额，商品已加入购物车等消息，需高亮显示

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

shopp_car = []  #初始购物车
shopp_car_price = 0 #购物车商品金额

_user = input('请输入用户名：').strip()
_password = input('请输入密码：').strip()
_salary = int(input('请输入工资：').strip())

while True:
    print ('----------商品清单----------')
    for index,k in enumerate(goods):    #通过枚举打印出商品清单
        print (index,' ',(goods[index]).get('name'),"  ",(goods[index]).get('price'))

    choice = input("请输入商品序号,'q'退出：").strip()
    if not choice:continue
    if choice.isdigit():    #判断输入是否是数据
        choice = int(choice)
        if choice >=0 and choice < len(goods):   #判断输入序号
            shopp_car.append(goods[choice])   #选择的商品加入购物车列表

            print('\033[1;37;44m','%s 已经加购物车' % ((goods[choice]).get('name')),'\033[0m')  #高亮资显示
            shopp_car_price = shopp_car_price + (goods[choice]).get('price')    #汇总购物车商品价格
            balance = _salary - shopp_car_price   # 余额=工资-商品汇总价
            if balance < 0:   #余额为负数显示不足
                print("余额不足")
    elif choice == 'q':     #输入q 退出，显示 已选择商品清单
        print('\n----------已选择商品----------')
        for index,k in enumerate(shopp_car):    #打印
            print(index, ' ', (shopp_car[index]).get('name'), "  ", (shopp_car[index]).get('price'))
        print('已选商品总金额： %s元 '% (shopp_car_price) )
        print('\033[1;37;44m','工资余额： %s元' % (balance),'\033[0m')    #高亮显示
        break