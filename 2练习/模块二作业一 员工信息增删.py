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
    tag=False
    for item in sql_l:
        if tag and item in sql_dic:
            tag=False
        if not tag and item in sql_dic:
            tag = True
            key = item
            # print('Item1:\033[41;1m%s \033[0m' %item)

            continue
        if tag:
            sql_dic[key].append(item)    #添加到 sql_dic
        # print ('Item2:',item)
    print('from in the handle_parse sql_dic is \033[43;1m %s \033[0m' %sql_dic)

    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where'))    #['id>4','and','id<10']
    return sql_dic

def where_parse(where_l):    #['id>', '4', 'and', 'id', '<10']  -->  ['id>4','and','id<10']
    res= []
    key=['and','or','not']
    char=' '
    for i in where_l:
        if len(i) == 0:continue
        if i in key:
            # i为key当中存放的逻辑运算符
            if len(char) != 0:
                res.append(char)
                res.append(i)
                char=' '
        else:
            char+=i   #'id>4'
    else:
        res.append(char)
    print('from in the where_parse res is:\033[41;1m %s \033[0m' %res)
    return res


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
