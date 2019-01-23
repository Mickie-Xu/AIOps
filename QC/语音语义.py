# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:04:14 2018

@author: xuziyi

create data of qc aiops 2018
"""

import numpy as np
from pyecharts import Scatter

x = np.arange(100)
y = np.arange(100) + np.random.normal(loc=0, scale=15, size=100)

scatter =Scatter("相关性检验")
scatter.add("相关性", x, y, yaxis_min=0,yaxis_max=101)
scatter.show_config()
scatter.render(r"C:\Users\Administrator\Desktop\相关性检验.html")
