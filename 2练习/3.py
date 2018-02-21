#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

# 字典示例
# 一个简单的数据库
# 字典使用人名作为键，每个人用另一个字典表示，其键“phone”和“addr”分别表示他们的电话号码和地址

pepole = {
    'Alic':{
    'phone':'2341',
    'addr':'Foo drive 23'
},
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }
}
print (pepole['Alic']['addr1'])
print (pepole.get('Alic').get('addr'))



# # 针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
# labels = {
#      'phone':'phone number',
#     'addr':'address'
# }
#
# name = input("Name:")
#
# #查找电话号码还是地址？
# request = input('Phone number(p) or address(a)?')
#
# #使用正确的键：
# if request == 'p':key = 'phone'
# if request == 'a':key = 'addr'
#
# #如果名字是字典中的有效键才打印信息：
# if name in pepole:
#     print("%s's %s is \033[1;37;44m %s.\033[0m" %(name,labels[key],pepole[name][key]))