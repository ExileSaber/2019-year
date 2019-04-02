import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time")  # 实例化绘图的区域,第一个参数是传入的数据，后面的数据是分类标准，以time为标准分为两类
g.map(plt.hist, "tip")  # 第一个变量设置的是画图类型，第二个是横坐标名称
plt.show()

f = sns.FacetGrid(tips, col="sex", hue="smoker")  # 以sex， 和smoker为标准分为四类
f.map(plt.scatter, "total_bill", "tip", alpha=.7)  # 第二个是横坐标名称，第三个是纵坐标名称
f.add_legend()  # 将绘图说明表示出
plt.show()

g_1 = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)  # margin边缘，将第一个分类标准的注释单独表在右边
g_1.map(sns.regplot, "size", "total_bill", color=".3", fit_reg=False, x_jitter=.1)
# color参数越小越深， fit_reg设置是否绘制回归曲线，x_jitter设置浮动
plt.show()

g_2 = sns.FacetGrid(tips, col="day", size=4, aspect=.5)  # aspect设置长宽比
g_2.map(sns.barplot, "sex", "total_bill")
plt.show()