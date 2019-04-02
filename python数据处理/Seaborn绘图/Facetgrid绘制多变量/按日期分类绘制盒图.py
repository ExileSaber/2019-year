import seaborn as sns
from pandas import Categorical
import matplotlib.pyplot as plt

sns.set(style="ticks")
tips = sns.load_dataset("tips")

ordered_days = tips.day.value_counts().index
print(ordered_days)
ordered_days = Categorical(['Thur', 'Fri', 'Sat', 'Sun'])
g = sns.FacetGrid(tips, row="day", row_order=ordered_days, height=1.7, aspect=4)
# row设置绘图的分类标准，并注释，row_order参数传入分类数据
g.map(sns.boxplot, "total_bill")  # 设置绘图类型和横坐标
plt.show()