import numpy as np
from pyecharts import Line

line = Line("稳定性对比", title_top="50%")
v1 = np.random.normal(loc=0.84, scale=0.03, size=7)
v2 = np.random.normal(loc=0.88, scale=0.03, size=7)

attr = ['一', '二', '三', '四', '五', '六', '七']
line.add("前端成功率",attr,v1,mark_point=["max", "min"],mark_line=["average"],)
line.add("后台成功率",attr,v2,mark_point=["max", "min"],mark_line=["average"],legend_top="50%",yaxis_min=0.8,yaxis_max=0.92)

line.render(r"C:\Users\Administrator\Desktop\稳定性对比.html")