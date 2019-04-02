import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)  #在0到14的区间上平均分100个点
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)  #描点
    plt.show()

sns.set_style("darkgrid")

sns.set_context("paper")  # 画图格子大小设置，还有talk（中），poster（大）
plt.figure(figsize=(8, 6))
sinplot()

sns.set_context("talk")  # 画图格子大小设置，还有talk，poster
plt.figure(figsize=(8, 6))
sinplot()

sns.set_context("poster")  # 画图格子大小设置，还有talk，poster
plt.figure(figsize=(8, 6))
sinplot()

sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})  # font_scale是坐标值的字体九大小，lines.linewidth指定图像的粗细
sinplot()