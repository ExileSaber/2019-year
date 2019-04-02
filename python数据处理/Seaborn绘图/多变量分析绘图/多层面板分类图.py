import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)
tips = sns.load_dataset("tips")
print(tips)

sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips)
plt.show()

# bar条形图
sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips, kind="bar")  # kind设置画图类型
plt.show()

# swarm分簇图
sns.factorplot(x="day", y="total_bill", hue="smoker", col="time", data=tips, kind="swarm")
plt.show()


sns.factorplot(x="time", y="total_bill", hue="smoker", col="day", data=tips, kind="box", size=4, aspect=.5)
plt.show()

'''
Parameters：
x,y,hue 数据集变量 变量名
date 数据集 数据集名
row,col 更多分类变量进行平铺显示 变量名
col_wrap 每行的最高平铺数 整数
estimator 在每个分类中进行矢量到标量的映射 矢量
ci 置信区间 浮点数或None
n_boot 计算置信区间时使用的引导迭代次数 整数
units 采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据
order, hue_order 对应排序列表 字符串列表
row_order, col_order 对应排序列表 字符串列表
kind : 可选：point 默认, bar 柱形图, count 频次, box 箱体, violin 提琴, strip 散点，swarm 分散点 
       size 每个面的高度（英寸） 标量 aspect 纵横比 标量 orient 方向 "v"/"h" color 颜色 matplotlib颜色
        palette 调色板 seaborn颜色色板或字典 legend hue的信息面板 True/False legend_out 是否扩展图形，并将信息框绘制在中心右边 True/False share{x,y} 共享轴线 True/False
'''