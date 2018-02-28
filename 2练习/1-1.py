def stu_register(name,age,course):
    print(name,age,course)
    # if age > 22:
    #     return True
    # else:
    #     return False
    # return 888      #后面的语句将不执行
    return  name,age    #返回列表
    # return [name,age]     #返回列表
    print (111)

status = stu_register('Peiqi',29,'安保')
print ('status:',status)