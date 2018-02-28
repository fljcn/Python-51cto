#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

import os
f_name = '联系方式 .txt'
f_new_name = '%s.new' % f_name

old_str = '乔一菲'
new_str = '肛娘'
f = open(f_name,'r',encoding='utf-8')
f_new = open (f_new_name,'w',encoding='utf-8')

for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)

    f_new.write(line)

f.close()
f_new.close()

os.replace(f_new_name,f_name)
