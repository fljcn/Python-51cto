old_str = '乔一菲'
new_str = '肛娘'
f = open( '联系方式 .txt','r+',encoding='utf-8')
data = f.read()

data = data.replace(old_str,new_str)
# 把文件指针移动到文件头
f.seek(0)
f.write(data)
print ('===================')
print (data)

f.flush()
f.close()


