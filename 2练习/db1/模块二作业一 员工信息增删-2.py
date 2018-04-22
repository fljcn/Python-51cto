 #!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng
def sql_parse(sql):
    '''
    把sql字符串切分，提取命令信息，分发给具体解析函数执行
    :param sql:
    :return:
    '''
    pass

def insert_parse(sql):
    '''
    定义insert语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:
    :return:
    '''
    pass

def delete_parse(sql):
    pass

def update_parse(sql):
    pass

def select_parse(sql):
    pass


def sql_action(sql_dic):
    pass

if __name__ == '__main__':
    while True:
        sql = input("sql>").strip()
        if sql == 'exit':break
        if len(sql) == 0:continue

        sql_dic=sql_parse(sql)

        res=sql_action(sql_dic)