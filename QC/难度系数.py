import random
from pyecharts import Bar
 
X_AXIS = ["基于离散型数据", "基于连续型数据"]
bar = Bar("难度系数", "据7位专家评断")
bar.add("专家A", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.add("专家B", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.add("专家C", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.add("专家D", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.add("专家E", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.add("专家F", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.add("专家G", X_AXIS, [random.randint(10, 100) for _ in range(2)])
bar.render(r"C:\Users\Administrator\Desktop\难度系数.html")