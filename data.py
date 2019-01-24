# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:19:25 2019

@author: Mickie(Ziyi) Xu
"""

from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import pandas as pd
import time
import thread
import statsmodels.api as sm

def __init__(self, data1, data2, x, anormaly, result):
    self.data1=data1
    self.data2=data2
    self.x = x
    self.anormaly = anormaly
    self.result = result

def get_cpu_data(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    result = client.query("select LAST(usage_user) from cpu where cpu = 'cpu-total';")
    return result

def get_cpu_datas(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    self.result = client.query("select LAST(usage_user) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    return self.result

def get_cpu_MEAN(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    self.result = client.query("select MEAN(usage_user) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    return self.result

def get_cpu_VAR(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    self.result = client.query("select STDDEV(usage_user) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    return self.result^2

def get_cpu_IQR(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    result1 = client.query("select PERCENTILE(usage_user, 75) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    result2 = client.query("select PERCENTILE(usage_user, 25) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    self.result = (result1 - result2) * 1.5
    return self.result

def get_cpu_RANGE(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    result1 = client.query("select MAX(usage_user) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    result2 = client.query("select MIN(usage_user) from cpu where cpu = 'cpu-total' and time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    self.result = result1 - result2
    return self.result

def get_mem_datas(self):
    client = InfluxDBClient(host='172.16.248.177', port=8086, username='root', database='telegraf')
    self.result = client.query("select LAST(used_percent) from mem where time >= '%s' AND time <= '%s' GROUP BY time(10s),* fill(10) LIMIT 360 SLIMIT 1;" %(self.data1, self.data2))
    return self.result

def update_cpu_data(self):
    data_cpu = get_cpu_data()
    try:
    self.result
    except NameError:
        self.result = []
        self.result.append(data_cpu)
    else:
        self.result.append(data_cpu)
    return self.result

def updata_cpu_datas():
    data1 = input("input start time(example:2018-12-22T14:40:00Z):")
    data2 = input("input end time(example:2018-12-22T14:40:30Z):")
    data_cpu = get_datas(data1, data2)
    return data_cpu

def ARIMA_cpu_models(p, d, q, t):
    data = updata_cpu()
    new_data = data.diff(d)
    model = sm.tsa.ARMA(new_data,(p,q)).fit()
    predict_data = model.predict(t)

'''
cpu_ARIMA(1, 1, 1, 6)
'''

def IQR_cpu_model():
    range = get_cpu_RANGE()
    iqr = get_cpu_IQR()
    if iqr >= range:
        self.anormaly.append('anormaly')
    else:
        self.anormaly.append('normal')

def anormal_cpu_model(self, threadname, x = 50, y = 80):
    mean = get_cpu_MEAN()
    var = get_cpu_VAR()
    if mean >= x:
        self.anormaly.append('red')
        print('red error')
    elif var >= y:
        self.anormaly.append('yellow')
        print('yellow error')
    else:
        self.anormaly.append('green')

def run_cpu_model(self, threadname):
    y = 1
    while y < 10:
        time.sleep(self.x)
        time = time.ctime()
        data = data_update()
        print(threadname,':', time,',', data[-1])

def predict_cpu_data(self, threadname):
    y = 1
    while y < 10:
        time.sleep(self.x)
        time = time.ctime()
        data = data_update()
        new_data = data[-60:].diff(1)
        model = sm.tsa.ARMA(new_data,(1,1)).fit()
        predict_data = model.predict(6)
        print(threadname,':', time,',', predict_data)

'''
try:
   thread.start_new_thread(run_data, "Thread-1")
   thread.start_new_thread(predict_data, "Thread-2")
except:
   print("Error: oh my god, we are dead!")

while 1:
    pass
'''
