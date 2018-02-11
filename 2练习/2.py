#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

https://www.cnblogs.com/yes5144/p/6839980.html

################################################
# Task Name: 三级菜单                           #
# Description：打印省、市、县三级菜单             #
#              可返回上一级                      #
#               可随时退出程序                   #
#----------------------------------------------#
# Author：Oliver Lee                           #
################################################
data = {'北京':{'海淀':{'五道口':{'soho':{},'网易':{}, 'Google':{},}, '中关村':{},'爱奇艺':{},'汽车之家':{}}}}
#3级菜单
#
data = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'Google':{},
            },
                '中关村':{},
                '爱奇艺':{},
                '汽车之家':{}
            }
        }
    }

# ===

# menu = {"河南": {
#     "郑州站":{},
#     "漯河站":{},
#     "信阳站":{}}}

data = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'Google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            }
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{}
            },
            '天通苑':{},
            '回龙观':{}
        },
        '朝阳':{},
        '东城':{}
    },
    '上海':{},
    '湖北':{},
    '广东':{}
}
exit_flag = False#标志位,只要不为True,循环会一直执行
while not exit_flag:
    for i in data:#循环打印data
        print(i)
    choice = input("请输入>>>")
    if choice in data:#判断choice是否在data中
        while not exit_flag:
            for i2 in data[choice]:
                print(i2)
            choice2 = input("请输入>>>")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print(i3)
                    choice3 = input("请输入>>>")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("最后一层,请输入b返回或输入q结束>>>")
                        if choice4 == 'b':
                            pass#直接跳过,如果不加pass的话会报错
                        elif choice4 == 'q':
                            exit_flag = True
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
    elif choice == 'q':
        exit_flag = True