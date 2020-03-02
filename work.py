# 利用 Python 完成一元二次方程 2 0 ax bx c    的求解，要求程序输入任意,, abc的值后，程序能判断输出有解或无解，有解的话，输出x的解为多少。
import math
a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
c = int(input("请输入c的值："))
s = 0
x1 = 0
x2 = 0
if a == 0 :
    print("a不能为0，无解")
else :
    s = b*b - 4*a*c
    if s < 0 :
        print("无解")
    else :
        x1 = (-b + math.sqrt(s)) / 2*a
        x2 = (-b - math.sqrt(s)) / 2*a
        print("两个解分别是：x1:%d,x2:%d" %(x1,x2))