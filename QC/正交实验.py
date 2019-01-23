import numpy as np
import pandas as pd
from pyecharts import Line

n = []
n11=[]
n12=[]
n13=[]
n21=[]
n22=[]
n23=[]
n31=[]
n32=[]
n33=[]
s=[]

for i in np.arange(3):  
    for j in np.arange(3):
        for k in np.arange(3):
            n.append(i+1)
            n.append(j+1)
            n.append(k+1)
            m = np.random.randint(3000,5000)
            n.append(m)
            s.append(m)
            if i == 0:
                n11.append(m)
            elif i == 1:
                n12.append(m)
            else:
                n13.append(m)
            if j == 0:
                n21.append(m)
            elif j == 1:
                n22.append(m)
            else:
                n23.append(m)
            if k == 0:
                n31.append(m)
            elif k == 1:
                n32.append(m)
            else:
                n33.append(m)
np.reshape(np.array(n),(27,4))
print(n)
print(np.sum(n11))
print(np.sum(n12))
print(np.sum(n13))
print(np.sum(n21))
print(np.sum(n22))
print(np.sum(n23))
print(np.sum(n31))
print(np.sum(n32))
print(np.sum(n33))
print(np.sum(s))


x = np.random.normal(40,5,9)
print(x)
print(x[0]+x[1]+x[2])
print(x[3]+x[4]+x[5])
print(x[6]+x[7]+x[8])
print(x[0]+x[3]+x[6])
print(x[1]+x[4]+x[7])
print(x[2]+x[5]+x[8])
print(x[0]+x[5]+x[7])
print(x[1]+x[3]+x[8])
print(x[2]+x[4]+x[6])
print(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8])

line = Line("正交实验")
attr = ['一', '二', '三']
v1=[x[0]+x[1]+x[2],x[3]+x[4]+x[5],x[6]+x[7]+x[8]]
v2=[x[0]+x[3]+x[6],x[1]+x[4]+x[7],x[2]+x[5]+x[8]]
v3=[x[0]+x[5]+x[7],x[1]+x[3]+x[8],x[2]+x[4]+x[6]]
line.add("A",attr,v1)
line.add("B",attr,v2)
line.add("C",attr,v3,yaxis_min=95,yaxis_max=130)
line.render(r"C:\Users\Administrator\Desktop\分析图.html")