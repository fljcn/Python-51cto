names = []    #创建一个空列表，命名为names，往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl
names.append("old_driver")
names.append("rain")
names.append("jack")
names.append('shanshan')
names.append('peiqi')
names.append('black_girl')
names.insert(-1,"alex")    #往names列表里black_girl前面插入一个alex
names[3]="姗姗" #把shanshan名字改成中文，姗姗
names.insert(2,['oldboy','oldgirl'])    #往names列表里rain的后面插入一个子列表，[oldboy,oldgirl]插入到前面
#del names[3]
names.extend([1,2,3,4,2,5,6,2])     #创建新列表[1,2,3,4,2,5,6,2] ，合并入names列表
print (names)

# print ("peiqi的索引值",names.index("peiqi"))    # 返回peiqi的索引值
# print ("取出names列表中索引4-7的元素是：",names[4:7])
# print ("取出names列表中索引2-10的元素是：",names[2:10:2])
# print ("取出names列表中最后3个元素是：",names[-3:])
print ("names列表长度：",len(names))
# print (names[2])

# 显示索引值和元素  方法一
count = 0
# for i in names:
#     print ("names的索引值：",count,"    元素：",i)
#     count += 1

# 显示索引值和元素  方法二
for index,i in enumerate(names):   #枚举
    print (index,"  ",i)

# 显示索引值和元素，当索引值为偶数时，值为-1
# for index,i in enumerate(names):
#     if index % 2 == 0: # 偶数
#         names[index] = -1
# for index,i in enumerate(names):
#     print (index," ",i)
print (names)
# names里面有3个2，请返回第2个2的索引值，分块 第一个+1后，查找

first_index = names.index(2)    #第一个2位置
new_list = names[first_index+1:]    #第一个2切片后
second_index = new_list.index(2)    #第二个2切片后位置
second_val = names[first_index+second_index+1]   #first_index+second_index+1
print (new_list,first_index,second_val)
print ('second values:',second_val)


