import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("lena.tiff") #读取图片

plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False
img_r,img_g,img_b = img.split() #分离图片通道
plt.figure(figsize = (8,8))#创建画布


#r通道缩小
plt.subplot(2,2,1)
img_small = img_r.resize((50,50))
plt.title("R-缩放",fontsize=14)
plt.axis("off")
plt.imshow(img_small,cmap="gray")

#g通道水平旋转
plt.subplot(2,2,2)
img_flr = img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_r270 = img_flr.transpose(Image.ROTATE_270)
plt.title("G-镜像+旋转",fontsize=14)
plt.imshow(img_r270,cmap="gray")

#B通道裁剪
plt.subplot(2,2,3)
img_region = img_b.crop((0,0,150,150))
plt.title("B-裁剪",fontsize=14)
plt.imshow(img_region,cmap="gray")

#RGB合并
plt.subplot(2,2,4)
img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
plt.title("RGB",fontsize = 14)
plt.imshow(img_rgb,cmap="gray")

#保存图片
img_rgb.save("test.png")


plt.suptitle("图像基本操作",fontsize=20,color="blue")
plt.show()