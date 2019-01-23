import numpy as np
from pyecharts import Bar

attr = ["设计时间", "搭建时间", "开发时间", "测试时间", "部署时间"]
v1 = [3, 15, 60, 12, 4]
v2 = [4, 14, 55, 10, 5]
v3 = [5, 12, 48, 8, 5]

bar = Bar()
bar.add("paas", attr, v1, mark_point=["max"], is_stack=True)
bar.add("devops", attr, v2, mark_line=["max"], is_convert=True, is_stack=True)
bar.add("aiops", attr, v3, mark_line=["max"], is_convert=True, is_stack=True)
bar
bar.render(r"C:\Users\Administrator\Desktop\周期耗时.html")
