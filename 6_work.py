import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(11,11))

x_data = np.linspace(1,100,500)
y_data = 3.1234 * x_data + 2.98 + np.random.randn(x_data.shape) * 0.4

plt.scatter(x_data,y_data)
plt.plot(x_data,3.1234 * x_data + 2.98,color = 'red',linewidth = 3)

plt.show()