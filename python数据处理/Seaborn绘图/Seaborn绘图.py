import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style="ticks")
np.random.seed(sum(map(ord, "axis_grids")))
tips = sns.load_dataset("tips")
print(tips)  # 用此方法输出
tips.head()  # 这部分没有输出，和jupyter有区别
g = sns.FacetGrid(tips, col="time")
g.map(plt.hist, "tip")
plt.show()  # 这里也和jupyter上面运行代码不一样