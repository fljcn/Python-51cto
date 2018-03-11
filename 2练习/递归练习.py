#递归练习题
#深度查询
#1. 打印所有的节点
#2. 输入一个节点名字，沙河， 你要遍历找，找到了，就打印它，并返回true,
menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': []},
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
        ]
    }
]
def func1(m):
    for con in m:
        print(con['text'])
        func1(con['children'])
func1(menus)

def func2(menu,name):
    for con in menu:
        if name != con['text']:
            func2(con['children'],name)
        else:
            print(con['text'])
name=input('请输入地名：')
func2(menus,name)