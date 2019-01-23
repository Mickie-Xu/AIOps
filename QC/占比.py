import numpy as np
from pyecharts import Gauge

gu = Gauge("模型精度占比")
gu.add("在线", "离线", 62.63)

gu.render(r"C:\Users\Administrator\Desktop\占比.html")