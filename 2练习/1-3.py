def js(n):
    if n == 1:
        return 1
    else:
        return n*js(n-1)

print (js(5))