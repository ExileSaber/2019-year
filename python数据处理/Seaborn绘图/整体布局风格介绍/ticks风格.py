import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)  #在0到14的区间上平均分100个点
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)  #描点
    plt.show()

sns.set_style('ticks')
sinplot()
