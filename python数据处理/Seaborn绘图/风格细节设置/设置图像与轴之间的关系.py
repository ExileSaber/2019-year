import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(size=(20, 6)) + np.arange(6)/2
sns.violinplot(data)
sns.despine(offset=10)  # despine方法用来调整图像位置，到x轴距离
plt.show()

sns.set_style('whitegrid')
sns.boxplot(data=data, palette='deep')
sns.despine(left=True)  # 去掉左侧轴
plt.show()