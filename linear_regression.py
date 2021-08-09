
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
from math import *
# sample data
eps = 0.000001
x = range(1, 15+1)
y = [10.00, 16.30, 23, 27, 31, 35.60, 39, 41.50,
     41.90, 45.00, 46.00, 45.50, 46.00, 49, 50.00]
x2 = [val**2 for val in x]
x3 = [val*val*val for val in x]
x4 = [val*val*val*val for val in x]
xy = [x[a]*y[a] for a in range(len(x))]
x2y = [x2[a]*y[a] for a in range(len(x2))]

n = len(x)
# linear regression
sumx = 0.0
sumy = 0.0
sumxx = 0.0
sumxy = 0.0
xmean = 0.0
ymean = 0.0
denom = 0.0

for val in range(n):
    sumx += x[val]
    sumy += y[val]
    sumxx += x2[val]
    sumxy += xy[val]
xmean = sumx/n
ymean = sumy/n
denom = n*sumxx-sumx*sumx

if abs(denom) > eps:
    b = (n*sumxy-sumx*sumy)/denom
    a = ymean-b*xmean
    print('the regression line y=a+bx'.title())
    print('the coefficients'.title())
    print(a, b)
else:
    print('no solution'.title())

line = [b*i+a for i in x]
plt.title('linear regression'.title())
plt.xlabel('x coordinates'.title())
plt.ylabel('y coordinates'.title())
plt.scatter(x, y, marker='o', c='b')
plt.grid(True)
plt.plot(x, line, '--')
plt.show()
