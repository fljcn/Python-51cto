
info = ['Name','Age','Job','Dept','Phone']
account1=[]

with open('account.txt',encoding='utf-8') as file :
    account = file.readlines()
    print(account)
    for i in account:
        i = i.strip()
        account1.append(i)
print('account0',account1[0])
print('account1',account1[1])
print('account2',account1[2])
print('Name',account1[0])



# def _print(abc,sep=' '):
#     print()


