import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)  # 设置柱形图之间分隔线
iris = sns.load_dataset("iris")  # 导入seaborn内置的数据集
sns.pairplot(iris)  # 绘制多变量两两分析图
plt.show()