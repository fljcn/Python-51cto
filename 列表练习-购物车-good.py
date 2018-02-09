#写一个循环，不断的问用户想买什么，用户选择一个商品编号，打印该商品，就把对应的商品添加到购物车里，最终用户输入q时退出，打印购物车商品。


# products = [['Iphone',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
# shopping_car = []
# exit_flag = False
# while not exit_flag:
#     print('-------商品列表--------')
#     for index,p in enumerate(products):
#         print ("%s.%s    %s" % (index,p[0],p[1]))
#
#     choice = input("请输入商品序号：")
#     if choice.isdigit():
#         choice = int(choice)
#         if choice >= 0 and choice < len(products):
#             print ("商品 %s 加入购物车！" % (products[choice]))
#             shopping_car.append(products[choice])
#         else:
#             print ('商品不存在')
#     elif choice == "q":
#         if len(shopping_car) > 0:
#             print('-------已购买商品--------')
#             for index, p in enumerate(shopping_car):
#                 print ("%s.%s    %s" % (index, p[0], p[1]))
#         exit_flag = True

#第二
products = [['Iphone',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
shopping_car = []
exit_flag = False
while not exit_flag:
    print ("----------商品清单---------")
    for index,p in enumerate(products):
        print (index,p[0],p[1])

    choice = input('请输入商品序号')
    if choice.isdigit():
        choice = int(choice)
        if choice >=0 and choice < len(products):
            shopping_car.append(products[choice])
            print ('%s 商品已经加入购物车' % (products[choice]))

    elif choice == 'q':
        if len(shopping_car)>0:
            print ("----------已购商品清单----------")
            for index,p in enumerate(shopping_car):
                print (index,p[0],p[1])
        exit_flag = True