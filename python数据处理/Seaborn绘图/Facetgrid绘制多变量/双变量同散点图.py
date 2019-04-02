import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")
tips = sns.load_dataset("tips")

pal = dict(Lunch="blue", Dinner="gray")
g = sns.FacetGrid(tips, hue="time", palette=pal, height=5)  # palette参数传入颜色，传入数据为字典类型
g.map(plt.scatter, "total_bill", "tip", s=30, alpha=.7, linewidth=.5, edgecolor="white")  # s设置散点的大小
g.add_legend()
plt.show()