import numpy as np
from pyecharts import Pie

attr = ["16便利店",
"16超市",
"16大型超市",
"16百货店",
"16专业店",
"16专卖店",
"15便利店",
"15超市",
"15大型超市",
"15百货店",
"15专业店",
"15专卖店",
"14便利店",
"14超市",
"14大型超市",
"14百货店",
"14专业店",
"14专卖店",
]
v1 = [23495,
715963,
1408976,
3321624,
1829741,
355918,
22174,
648000,
1495975,
3623198,
1737108,
415597,
15630,
568451,
1365523,
3826675,
1627269,
366609,
]

pie = Pie("销售饼图", title_pos="center")
pie.add("销售饼图", attr, v1,
        is_label_show=True,
        center=[50, 50],
        radius=[40, 75],
        legend_orient="vertical",
        legend_pos="left"
       )
pie
pie.render(r"C:\Users\Administrator\Desktop\销售饼图.html")