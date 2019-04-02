import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# 盒图
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)  # 数据根据time分类
plt.show()

sns.boxplot(data=iris, orient="h")  # orient指定为h，横着画图
plt.show()


# 水滴图
sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
plt.show()

# 水滴图（数据根据sex分类，绘图将水滴图按轴线分为两部分，两种数据各用一半）
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
plt.show()