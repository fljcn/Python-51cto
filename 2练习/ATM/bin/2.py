# 追踪代码
# -*- coding:utf-8 -*-
from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput

from atm import *

graphviz = GraphvizOutput(output_file=r'./trace_detail.png')
