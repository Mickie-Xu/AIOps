import pandas as pd
import numpy as np
#import math
#from scipy import stats
import matplotlib.pyplot as plt
#import random
#import sys
#from sklearn.ensemble import IsolationForest as IF
import data

'''
def calc_distance(p1, p2):
    if len(p1) != len(p2): raise IndexError('Training and testing datasets are of different dimensions.')
    else:
        sum = 0
        for i in range(len(p1)):
            sum += (p1[i] - p2[i]) **2
        return sum ** 0.5
'''

def normalize(dataset):
    new_set = [a for a in dataset]
    minValue = min(dataset)
    maxValue = max(dataset)
    #mean = np.average(dataset)
    #sigma = np.std(dataset)
    for i in range(len(dataset)):
        new_set[i] = (new_set[i] - minValue)/(maxValue - minValue)
        #dataset[i] = (dataset[i] - mean) / sigma
    return new_set

#num = float(input("How many times of IQR: "))
def IQR_classify(data, num=1.5):
    data2 = sorted(data)
    q1 = int(0.25 * len(data2))
    q3 = int(0.75 * len(data2))
    IQR = data2[q3] - data2[q1]
    #return test < data[q1] - 1.5 * IQR or test > data[q3] + 1.5 * IQR
    a = [(i, item) for i, item in enumerate(data,1) if item > num*IQR + data2[q3] or item < data2[q1] - num*IQR]
    #print(a)
    return a #if a < data[q1 - 1.5*IQR] or a > data[q3] + 1.5*IQR]
    #return IQR
'''
def classify(test, data, labels, k=5):
    distance_list = []
    for i in range(len(data)):
        distance_list.append((calc_distance(test, data[i]), labels[i]))
    sort = sorted(distance_list)
    count0 = 0
    count1 = 0
    for i in range(k):
        if sort[i][1] == 0:
            count0 += 1
        else:
            count1 += 1
    #print("0:{0}, 1:{1}".format(count0, count1))
    if count0 > count1: return False 
    else: return True
 

'''
#Change File Directory
#f = open(r'C:\Users\Administrator\Desktop\data\CPU_Data.txt')
f = open(r'C:\Users\Administrator\Desktop\data\demo.txt')
data = f.read().split('\n')

data = np.array(list(map(float, data)))
f.close()

print(len(data))

#plt.plot(np.arange(1837), data)
plt.plot(np.arange(204), data)
plt.show()

k = int(input("time "))#int(input("Determine the size of the box: "))
#IQR_range = int(input("Acceptable Range of IQR: "))

def calc_stats(data):
    return np.mean(data), np.var(data)

def anomalies_by_range(data, size=k):
    df = pd.DataFrame(columns=["Minute", "Average", "Variance"], index=None)
    i = 0
    index = 0
    while i < len(data):
        for j in range(size):
            try:
                a, b = calc_stats(data[i:i+size])
                df.loc[index] = [index,a,b]
            except IndexError:
                a, b = calc_stats(data[i:len(data)])
                df.loc[index] = [index,a,b]
        i += size
        index+=1
    df['Avg_norm'] = normalize(df['Average'])
    df['Var_norm'] = normalize(df['Variance'])
    return find(df), df

def find(data):
    anomalies = []
    for index, row in data.iterrows():
        #time = row["Minute"]
        if row['Average'] > 15:
            anomalies.append([index, 2])
        elif row["Variance"] > 3:
            anomalies.append([index, 1])
        else:
            anomalies.append([index, 0])
    return anomalies

processed_range, data_df = anomalies_by_range(data)

def find1(data, size):#, range):
    index = []
    anomalies = []
    i = 0
    while i + size < len(data):
        if np.var(np.array(data[i:i+size])) < 20:
            i+=1
        elif len(IQR_classify(data[i:i+size], num)) > 0:
            #print("Anomaly: {0} to {1}".format(i, i+size))
            #x = max(data[i:i+size])
            #print(x)
            for a in IQR_classify(data[i:i+size], num):
                index.append(a[0] + i)
                anomalies.append(a[1])
            i += size
            
        else:
            i+=1
    #print(index, anomalies)
    return index, anomalies


print(find1(data, k))

x2, y2 = find1(data,k)


norm = np.array([list(range(a[0]*k, a[0]*k + k)) for a in processed_range if a[1] == 0]).flatten()
lv1 = np.array([list(range(a[0]*k, a[0]*k + k)) for a in processed_range if a[1] == 1]).flatten()
lv2 = np.array([list(range(a[0]*k, a[0]*k + k)) for a in processed_range if a[1] == 2]).flatten()

norm = [a for a in norm if a < len(data)]
lv1 = [a for a in lv1 if a < len(data)]
lv2 = [a for a in lv2 if a < len(data)]
x = np.array([a for a in range(1, len(data) + 1)])
y_norm = []
y_lv1 = []
y_lv2 = []
for index, y in enumerate(data):
    if index in norm:
        #print(index)
        y_norm.append(y)
    elif index in lv1:
        y_lv1.append(y)
    elif index in lv2:
        y_lv2.append(y)
    else:
        print(index)
        raise IndexError
    #print(index)

print(data_df)

y = data
#x2, y2 = find2(data,find1(data, k, IQR_range))
plt.subplot(211)
plt.plot(data_df['Minute'], data_df['Avg_norm'], c="red")
plt.plot(data_df['Minute'], data_df['Var_norm'], c="green")

plt.subplot(212)
#plt.scatter(x, y)

plt.scatter(norm, y_norm, c="green")
plt.scatter(lv1, y_lv1, c="yellow")
plt.scatter(lv2, y_lv2, c="red")
plt.scatter(x2, y2, c='red')

plt.show()

# print(data_df['Avg_norm'],data_df['Var_norm'])