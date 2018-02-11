
# dic = {'K1':'v1','K2':'v2','K3':'v3',}
# # question1 循环遍历出所有的key
# for k in dic:
#     print (k)
#
# #question 2 循环遍历出所有的value
# for v in dic:
#     print (dic[v])
#
# #question 3 循环遍历出所有的key和value
# for v in dic:
#     print (v,dic[v])
#
# #question 4 在字典中添加一个键值对，'K4':'v4'，输出添加后的字典
# dic['K4']='v4'
# print (dic)
#
# #question 5 重点重点   删除字典中键值对'K1','v1'，并输出删除后的字典
# del dic['K1']    #方法一  注意是中括号，删除一个没有的值不报错
# #dic.pop('K1')   #方法二 注意中小括号
# print (dic)

# #question 6    难点  # 获取一个没有k5，并不报错
# dic = {'K1':'v1','K2':'v2','K3':'v3',}
# dic.get('K5')
# print (dic.get('K5'))
#
# # question 7 获取字典中'K2'的对应值
# # print (dic.get('K2'))   方法一
# print (dic['K2'])       # 方法二
#
# # question 8 获取字典中‘K6’对应的值，如果键‘K6’不存在，侧不报错，并让其返回None.
# print (dic.get('K6'))

 #question 9 重点  现有dic2 = {'K1':'v111','a':'b'}通过一行操作使{'K1': 'v111', 'K2': 'v2', 'K3': 'v3', 'a': 'b'}
# dic = {'K1':'v1','K2':'v2','K3':'v3'}
# dic2 = {'K1':'v111','a':'b'}
# dic.update(dic2)             #替换的旧的，新的增加，旧的不重复，复制过来
# print (dic)

#question 10 组合嵌套
# 10-1 将列表lis中的'tt'变成大写（用两种方式）

# lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
# lis[0][1][2]['k1'][0]=lis [0][1][2]['k1'] [0].upper()    #方法一
# print (lis)

# lis = [['k',['qwe',20,{'k1':['tt'.upper(),3,'1']},89],'ab']]  #方法二
# print (lis)

#question 10-2 将列表中数字 3 变成字符串“100”（用两种方法）
# lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
# lis[0][1][2]['k1'][1]='100'                    #方法一
# print (lis)

#question 10-2 将列表中字符串 “1” 变成数字101（用两种方法）
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
lis[0][1][2]['k1'][2]=100                    #方法一
print (lis)

# question 11 