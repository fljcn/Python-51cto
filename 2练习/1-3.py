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
# 3、步骤：一是输入用户名，验证密码，显示余额。二是显示上次消费记录。三是继续购物。
# 4、工资总额默认是15000元。

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


user_info = {       #用户信息和上次消费余额
    "user1":{'password':'user1.1','balance':12991},
    "user2":{'password':'user2.2','balance':13982},
    "user3":{'password':'user3.3','balance':12003},
     }


old_shopp_car={              #上次购物清单
    'user1':
         [{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}],
    'user2':
         [{'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}],
    'user3':
         [{'name': '电脑', 'price': 1999}, {'name': '美女', 'price': 998}]
     }

old_shopp_car_price = 0 #上次购物商品金额
shopp_car = []          #本次购物车
shopp_car_price = 0 #本次购物商品金额
print ("工资金额\033[1;37;44m15,000元\033[0m")
count1 = 0
count2 = 0
while True:
    while True:
        _user = input('请输入用户名：').strip()

        if _user  in user_info:
            _password = input('请输入密码：').strip()
            if _password == user_info[_user]['password']:
                print('\033[1;37;44m上次消费余额:%s元\033[0m' % (user_info[_user]['balance']))
                break
            else:
                print('用户密码错误，请重新输入，共3次机会！')
                if count1 == 2:
                    print("已输入3次,即将退出！")
                    exit(0)
                count1 += 1
        else:
            print ('用户名错误，请重新输入，3次机会。')
            if count2 == 2:
                print("已输入3次,即将退出！")
                exit(0)
            count2 += 1
    break

    choice1 = input('是否显示上次购物清单清(y/n):').strip()
    if choice1 == 'y':
        print ('==========上次购物清单==========')
        for index, k in enumerate(old_shopp_car[_user]):  # 打印
            print(index, ' ', (old_shopp_car[_user][index]).get('name'), "  ", (old_shopp_car[_user][index]).get('price'))
            old_shopp_car_price= old_shopp_car_price+(old_shopp_car[_user][index]).get('price')
        print ('上次购物金额总计%s元：' % (old_shopp_car_price))

    while True:
        print('\n----------商品清单----------')
        for index, k in enumerate(goods):  # 通过枚举打印出商品清单
            print(index, ' ', (goods[index]).get('name'), "  ", (goods[index]).get('price'))
        choice2 = input("请输入商品序号,'q'退出：").strip()
        if not choice2: continue
        if choice2.isdigit():  # 判断输入是否是数据
            choice2 = int(choice2)
            if choice2 >= 0 and choice2 < len(goods):  # 判断输入序号
                shopp_car.append(goods[choice2])  # 选择的商品加入购物车列表

                print('\033[1;37;44m', '%s 已经加购物车' % ((goods[choice2]).get('name')), '\033[0m')  # 高亮资显示
                shopp_car_price = shopp_car_price + (goods[choice2]).get('price')  # 汇总购物车商品价格
                balance = (user_info[_user] ['balance']) - shopp_car_price  # 余额=工资-商品汇总价
                if balance < 0:  # 余额为负数显示不足
                    print("余额不足")
        elif choice2 == 'q':     #输入q 退出，显示 已选择商品清单
            print('\n----------本次已选择商品----------')
            for index,k in enumerate(shopp_car):    #打印
                print(index, ' ', (shopp_car[index]).get('name'), "  ", (shopp_car[index]).get('price'))
            print('已选商品总金额： %s元 '% (shopp_car_price) )
            print('\033[1;37;44m','工资余额： %s元' % (balance),'\033[0m')    #高亮显示
            break
    break
