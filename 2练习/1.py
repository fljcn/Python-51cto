import c
# f = open (file='联系方式 .txt',mode='r',encoding=('utf-8'))
f = open (file='联系方式 .txt',mode='rb')   # rb二进制模式，不能跟encoding
data = f.read()
f.close()
print (chardet.detect(data))



