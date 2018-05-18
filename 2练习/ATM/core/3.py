# -*- coding:utf-8 -*-
from pycallgraph import PyCallGraph  
from pycallgraph.output import GraphvizOutput  
  
from main import *  
# ddd是你想绘制函数关系图的py文件  
graphviz = GraphvizOutput(output_file=r'./trace_detail.png') 
# graphviz = GraphvizOutput(output_file=r'./trace_detail.png')
 
# 这里直接输入ddd.py里面的函数就可以直接绘制出来了，打开trace_detail.png就能看到了 