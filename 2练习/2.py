#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@author: caimengzhi
@license: (C) Copyright 2013-2017.
@contact: 610658552@qq.com
@software: pycharm 2017.02
@project: luffy
@file: tmp.py
@time: 2018/1/24 15:15
@desc:
1.可进行模糊查询，语法至少支持下面3种查询语法:
    find name,age from staff_table where age > 22
    find * from staff_table where dept = "IT"
    find * from staff_table where enroll_date like "2013"
2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
    语法: add staff_table Alex Li,25,134435344,IT,2015-10-29
3.可删除指定员工信息纪录，输入员工id，即可删除
    语法: del from staff where  id=3
4.可修改员工信息，语法如下:
    UPDATE staff_table SET dept = "Market" WHERE  dept = "IT" 把所有dept=IT的纪录的dept改成Market
    UPDATE staff_table SET age = 25 WHERE  name = "Alex Li"  把name=Alex Li的纪录的年龄改成25
5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句 就显示 查询出了多少条、修改语句就显示修改了多少条等。
"""
import os
import re
import time
from tabulate import tabulate

# 高亮显示字体颜色
red = '\033[1;31;40m'  # 红色
green = '\033[1;32;40m'  # 绿色
blue = '\033[1;34;40m'  # 蓝色
end = '\033[0m'  # 无色

# 高亮闪烁显示字体颜色
red_twinkle = '\033[5;31;40m'  # 红色,闪烁
green_twinkle = '\033[1;32;40m'  # 绿色,闪烁
blue_twinkle = '\033[1;34;40m'  # 蓝色,闪烁

# 数据相关
data_path = "data"  # 数据文件夹
staff_table = "staff_table"  # 数据表名
staff_db = os.path.join(data_path, staff_table + '.db')  # 路径全称
staff_db_swap = os.path.join(data_path, staff_table + '.swap')
FIELD_LEN = 7  # 表中字段必须是5

# query
keywords = {
    "star": "*",
    "from": "from",
    "where": "where"
}
field_symbol = {
    ">": ">",
    "<": "<",
    "=": "=",
    "like": "like"
}
field_keywords = {
    "staff_id": "staff_id",
    "name": "name",
    "age": "age",
    "phone": "phone",
    "dept": "dept",
    "enroll_date": "enroll_date"
}
sql_commands = {
    "find": "find",
    "add": "add",
    "del": "del",
    "update": "update"
}

# 字段比较> < =
def show_basic_field(query_list_head_field,user_list_tmp):
    list_tmp, list_tmp1, list_tmp2 = [],[],[]
    for line in query_list_head_field:
        print(line, end="      ")
        list_tmp1.append(line)
    print("")
    for i in user_list_tmp:
        for j in query_list_head_field:
            print(i[get_feild_id(j)], end="    ")
            list_tmp2.append(i[get_feild_id(j)])
        print("")

def field_symbol_gt(user_list,query_list_head_field, position3, position1):
    user_list_tmp, count = [], 0
    for k in user_list:
        if k[get_feild_id(position3)] > position1:
            count += 1
            k_str = ','.join(k).replace("\n", "")
            k_str = k_str.replace(',', "     ")  # 将逗号替换成空格
            user_list_tmp.append(k)
    show_basic_field(query_list_head_field, user_list_tmp)
    return count

def field_symbol_lt(user_list,query_list_head_field, position3, position1):
    user_list_tmp, count = [], 0
    for k in user_list:
        if k[get_feild_id(position3)] < position1:
            count += 1
            k_str = ','.join(k).replace("\n", "")
            k_str = k_str.replace(',', "     ")  # 将逗号替换成空格
            user_list_tmp.append(k)
    show_basic_field(query_list_head_field, user_list_tmp)
    return count

def field_symbol_eq(user_list,query_list_head_field, position3, position1):
    user_list_tmp, count = [], 0
    for k in user_list:
        if k[get_feild_id(position3)] < position1:
            count += 1
            k_str = ','.join(k).replace("\n", "")
            k_str = k_str.replace(',', "     ")  # 将逗号替换成空格
            user_list_tmp.append(k)
    show_basic_field(query_list_head_field, user_list_tmp)
    return count

field_symbol_compare = {
    ">": field_symbol_gt,
    "<": field_symbol_lt,
    "=": field_symbol_eq
}

# 错误输出
def msg_log(normal_data, color_data, font_color):
    """
    :param normal_data: 输出不带颜色字体
    :param color_data:  输出带颜色的字体
    :param font_color:  输出字体的颜色
    :return:
    """
    if not color_data.split():
        print(font_color + normal_data + end)
    else:
        print(normal_data + font_color + color_data + end)


# 初始化员工数据
def initial_employee_information():
    """
    初始化数据库，员工信息数据
    :return:
    """
    msg = """1,Alex Li,22,13651054608,IT,2013-04-01
2,Jack Wang,28,13451024608,HR,2015-01-07
3,Rain Wang,21,13451054608,IT,2017-04-01
4,Mack Qiao,44,15653354208,Sales,2016-02-01
5,Rachel Chen,23,13351024606,IT,2013-03-16
6,Eric Liu,19,18531054602,Marketing,2012-12-01
7,Chao Zhang,21,13235324334,Administration,2011-08-08
8,Kevin Chen,22,13151054603,Sales,2013-04-01
9,Shit Wen,20,13351024602,IT,2017-07-03
10,Shanshan Du,26,13698424612,Operation,2017-07-02"""
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    if not os.path.exists(staff_db):
        with open(staff_db, "w", encoding="utf-8") as fd:
            fd.write(msg)
        msg_log("员工信息数据初始化完毕", "", blue)


def show_prompt_information():
    """
    提示信息，方便用户根据提示语法输入相关命令提示进行操作
    :return:
    """
    msg = """
---------------------------------------- 迎进入员工信息增删改查程序 ----------------------------------------     
语法操作：
1.可进行模糊查询:
    find name,age from staff_table where age > 22
    find * from staff_table where dept = "IT"
    find * from staff_table where enroll_date like "2013"
2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
    语法: add staff_table Alex Li,18,134435344,IT,2015-10-29  
3.可删除指定员工信息纪录，输入员工id，即可删除
    语法: del from staff_tables where  id=3
4.可修改员工信息，语法如下:
    UPDATE staff_table SET dept = "Market" WHERE  dept = "IT" 把所有dept=IT的纪录的dept改成Market
    UPDATE staff_table SET age = 25 WHERE  name = "Alex Li"  把name=Alex Li的纪录的年龄改成25

命令提示：
1. 输入q/Q 退出当前应用
2. 输入 show  查看当前数据人员名单
    """
    print(msg)


def get_staff_id(staff_db):
    """
    :param staff_db: 员工人员数据表
    :return: 员工人员自增id
    """
    list_data = []
    with open(staff_db, 'r') as fd:
        for line in fd:
            list_data.append(line)
    auto_increment_id = list_data[-1].split(",")[0]
    return auto_increment_id


def get_staff_info(dbfile):
    data_list = []
    with open(dbfile, "r") as fd:
        for i in fd:
            data_list.append(str(i).split(','))
    return data_list


def get_feild_id(column):
    if column == "staff_id":
        column = 0
    elif column == "name":
        column = 1
    elif column == "age":
        column = 2
    elif column == "phone":
        column = 3
    elif column == "dept":
        column = 4
    elif column == "enroll_date":
        column = 5
    return column

def tabulate_show(data_list):
    title_table = [["staff_id", "name", "age", "phone", "dept", "enroll_date"]]
    user_list = title_table + data_list
    print(tabulate(user_list))

def show_employee_info():
    """
    格式化输出当前数据库里面人员名单
    :return:
    """
    user_list = get_staff_info(staff_db)
    tabulate_show(user_list)

def show_tables():
    """
    提示当前数据中表
    :return:
    """
    for file in os.listdir(data_path):
        if file.endswith(".db"):
            db_name = file.split(".db")[0]

    msg = """+----------------------------+
| employee_information       |
+----------------------------+
| %s                |
+----------------------------+
rows in set (0.00 sec)
""" % db_name
    print(msg)


def check_table(table):
    """
    :param table: 要判断的数据库的表
    :return: 返回bool值（表存在就返回True，否则返回False）
    """
    for file in os.listdir(data_path):
        if file.endswith(".db"):
            db_name = file.split(".db")[0]
    if db_name == table:
        return True
    else:
        return False


def check_filed(table, filed):
    pass


def list_remove_null(content):
    """
    :param content:  sql 语句
    :return:         去除空的剩余sql语句
    """
    content_list = re.split(' |=', content)  # 分解sql命令
    while '' in content_list:  # 去除sql列表命令中的空元素
        content_list.remove('')
    return content_list


def list_replace(content, old, new):
    """
    嵌套列表数据修改数据操作
    :param content:  传入2层列表(嵌套列表)
    :param old:     旧字段
    :param new:     新字段
    :return:
    """
    p = content.index(old)
    content.remove(old)
    content.insert(p, new)
    return content


def check_user(dbfile, field):
    """
    通过检查唯一键filed，来检查数据库，用户存在就返回True，否则返回False
    :param dbfile: 要检查的数据库
    :param field: 要检查的字段
    :return: bool，True|False
    """
    with open(dbfile, "r", encoding="utf-8") as fd:
        for line in fd.readlines():
            if field in line:
                return True
            else:
                return False

def storage_data(data_value, rewrite=True):
    """
    :param data_value: 把列表data_value中的数据写入文件
    :return:
    """
    if rewrite == True:
        with open(staff_db, "w", encoding="utf-8") as fd:
            for item in data_value:
                fd.write(",".join(item))
    else:
        with open(staff_db, "a+", encoding="utf-8") as fd:
            fd.write("\n")
            fd.write(",".join(data_value))

def query_operation(content):
    """
    根据条件查询当前数据库中数据
    :param content:  传入sql语句
    :return:
    """
    user_list_tmp = []
    user_list = get_staff_info(staff_db)
    query_list = content.split()
    query_list_head, position1, position2, position3, position4 \
        = query_list[0], query_list[-1], query_list[-2], query_list[-3], query_list[-4]  # 去除 * ,name/age
    if position3 not in field_keywords:
        msg_log("抱歉，输入命令错误,字段不正确，请打印h，查看规则", "", red)
    else:
        if query_list_head == '*':  # 判断查询语句，关键字是否为*号
            if position2 == field_symbol[">"]:
                pass
            elif position2 == field_symbol["<"]:
                pass
            elif position2 == field_symbol["="]:  # 判断类似语句 find * from staff_table where dept = "IT"
                count = 0
                for k in user_list:
                    if eval(position1) in k:
                        count += 1
                        user_list_tmp.append(k)
                tabulate_show(user_list_tmp)
            elif position2 == field_symbol["like"]:  # 判断类似语句  find * from staff_table where enroll_date like "2013"
                count = 0
                for k in user_list:
                    if eval(position1) in k[get_feild_id(position3)]:
                        count += 1
                        user_list_tmp.append(k)
                tabulate_show(user_list_tmp)
            else:
                msg_log("抱歉，输入命令错误,字段不正确，请打印h，查看规则", "", red)
        else:  # find name,age from staff_table where age >|<|= 22  三种情况
            query_list_head_field = query_list_head.split(",")
            count = field_symbol_compare.get(position2)(user_list,query_list_head_field, position3, position1)
            msg_log("查询到语句条数为: ", "%s" % count, green)  # 打印出受影响的条数

def add_operation(content):
    """
    :param content: 传入新增用户sql语句
    :return:
    """
    phone_list = []
    table, content = content.strip().split(" ", 1)
    content = content.split(",")
    user_list = get_staff_info(staff_db)
    if len(content) != 5:  # 判读输入sql的字段长度必须是5，否则打印命令错误
        msg_log("抱歉，输入命令错误,字段不正确，请打印h，查看规则", "", red)
    else:
        user_list = get_staff_info(staff_db)
        for line in range(len(user_list)):  # 去除文件中空行
            if ['\n'] in user_list:
                user_list.remove(['\n'])

        for i in range(len(user_list)):  # 保存当前数据库中的所有电话清单到列表
            phone_list.append(user_list[i][3])

        if content[2] in phone_list:  # 判断电话是否存在
            msg_log("抱歉，用户名已经存在", " ", red)
        else:
            increment_id = (len(user_list) + 1)
            content.insert(0, str(increment_id))
            content.append("\n")
            storage_data(content, rewrite=False)
            msg_log("新增语句，影响的行数为", "%s" % 1, green)


def del_operation(content):
    """
    根据id号删除用户数据
    :param content: sql语句内容
    :return:
    """
    tmp_id, tmp_id_flag, staff_id = 0, True, []  # 初始化临时参数
    del_id = int(content.split()[-1].split("=")[-1]) - 1  # 获取要删除的id
    user_list = get_staff_info(staff_db)  # 保存当前数据库中的所有电话清单到列表

    for i in range(len(user_list)):
        if str(del_id + 1) == user_list[i][0]:
            tmp_id, tmp_id_flag = i, True
            break
        else:
            tmp_id_flag = False
    if not tmp_id_flag:
        msg_log("抱歉，你要删除的数据不存在", "", red)
    else:
        del user_list[tmp_id]
        storage_data(user_list)
        msg_log("删除语句，影响的行数为", "%s" % 1, green)


def update_operation(content):
    """
    :param content: 传入查询sql语句
    :return:
    """
    update_keywords, content_list, data_value_tmp, count = ["set", "where"], [], [], 0
    data_value = get_staff_info(staff_db)
    content_list = list_remove_null(
        content)  # 分解sql命令 ['staff_table', 'SET', 'dept', '"Market"', 'WHERE', 'dept', '"IT"']
    if content_list[0] == "staff_table":  # 判读数据表,关键字例如where，set和要查询的字段例如name必须存存在(合法)
        # 判断sql 语法 合法性
        if content_list[1].lower() in update_keywords and content_list[4].lower() in update_keywords and \
                        content_list[2].lower() in field_keywords and content_list[5] in field_keywords:
            # 修改相同列， 例如 UPDATE staff_table SET dept="Market" WHERE  dept = "IT"
            if content_list[2] == content_list[5]:
                for line in data_value:
                    if eval(content_list[6]) in line[get_feild_id(content_list[5])]:
                        count += 1
                        line = list_replace(line, eval(content_list[6]), eval(content_list[3]))
                    data_value_tmp.append(line)
                storage_data(data_value_tmp)
            else:  # 修改不同列，UPDATE staff_table SET age=25 WHERE  name = "Alex Li"
                if 'WHERE' in content:
                    pre_content, after_content = content.split("WHERE")
                pre_content = pre_content.split()
                old_field_key = after_content.split("=")[0].split()[0]
                old_field_value = eval(after_content.split("=")[-1])
                new_filed_key, new_filed_value = pre_content[2], pre_content[4]
                for line in data_value:
                    if old_field_value in line:
                        count += 1
                        list_replace(line, line[get_feild_id(new_filed_key)], new_filed_value)
                    data_value_tmp.append(line)
                storage_data(data_value_tmp)
            msg_log("修改语句条数为: ", "%s" % count, green)  # 打印出受影响的条数
        else:
            msg_log("抱歉，你输入的SQL语法错误:", " ", red)
    else:
        msg_log("抱歉，你的输入的数据库表不存在:", " ", red)


def parse_input_data(sql):
    """
    解释输入数据，
    1. 解析动作，是add，find，del，update
    2. 解释内容，sql的具体操作
    :param sql: 操作sql语句
    :return:
    """
    command, content = sql.split(' ', 1)
    msg_log("本次执行操作语句：", "%s" % sql, blue)
    if command.lower() == sql_commands["find"]:  # 查询操作
        query_operation(content)
    elif command.lower() == sql_commands["add"]:  # 新增操作
        add_operation(content)
    elif command.lower() == sql_commands["del"]:  # 删除操作
        del_operation(content)
    elif command.lower() == sql_commands["update"]:  # 更新操作
        update_operation(content)
    else:
        msg_log("抱歉，你输入的SQL命令不存在:", "%s" % sql, red)


def main_process():
    """
    主函数通过输入，匹配相对应的功能，解析sql，对应输出数据
    :return:
    """
    initial_employee_information()
    query_status = True
    while query_status:
        input_data = input("请输入操作语句，<h|H 帮助>: ").strip()
        if input_data.lower() == "q":  # 输入q/Q 退出操作
            query_status = False
        elif not input_data:
            msg_log("抱歉，输入不能为空", "", red)
        elif input_data.lower() == "h":  # 展示提示信息，以便按照语法输入
            show_prompt_information()
        elif input_data.lower().split()[0] == "show":  # 查看人员信息
            show_employee_info()
        else:
            if input_data.split()[0].lower() in sql_commands and len(input_data.split()) > 3:
                parse_input_data(input_data)  # 解析输入的sql语法
            else:
                msg_log("抱歉，sql命令不存在: ", "%s" % input_data, red)


if __name__ == "__main__":
    main_process()