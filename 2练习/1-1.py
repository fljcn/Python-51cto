def f2():
    print(111)

def f1(sss):
    sss()
    print("f1")

f1(f2)
