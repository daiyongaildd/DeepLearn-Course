# (1) 下载波士顿数据集，读取全部506条数据，放在NumPy数组x、y中（x：属性，y：标记）。(5分)

# (2) 使用全部506条数据，实现波士顿房价数据集可视化，如图1所示。(10分)

# (3) 要求用户选择属性，如图2所示，根据用户的选择，输出对应属性的散点图，如图3所示。(5分)
import matplotlib.pyplot as plt 
import numpy as np
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x , train_y),(_,_) = boston_housing.load_data(test_split = 0)

plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

title = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B-1000', 'LSTAT', 'MEDV']
plt.figure(figsize=(11,11))
for i in range(13):
    plt.subplot(4,4,(i + 1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(title[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i+1) + "." +title[i] + " - Price" )

plt.tight_layout(rect=[0,0,1,0.95])
plt.suptitle("各个属性与房价的关系", x = 0.5, y = 1, fontsize = 20)
plt.show()
print(" 1 -- CRIM \n 2 -- ZN \n 3 -- INDUS \n 4 -- CHAS \n 5 -- NOX \n 6 -- RM \n 7 -- AGE \n 8 -- DIS \n 9 -- RAD \n 10 -- TAX \n 11 -- PTRATIO \n 12 -- B-1000 \n 13 -- LSTAT \n 14 -- MEDV")
x = int(input("请选择属性:"))
plt.subplot()
plt.scatter(train_x[:,x - 1],train_y)
plt.xlabel(title[x - 1])
plt.ylabel("Pricr($1000's)")
plt.title(str(x) + "." + title[x - 1] + " - Price")
plt.show()