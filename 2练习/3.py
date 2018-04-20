def table_info():
    data_file = open('staff_table.txt', 'r+', encoding='utf-8')
    data = data_file.readlines()
    data_list = []
    for i in data:
        data_list.append(str.strip(i).split(','))
    print ('data:',data_list)
    return data_list
#  将文本转换成数据组


def search():
    data_value = table_info()
    input_search = input('请输入查询语句:')
    num1 = input_search[5:6]  # 截取*格式
    num2 = input_search[43:]   # 截取age>22
    num3 = input_search[30:]  # 截取dept = "IT"
    if num1 == '*':   # 判断查询语句，关键字是否为*号
        value = 'dept = "IT"'
        if value == num3:
            count = 0   # 计数器，每次加1
            for k in data_value:
                if 'IT' in k[4]:
                    str_i = ','.join(k)
                    str_ii = str_i.replace(',',' ')
                    print(str_ii)
                    count += 1
            print('查询到%s条语句！' % count)  # 打印受影响的条数
        else:
            count = 0
            for k in data_value:
                if '2013'in k[5]:
                    str_i = ','.join(k)
                    str_ii = str_i.replace(',',' ')
                    print(str_ii)
                    count += 1
            print('查询到%s条语句！' % count)
    else:
        count = 0
        for k in data_value:
            if int(k[:][2]) > int(num2):
                print(k[1],k[2])
                count += 1
        print('查询到%s条语句！' % count)


def append():
    data_value = table_info()
    input_add = input('请输入新增语句:')
    input_cut = input_add[16:]
    input_list = list(input_cut.split(','))
    phone_list =[]
    # 将已存在的电话号，存在列表中+
    for i in data_value:
        phone = i[3]
        phone_list.append(phone)
    if input_list[2] in phone_list:
        print('手机号已存在！')
        exit()
    else:
        data_count = len(data_value)+1
    # 设置新员工的ID值
        input_list.insert(0, str(data_count))
        input_list_str = ','.join(input_list)
    # 转换成以逗号分隔得员工信息
        data_file = open('staff_table.txt', 'a+')
        data_file.write('\n')
        # 打开文件后首先在最后文件末尾换行
        data_file.write(input_list_str)
        data_file.close()
        print('插入1条新语句！')


def delete():
    data_value = table_info()
    input_remove = input('请输入删除语句:')
    input_remove_id = input_remove[24:]
    remove_id = int(input_remove_id) - 1
    # 列表值是从0开始的
    del data_value[remove_id]
    print('删除了1条数据')
    data_file = open('staff_table.txt', 'w', encoding='utf-8')
    for i in data_value:
        str = ','.join(i).replace('\n',',')
        data_file.write(str)
        data_file.write('\n')
    data_file.close()


def update():
    data_value = table_info()
    input_update = input('请输入修改语句:')
    cut1 = input_update[23:36]  # 截取dept="Market"
    cut2 = input_update[43:54]  # 截取dept = "IT"
    cut3 = input_update[23:29]  # 截取age=25
    cut4 = input_update[36:52]  # 截取name = "Alex Li"
    value = 'dept = "Market"'
    value1 = 'name = "Alex Li"'
    if value == cut1:
        count = 0
        for k in data_value:
            if k[4] == 'IT':
                k[4] = 'Market'
                count += 1
        print('修改了%s条数据' % count)

    elif value1 == cut4:
        count = 0
        for k in data_value:
            if k[1] == "Alex Li":
                k[2] = 25
                count += 1
        print('修改了%s条数据' % count)
    else:
        print('操作错误')
    data_file = open('staff_table.txt', 'w', encoding='utf-8')
    for i in data_value:
        str = ','.join(i).replace('\n', ',')
        data_file.write(str)
        data_file.write('\n')
    data_file.close()


while True:
    print('''
--------------------------------员工信息表增删改查程序--------------------------------------
    1.模糊查询(语法:find name,age from staff_table where age > 22

               find * from staff_table where dept = "IT"

               find * from staff_table where enroll_date like "2013")
    2.新增信息(语法: add staff_table Alex Li,25,134435344,IT,2015-10-29)
    3.删除信息(语法:del from staff where id=3)
    4.修改信息(语法:UPDATE staff_table SET dept="Market" WHERE dept = "IT" 
               UPDATE staff_table SET age=25 WHERE name = "Alex Li"  )''')#把name=Alex Li的纪录的年龄改成25,把所有dept=IT的纪录的dept改成Market
    do = int(input('请输入你想要的操作：'))
    if do == 1:
        print('---欢迎进入查询界面----')
        search()
        break
    elif do == 2:
        print('---欢迎进入新增界面----')
        append()
        break
    elif do == 3:
        print('---欢迎进入删除界面----')
        delete()
        break
    elif do == 4:
        print('---欢迎进入修改界面----')
        update()
        break
    else:
        print('wrong do')