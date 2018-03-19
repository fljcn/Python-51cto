#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

def js(n):
    if n == 1:
        return 1
    else:
        return n*js(n-1)

print(js(5))