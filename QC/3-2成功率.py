import numpy as np
import pandas as pd
from pyecharts import Line

n = np.random.normal(loc=0.9995, scale=0.00002, size=12)
m = []
for i in n:
    m.append((1-i)*5.6*100000000*30)
    continue

print(n)
print(m)

line = Line("17.3-18.2成功率")
attr = ['17.3', '17.4','17.5','17.6','17.7','17.8','17.9','17.10','17.11','17.12','18.1','18.2',]
line.add("月成功率",attr,n,yaxis_min=0.9992,yaxis_max=0.9998)
line.render(r"C:\Users\Administrator\Desktop\月成功率.html")