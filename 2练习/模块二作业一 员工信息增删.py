#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

# 第一部分： sql解析
def sql_parse(sql):    #sql解析: insert delete update select
    '''
    把sql字符串切分，提取命令信息，分发给具体的解析函数去解析
    :param sql:
    :return:
    '''
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }
    print('sql str is: %s' %sql)
    sql_l=sql.split(' ')
    func=sql_l[0]
    print('sql_l str is: %s' %sql_l)
    print('func str is: %s' %func)
    res=' '

    if func in parse_func:
        parse_func[func](sql_l)

    return res

def insert_parse(sql_l):
    '''
    定义insert语句的语法结构，执行sql解析操作，返回sql_dic

    :param sql:
    :return:
    '''
    pass

def delete_parse(sql_l):
    '''
    定义deletet语句的语法结构，执行sql解析操作，返回sql_dic


    :param sql:
    :return:
    '''
    pass

def update_parse(sql_l):
    '''
        定义update语句的语法结构，执行sql解析操作，返回sql_dic

    :param sql:
    :return:
    '''
    pass

def select_parse(sql_l):
    '''
        定义select语句的语法结构，执行sql解析操作，返回sql_dic

    :param sql:
    :return:
    '''
    print('from in the select_parse \033[42;1m %s\033[0m' %sql_l)
    sql_dic ={
        'func':select,
        'select':[],   #查询字段
        'from':[],      #数据，表
        'where':[],     #filter条件
        'limit':[],     #limit条件
    }
    return handle_parse(sql_l ,sql_dic)


def handle_parse(sql_l,sql_dic):
    '''
    执行sql解析操作，返回sql_dic

    :param sql_l:
    :param sql_dic:
    :return:
    '''
    print('sql_l is \033[41;1m %s \033[0m \n sql_dic is \033[42;1m %s \033[0m ' % (sql_l,sql_dic))


# 第二部分：sql执行
def sql_action(sql_dic):
    '''
    从字典sql_dic提取命令，分发给具体的命令执行函数去执行
    :param sql_dic:
    :return:
    '''
    pass

def insert(sql_dic):
    pass

def delete(sql_dic):
    pass

def update(sql_dic):
    pass

def select(sql_dic):
    pass



if __name__ == '__main__':
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit':break
        if len(sql) == 0:continue

        # sql解析
        sql_dic=sql_parse(sql)
        # print('main res is %s' %sql_dic)
        if len(sql_dic) == 0:continue
        #sql执行
        sql_action(sql_dic)
