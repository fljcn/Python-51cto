
# 定义三个函数：
# 1、用于打印个人信息
# 2、回写文件
# 3、修改个人信息

#打印个人信息
def print_personal_info(account_dict,username):
    personal_data = account_dict[username]
    info = '''
    -----------------------
    Name:   %s
    Age :   %s
    Job :   %s
    Dept:   %s
    Phone:  %s
    -----------------------
    '''% (personal_data[2],personal_data[3],personal_data[4],personal_data[5],personal_data[6])
    print(info)


#文件回写
def save_back_to_file(account_dict):
    with open("account.txt","r+",encoding="utf-8") as f:
        f.seek(0)   #回到文件头
        f.truncate()    #清空文件
        for i in account_dict:
            row=','.join(account_dict[i])   #把列表转换成字符
            f.write("%s\n" % (row))

#个人信息修改
def  change_personal_info(account_dict,username):
    personal_data=account_dict[username]
    print('personal_data',personal_data)
    column_names = ['Username', 'Password', 'Name', 'Age', 'Job', 'Dept', 'Phone']  # 对应60行语句
    # for index,k in enumerate(accounts):  #错误（accounts）
    for index,k in enumerate(personal_data):
        if index > 1:    #跳过前两字段
            # print (('%s. %s.   %s') % (index,column_names[k],k))   #打印修改列表  错误column_names[k]
            print (('%s. %s.   %s') % (index,column_names[index],k))   #打印修改列表

    choice = input("请输入修改的序号").strip()
    if choice.isdigit():
        choice=int(choice)
        if choice > 0 and choice < len(personal_data):
            column_data = personal_data[choice]
            print("当前值",column_data)
            new_val = input('输入修改值').strip()
            if new_val:
                personal_data[choice] = new_val
                print(personal_data)

                save_back_to_file(account_dict)
            else:
                print("不能为空。。。")

#把账户文件读取出来转换成dict，便于后面查询
accounts={}
with open("account.txt","r+",encoding="utf-8") as f:
    raw_data = f.readlines()
print("raw_data",raw_data)

for i in raw_data:
    i=i.strip()
    if not i.startswith("#"): #跳过注释行,开头有#为真，如果没有为假
        i=i.split(',')
        # print('i:',i)
        accounts[i[0]]=i

print('accounts',accounts)

menu = '''
1. 打印个人信息
2. 修改个人信息
3. 修改密码
'''

count = 0
while  count < 3:
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    if username in accounts:
        if password == accounts[username][1]:
            print("欢迎%s".center(50,'=')% username)
            while True:
                print(menu)
                user_choice = input('>>>').strip()
                if user_choice.isdigit():
                    user_choice=int(user_choice)
                    if user_choice == 1:
                        print_personal_info(accounts,username)
                    elif user_choice == 2:
                        change_personal_info(accounts,username)
                elif user_choice ==  'q':
                    exit ("退出程序")
        else:
            print ('用户名、密码错误！')
    else:
        print ('用户名错误！')
    count += 1
print ('输入错误超过3次！')








