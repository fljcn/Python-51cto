# -*- coding:utf-8 -*-
from pycallgraph import PyCallGraph  
from pycallgraph.output import GraphvizOutput  
  
from main import *  
# ddd��������ƺ�����ϵͼ��py�ļ�  
graphviz = GraphvizOutput(output_file=r'./trace_detail.png') 
# graphviz = GraphvizOutput(output_file=r'./trace_detail.png')
 
# ����ֱ������ddd.py����ĺ����Ϳ���ֱ�ӻ��Ƴ����ˣ���trace_detail.png���ܿ����� 