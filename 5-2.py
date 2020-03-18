import numpy as np
x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x.reshape(-1)
y.reshape(-1)
s = x.size
avg1 = np.sum(x) / s
avg2 = np.sum(y) / s
a = 0
b = 0
for i in range(0,s):
    a += (x[i] - avg1) * (y[i] - avg2)
    b += (x[i] - avg1) ** 2
w = a / b
b = avg2 - w * avg1
print("w = %s" %(w))
print("b = %s" %(b))