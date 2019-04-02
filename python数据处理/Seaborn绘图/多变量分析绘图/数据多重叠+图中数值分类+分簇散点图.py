import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
tips = sns.load_dataset("tips")

# 散点重合严重
sns.stripplot(x="day", y="total_bill", data=tips, jitter=False)  # jitter默认为True
plt.show()

# 数据抖动后
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
plt.show()

# 根据day数据分类画图（没有分开）
sns.stripplot(x="sex", y="total_bill", data=tips, hue="day", jitter=True)
plt.show()

# 根据day数据分类画图（有分开）
sns.stripplot(x="sex", y="total_bill", data=tips, hue="day", jitter=True, dodge=True)
plt.show()

# 分簇散点图
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()

# 分簇散点图（换个方向，根据time数据分类）
sns.swarmplot(x="total_bill", y="day", hue="time", data=tips)
plt.show()

# 分簇散点图（添加划分参数）
sns.swaimplot(x="day", y="total_bill", hue="sex", data=tips)
plt.show()

# 其他参数见  https://blog.csdn.net/qq_42554007/article/details/82625702
