import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

sns.palplot(sns.color_palette("cubehelix", 8))  # 线性变化方法1
sns.palplot(sns.cubehelix_palette(8, start=.5, rot=-.75))  # 线性变化方法2（设置区间）
plt.show()