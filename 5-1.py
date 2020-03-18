import numpy as np
a = int(input("请输入一个1-100之间的整数："))
print("序号\t  索引值\t  随机数\t")
for i in range(0,20):
 print ("%s\t    %s\t    %s\t" %(i + 1,0 + i * a,np.random.rand()))