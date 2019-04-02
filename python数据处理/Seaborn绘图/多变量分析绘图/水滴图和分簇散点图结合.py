import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
tips = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill", data=tips, inner=None)  # 水滴图（inner设置图中没有其他要素，将原来水滴图中的东西去掉）
sns.swarmplot(x="day", y="total_bill", data=tips, color="w", alpha=.5)  # 分簇散点图（alpha设置透明度）
plt.show()
