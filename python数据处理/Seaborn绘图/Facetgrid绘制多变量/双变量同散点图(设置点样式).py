import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")
tips = sns.load_dataset("tips")

g = sns.FacetGrid(tips, hue="sex", palette="Set1", height=5, hue_kws={"marker": ["^", "v"]})
# palette参数传入颜色，传入数据为字典类型，库自带一些颜色设置。hue_kws设置点的样式，传入字典类型数据，字典key为"market"，value为列表类型，列表中元素指定画图点样式
g.map(plt.scatter, "total_bill", "tip", s=100, linewidth=.5, edgecolor="white")
g.add_legend()
plt.show()