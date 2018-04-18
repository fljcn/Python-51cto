# def add()

accounts={}
with open("data.txt","r+",encoding="utf-8") as f:
    raw_data = f.readlines()
print("raw_data",raw_data)

for i in raw_data:
    i=i.strip()
    if not i.startswith("#"): #跳过注释行,开头有#为真，如果没有为假
        i=i.split(',')
        # print('i:',i)
        accounts[i[0]]=i

print('accounts',accounts)