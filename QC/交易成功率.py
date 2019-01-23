# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:04:14 2018

@author: xuziyi

create data of qc aiops 2018
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Scatter

x = np.arange(100)
y_ai = np.random.normal(loc=0.99991, scale=0.00003, size=100)
y_dev = np.random.normal(loc=0.99990, scale=0.00003, size=100)
y_paas = np.random.normal(loc=0.99988, scale=0.00003, size=100)

scatter =Scatter("交易成功率")
scatter.add("aiops", x, y_ai)
scatter.add("devops", x, y_dev)
scatter.add("paas", x, y_paas,yaxis_min=0.9998,yaxis_max=1)
scatter.show_config()
scatter.render(r"C:\Users\Administrator\Desktop\交易成功率.html")
