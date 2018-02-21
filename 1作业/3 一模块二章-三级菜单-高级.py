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
                '东岳':{
                    '一村':{},
                    '二村':{},
                },
                '回兰':{},
                '大佛':{},
                '马锣':{},
            }
    }

    },

    '山东':{},

}

currect_layer = menu  # 创建变量currect_layer，代表所有当前层
layers  = []    #创建空列表，用于记录上层
while True:
    for k in currect_layer:   #chrrect_layer 初始表示 menu
        print (k)
    choice = input("请输入上面内容，'q'退出程序,'b'返回上层:").strip()
    if not choice:continue
    if choice in currect_layer: #输入的在当前层
        layers.append(currect_layer)    #把当前层追加到layers列表
        currect_layer = currect_layer[choice]   #当前层的下一层赋值给当前层

    elif choice == 'b':
        if len(layers) != 0:    #layers中还有元素，执行
            currect_layer = layers.pop()    #移除列表中的一个元素（默认最后一个），并且返回该元素的值，赋值给currect_layer
        else:
            print ('已经是最上层！')
    elif choice == 'q':
        exit('退出程序')
