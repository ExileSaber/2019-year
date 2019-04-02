import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

plt.plot([0, 1], [0, 1], sns.xkcd_rgb["pale red"], lw=3)  # 画经过两点的直线，后面为设置颜色和线宽
plt.plot([0, 1], [0, 2], sns.xkcd_rgb["medium green"], lw=3)
plt.plot([0, 1], [0, 3], sns.xkcd_rgb["denim blue"], lw=3)
plt.show()