'''作业题目：编写登陆认证程序
作业需求：
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序

升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）'''

# 方法一
# user = 'user1'
# password = 'user1.1'
# exit_flah = False
# count = 0
# while not exit_flah:
#     _user = input('请输入用户名：')
#     _password = input("请输入密码：")
#     if _user == user and _password == password:
#         print('欢迎%s登录系统' % (user))
#     exit_flah = True
#     count += 1
#     if count == 3:
#         exit_flah = True

# 方法二
# user = 'user1'
# password = 'user1.1'
# count = 0
# while count < 3:
#     _user = input('请输入用户名：')
#     _password = input("请输入密码：")
#     if _user == user and _password == password:
#         print('-----欢迎%s登录系统!------' % (user))
#         break
#         else:
#              print (-----请重新再来------)
#     count += 1

# 升级需求
# 方法一
users = [['user1','user1.1'],['user2','user2.2'],['user3','user3.3'],['user4','user4.4']]
lock_names = []
exit_flag = False
# count = 0
# while not exit_flag:

_user = input('请输入用户名：')
_password = input("请输入密码：")
for index,u in enumerate(users):
    if u[0] == _user and u[1] == _password:
        print ('-----欢迎%s登录系统!------' % (_user))
    else:
        lock_names.append(users[0][1])
        print(lock_names)
