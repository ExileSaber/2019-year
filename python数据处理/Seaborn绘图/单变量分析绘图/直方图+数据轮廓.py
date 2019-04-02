import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)  # 设置柱形图之间分隔线
sns.axes_style("white")
x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)  # fit为当前统计指标
plt.show()