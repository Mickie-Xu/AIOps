import numpy as np
from pyecharts import Line

line = Line("成功率")
attr=np.arange(30)+1
v1=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
line.add("n次试验",attr,v1)
line.render(r"C:\Users\Administrator\Desktop\成功率.html")