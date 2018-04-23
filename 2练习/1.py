#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

#  将文本转换成列表
def table_info():
    with open('staff_table.txt', 'r+', encoding='utf-8') as staff_file:
        data = staff_file.readlines()
        data_list = []
        for i in data:
            data_list.append(str(i).strip().split(','))
    return data_list


#定义解析函数
def sql_parse(sql):

    parse_func = {
        'add': add_action,
        'del': del_action,
        'UPDATE': update_action,
        'find': find_action,
    }
    sql_l = sql.split(' ')
    func = sql_l[0]
    res = ''
    if func in parse_func:
        res = parse_func[func](sql_l)
    return res


    # print('sql_l:',sql_l)
    # return sql_l

def add_action(sql_l):
    data_value = table_info()
    input_add=sql
    #截取 Alex Li,25,134435344,IT,2015-10-29
    input_add=input_add[16:]
    #把增加的语句转换成列表
    input_list=input_add.split(',')
    phone=[]
    #把员工信息中的手机号提取到列表phone
    for k in data_value:
        phone.append(k[3])
    #检查新输入的员工信息手机号是否在列表phone中
    if input_list[2] in phone:
        print('手机号已经存在！')
        exit()
    else:
       # 员工记录ID+1，为新增员工ID
        data_count=len(data_value)+1
       #插入ID号
        input_list.insert(0,str(data_count))
        #转换成字符，以逗号分隔
        input_list_str=','.join(input_list)
    with open('staff_table.txt', 'a+', encoding='utf-8') as staff_file:
        # 打开文件后在最后文件末尾换行
        staff_file.write('\n')
        staff_file.write(input_list_str)
    print('插入1条新语句！')


def del_action(sql_l):
    data_value = table_info()
    # input_add=sql
    #取sql语句ID值
    id_str=sql_l[4][3]
    #匹配员工信息表中ID与sql语句ID相同的记录，并删除
    for k in data_value:
        if k[0] == id_str:
            del k[:]
    #删除空记录
    del data_value[int(id_str)-1]
    with open('staff_table.txt', 'w', encoding='utf-8') as staff_file:
        for k in data_value:
            k_str = ','.join(k)
            staff_file.write(k_str)
            staff_file.write('\n')
    print('删除1条语句！')


def update_action(sql_l):
    data_value = table_info()
    del_add = sql
    #切分出sql语句中IT
    it_cut=sql[49:51]
    # 切分出sql语句中Alex Li
    name_cut=sql[42:49]
    if it_cut == 'IT':
        count1 = 0
        for k in data_value:
            if k[4]==it_cut:
                k[4]='Market'
                count1+=1
    elif name_cut=='Alex Li':
        count1 = 0
        for k in data_value:
            if k[1] == name_cut:
                k[2] = '25'
                count1+=1
    with open('staff_table.txt','w',encoding='utf-8') as staff_file:
        for k in data_value:
            k_str=','.join(k)
            staff_file.write(k_str)
            staff_file.write('\n')
    print('共修改了%s条语句！'%count1)



def find_action(sql_l):
    data_value = table_info()
    age_cut=sql_l[7]  #切分出年龄
    it_cut=sql_l[7]   #切分出部门为IT
    num1=sql_l[1]     #切分出*
    if num1 == '*':
        if it_cut == '"IT"':
            count = 0   # 计数器，每次加1
            for k in data_value:
                if "IT" in k[4]:
                    str_i=' '.join(k)
                    print(str_i)
                    count+=1
            print('查询到%s条语句！' % count)  # 打印受影响的条数
        else:
            count = 0
            for k in data_value:
                if '2013' in k[5]:
                    str_i = ' '.join(k)
                    print(str_i)
                    count += 1
            print('查询到%s条语句！' % count)
    else:
        count = 0
        for k in data_value:
            if int(k[2]) > int(age_cut):
                print(k[1], k[2])
                count += 1
        print('查询到%s条语句！' % count)



if __name__ == "__main__":
    while True:
        print('''
        **********************员工信息表增删改查程序**********************
            1.模糊查询 语法:
                       find name,age from staff_table where age > 22
                       find * from staff_table where dept = "IT"
                       find * from staff_table where enroll_date like "2013")
            2.新增信息 语法:add staff_table Alex Li,25,134435344,IT,2015-10-29
            3.删除信息 语法:del from staff where id=3
            4.修改信息 语法:
                        UPDATE staff_table SET dept="Market" WHERE dept="IT"
                        UPDATE staff_table SET age=25 WHERE name="Alex Li"
            \033[42;0m 请在“sql>”后输入相应语法\033[0m
                         ''')
        sql=input('sql>').strip()
        if sql =='exit':break
        if len(sql)==0:continue

        sql_dic=sql_parse(sql)
        break