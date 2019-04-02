import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)  # 设置柱形图之间分隔线
np.random.seed(sum(map(ord, "distributions")))  # 设置随机种子
x = np.random.normal(size=100)

# 图一
sns.distplot(x, kde=False)
plt.show()

# 图二
sns.distplot(x, bins=20,  kde=False)  # 指定bins大小，即将数据分成多少份
plt.show()