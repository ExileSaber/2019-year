import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)  # 设置柱形图之间分隔线
mean, cov = [0, 1], [(1, .5), (.5, 1)]  # 设置平均值和协方差
data = np.random.multivariate_normal(mean, cov, size=200)
df = pd.DataFrame(data, columns=["x", "y"])  # 转化为dataframe格式

# 图一（散点图）
sns.jointplot(x="x", y="y", data=df)  # kind参数默认为散点图，kind : { “scatter” | “reg” | “resid” | “kde” | “hex” }, optional Kind of plot to draw.
plt.show()

# 图二（蜂巢图）
x, y = np.random.multivariate_normal(mean, cov, size=1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k")
    plt.show()

