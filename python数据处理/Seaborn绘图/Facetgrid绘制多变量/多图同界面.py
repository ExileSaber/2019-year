import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")
tips = sns.load_dataset("tips")

with sns.axes_style("white"):
    g = sns.FacetGrid(tips, row="sex", col="smoker", margin_titles=True, height=2.5)  # margin边缘，将第一个分类标准的注释单独表在右边
g.map(plt.scatter, "total_bill", "tip", color="#334488", edgecolor="white", lw=.5)
g.set_axis_labels("Total bill (US Dollars)", "Tip")  # 设置横纵坐标名称
g.set(xticks=[10, 30, 50], yticks=[2, 6, 10])  # 设置横纵坐标值
g.fig.subplots_adjust(wspace=.02, hspace=.02)  # 调整子图
# g.fig.subplots_adjust(left  = 0.125,right = 0.5,bottom = 0.1,top = 0.9, wspace=.02, hspace=.02)
plt.show()