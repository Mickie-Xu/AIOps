import numpy as np
from pyecharts import Pie

attr = ["A", "B", "C"]
v1 = [381, 236, 53]

pie = Pie("异常比较", title_pos="center")
pie.add("异常比较", attr, v1,
        is_label_show=True,
        center=[50, 50],
        radius=[40, 75],
        legend_orient="vertical",
        legend_pos="left"
       )
pie
pie.render(r"C:\Users\Administrator\Desktop\异常比较.html")