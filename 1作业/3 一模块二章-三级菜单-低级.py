#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

menu = {

    '北京':{

        '海淀':{

            '五道口':{

                'soho':{},

                '网易':{},

                'google':{}

            },

            '中关村':{

                '爱奇艺':{},

                '汽车之家':{},

                'youku':{},

            },

            '上地':{

                '百度':{},

            },

        },

        '昌平':{

            '沙河':{

                '老男孩':{},

                '北航':{},

            },

            '天通苑':{},

            '回龙观':{},

        },

        '朝阳':{},

        '东城':{},

    },

    '上海':{

        '闵行':{

            "人民广场":{

                '炸鸡店':{}

            }

        },

        '闸北':{

            '火车战':{

                '携程':{}

            }

        },

        '浦东':{},

    },
    '四川':{
        '德阳':{
            '乐山':{
                '东岳':{},
                '回兰':{},
                '大佛':{},
                '马锣':{},
            }
    }

    },

    '山东':{},

}



while True:
    for k in menu:  #打印第一层
        print(k)
    choice1 = input('choice1=').strip()
    if not choice1:continue
    if choice1 in menu:
        while True:
            for k in menu[choice1]:
                print (k)   #打印第二层

            choice2 = input('choice2=').strip()
            if not choice2:continue
            if choice2 in menu[choice1]:
                while True:
                    for k in menu[choice1] [choice2]:
                        print (k)  #打印第三层

                    choice3 = input('choice3=').strip()
                    if not choice3:continue
                    if choice3 in menu [choice1][choice2]:
                        while True:
                            for k in menu[choice1][choice2][choice3]:
                                print(k)     #打印第四层
                            choice4 = input("最后一层，'b'返回上一层，'q'退出程序")
                            if not choice4:continue
                            if choice4 == 'b':
                                break
                            elif choice4 == 'q':
                                exit('退出程序')
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit("退出程序")
                    else:
                        print('没有这个节点')
            elif choice2 == 'b':
                break
            elif choice2== 'q':
                exit('退出程序')
            else:
                print ("没有这个节点")
    elif choice1 == 'q':
        exit("退出程序")
    else:
        print ('没有这个节点')