num_list = []
f=open('black_user.txt','a')
# f.write(str(1000)+'\n')
f=open('black_user.txt')
abc= f.readlines()
for i in abc:
    num_list.append(i.strip())
print (abc)
abc1 = (num_list[-1])

print (abc1)
print (type(abc1))

f.close()