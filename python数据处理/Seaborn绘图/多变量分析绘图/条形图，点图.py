import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

titanic = sns.load_dataset("titanic")

# 显示集中趋势可以使用条形图
sns.barplot(x="sex", y="survived", hue="class", data=titanic)
plt.show()

# 点图更好的描述变化差异
sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
plt.show()

# 多个参数
sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
              palette={"male": "g", "female": "m"},
              markers=["^", "o"], linestyles=["-", "--"])
plt.show()