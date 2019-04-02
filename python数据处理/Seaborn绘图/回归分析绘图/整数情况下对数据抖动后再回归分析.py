import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)  # 设置数据之间分隔线
np.random.seed(sum(map(ord, "regression")))  # 设置随机种子
tips = sns.load_dataset("tips")  # 导入内置数据tips

# 没有数据抖动的情况下的回归绘图
sns.regplot(x="size", y="tip", data=tips)
plt.show()

# 数据抖动后的回归绘图
sns.regplot(x="size", y="tip", data=tips, x_jitter=.05)
plt.show()