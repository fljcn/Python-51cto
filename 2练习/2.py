#_*_coding:utf-8_*_
#第一部分：sql解析
def sql_parse(sql): #insert delete update select
    '''
    把sql字符串切分，提取命令信息，分发给具体的解析函数去解析
    :param sql:
    :return:
    '''''
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }
    # print('sql str is %s' %sql)
    sql_l=sql.split(' ')
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
    return res

def insert_parse(sql_l):
    '''
    定义insert语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:
    :return:
    '''''
    pass

def delete_parse(sql_l):
    '''
    定义delete语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:
    :return:
    '''''
    pass

def update_parse(sql_l):
    '''
    定义update语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:
    :return:
    '''''
    pass

def select_parse(sql_l):
    '''
    定义select语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:
    :return:
    '''''
    print('from in the select_parse \033[42;1m%s\033[0m' %sql_l)
    sql_dic={
        'func':select,
        'select':[], #查询字段
        'from':[],   #数据.表
        'where':[],  #filter条件
        'limit':[],  #limit条件
    }
    return handle_parse(sql_l,sql_dic)

def handle_parse(sql_l,sql_dic):
    '''
    执行sql解析操作，返回sql_dic
    :param sql_l:
    :param sql_dic:
    :return:
    '''''
    print('sql_l is \033[41;1m%s\033[0m \nsql_dic is \033[41;1m%s\033[0m' %(sql_l,sql_dic))
    tag=False
    for item in sql_l:
        if tag and item in sql_dic:
            tag=False
        if not tag and item in sql_dic:
            tag=True
            key=item
            continue
        if tag:
            sql_dic[key].append(item)
    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where')) #['id>4', 'and', 'id<10']
    print('from in the handle_parse sql_dic is \033[43;1m%s\033[0m' %sql_dic)
    return sql_dic

def where_parse(where_l):#['id>', '4','','and', 'id', '<10']-->['id>4', 'and', 'id<10']
    res=[]
    key=['and','or','not']
    char=''
    for i in where_l:
        if len(i) == 0:continue
        if i in key:
            #i为key当中存放的逻辑运算符
            if len(char) != 0:
                char=three_parse(char)
                res.append(char) #char='id>4'--->char=['id','>','4']
                res.append(i)
                char=''
        else:
            char+=i #'id<=10' #id<=10--->['id','<=','10']
    else:
        char = three_parse(char)
        res.append(char)
    #['id>4', 'and', 'id<=10']-->[['id','>','4'],'and',['id','<=','10']]
    print('from in the where_parse res is \033[43;1m%s\033[0m' % res)
    return res
def three_parse(exp_str):
    #'id<=10'-->['id','<=','10']
    key=['>','<','=']
    res=[]
    char=''
    opt=''
    tag=False
    for i in exp_str:
        if i in key:
            tag=True
            if len(char) != 0:
                res.append(char)
                char=''
            opt+=i  #opt='<='
        if not tag:
            char+=i #char='10'

        if tag and i not in key:
            tag=False
            res.append(opt)
            opt=''
            char+=i #char='1'
    else:
        res.append(char)

    #新增解析like的功能
    if len(res) == 1:
        res=res[0].split('like')
        res.insert(1,'like')
    print('three_parse res is \033[43;1m%s\033[0m' % res)
    return res







#第一部分：sql执行
def sql_action(sql_dic):
    '''
    从字典sql_dic提取命令，分发给具体的命令执行函数去执行
    :param sql_dic:
    :return:
    '''''
    return sql_dic.get('func')(sql_dic)

def insert(sql_dic):
    pass

def delete(sql_dic):
    pass

def update(sql_dic):
    pass

def select(sql_dic):
    print('from select sql_dic is %s' %sql_dic)
    #first：from
    db,table=sql_dic.get('from')[0].split('.')

    fh=open("%s/%s" %(db,table),'r',encoding='utf-8')
    #second:where
    filter_res=where_action(fh,sql_dic.get('where'))
    # for record in filter_res:
    #     print('filter res is %s' %record)
    #third:limit
    limit_res=limit_action(filter_res,sql_dic.get('limit'))
    # for record in limit_res:
    #     print('limit res is %s' %record)
    #lase:select
    search_res=search_action(limit_res,sql_dic.get('select'))
    # for record in search_res[-1]:
    #     print('limit res is %s' %record)

    return search_res

def where_action(fh,where_l):
    #id,name,age,phone,dept,enroll_data
    # 10,吴东杭,21,17710890829,运维,1995-08-29
    #['id>7', 'and', 'id<10', 'or', 'namelike李']
    print('in where_action \033[41;1m%s\033[0m' %where_l)
    res=[]
    logic_l=['and','or','not']
    title="id,name,age,phone,dept,enroll_data"
    if len(where_l) != 0:
        for line in fh:
            dic=dict(zip(title.split(','),line.split(','))) #一条记录
            #逻辑判断
            logic_res=logic_action(dic,where_l)
            if logic_res:
                res.append(line.split(','))
    else:
        res=fh.readlines()
    return res

def logic_action(dic,where_l):
    res=[]
    # where_l=[['name', 'like', '李'], 'or', ['id', '<=', '4'], 'or', ['id', '=', '24']]
    for exp in where_l:
        #dic与exp做bool运算
        if type(exp) is list:
            #做bool运算
            exp_k,opt,exp_v=exp
            if exp[1] == '=':
                opt="%s=" %exp[1]
            if dic[exp_k].isdigit():
                dic_v=int(dic[exp_k])
                exp_v=int(exp_v)
            else:
                dic_v="'%s'" %dic[exp_k]
            if opt != 'like':
                exp=str(eval("%s%s%s" %(dic_v,opt,exp_v)))
            else:
                if exp_v in dic_v:
                    exp='True'
                else:
                    exp='False'
        res.append(exp)  #['True','or','Fasle','or','True']

    res=eval(' '.join(res))
    return res

def limit_action(filter_res,limit_l):
    res=[]
    if len(limit_l) != 0:
        index=int(limit_l[0])
        res=filter_res[0:index]
    else:
        res=filter_res
    return res

def search_action(limit_res,select_l):
    res=[]
    fields_l=[]
    title = "id,name,age,phone,dept,enroll_data"
    if select_l[0] == '*':
        fields_l=title.split(',')
        res=limit_res
    else:
        for record in limit_res:
            dic=dict(zip(title.split(','),record))
            r_l=[]
            fields_l=select_l[0].split(',')
            for i in fields_l: #id,name
                r_l.append(dic[i].strip())
            res.append(r_l)
    return (fields_l,res)



if __name__ == '__main__':
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit':break
        if len(sql) == 0 :continue

        sql_dic=sql_parse(sql)
        # print('main res is %s' %sql_dic)
        if len(sql_dic) == 0:continue

        res=sql_action(sql_dic)
        print('\033[43;1m%s\033[0m' %res[0])
        for record in res[-1]:
            print('limit res is %s' %record)