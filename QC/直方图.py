import numpy as np
from pyecharts import Bar

attr = ["x1", "x2", "x3", "x4", "x5"]
v1 = [22.57 ,
22.88 ,
22.88 ,
22.72 ,
23.03 
]
v2 = [23.18 ,
23.26 ,
22.95 ,
23.18 ,
23.03 
]
v3 = [22.65 ,
23.18 ,
22.57 ,
22.80 ,
23.10 
]
v4 = [22.88 ,
22.57 ,
22.65 ,
22.57 ,
22.95  
]
v5 = [22.95 ,
23.26 ,
23.03 ,
23.03 ,
23.26 
]

bar = Bar()
bar.add("paas", attr, v1, mark_point=["max"])
bar.add("devops", attr, v2, mark_line=["max"])
bar.add("aiops", attr, v3, mark_line=["max"])
bar.add("aiops", attr, v4, mark_line=["max"])
bar.add("aiops", attr, v5, mark_line=["max"])
bar
bar.render(r"C:\Users\Administrator\Desktop\直方图.html")
