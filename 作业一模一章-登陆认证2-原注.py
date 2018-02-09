import os
user_info = {
 'mary': {'password': '123456'},
 'tom': {'password': '12356'},
 'jerry': {'password': '123456'},
 }    #建立用户和密码字典
if not os.path.isfile('black_user' ):   # 判断记录锁定文件不存在
    f = open('black_user','w')    #不存在 新建一个‘black_user’文件
    f = open('black_user')         #读取black_user 文件,防止上一条以只写方式打开文件
else:
    f = open('black_user')          #如果文件存在直接打开
user = f.readlines()     #以行的方式读取，返回的是一个字符串对象，赋值给 user
lock_user = []            #新建锁定用户列表
for i in user:          #把black_user中的用户追加到lock_user列表中
    i = i.strip()
    lock_user.append(i)
print('锁定用户',lock_user)     #显示哪些用户被锁定
f.close()                         # 关闭lock_user文件
count = 0
count1 = 0
while 1:        #永远循环  等于  while True:
    username = input('请输入用户名')
    if username in lock_user:      #username在lock_user列表中
       print('该用户已被锁定')     #打印“该用户已被锁定'”
       exit(0)                      # 无错误退出
    if not username in user_info:   #username不在字典user_info中，
        print('请输入正确的用户名')
        if count == 2:              #输入3次，将退出
            print('输入次数已达上限，即将退出')
            exit(0)                 # 无错误退出
    else:                          # 用户名在字典user_info中
        while count1 < 3:           #循环3次
            password = input('请输入密码')
            if password == user_info[username]['password']:  #判断输入的密码是否等于字典 user_info中 相应用户名的密码
                print('welcome',username)
                exit(0)
            else:
                print('密码错误，请重新输入')
                count1 += 1
                continue               #跳出本次循环
        if count1 == 3:
            print('密码输入错3次，该用户将被锁定')
            f = open('black_user','a')          #打开文件black_user，并允许追加内容
            f.write('%s\n' % (username))        #把username写入到black_user文件
            f.close()
            exit(0)
    count += 1