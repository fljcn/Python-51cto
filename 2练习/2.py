# 求188除以2，5次，并把最后一次结果返回
def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count+1)
    else:
        return n

res = calc(188,1)
print ('res',res)