
account_file = "account.txt"
f = open(account_file,"r+",encoding='utf-8')
raw_data = f.readlines()
accounts = {}
accounts1 = []
print('raw_data:',raw_data)
#把账户数据从文件里读书来，变成dict,这样后面就好查询了
for line in raw_data:

    line = line.strip()
    # if not  line.startswith("#"):
    items = line.split(",")
    # items = line
    print('items:',items[0])
    # accounts[items[0]] = items
    accounts1.append(items)
print ('accounts1:',accounts1)
