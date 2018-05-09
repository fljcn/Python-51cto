#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

def foo(bar=[]):
    bar.append('bar')
    return bar
print(foo())
print(foo())