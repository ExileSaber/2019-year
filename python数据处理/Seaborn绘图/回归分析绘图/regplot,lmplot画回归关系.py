import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(color_codes=True)  # 设置数据之间分隔线
np.random.seed(sum(map(ord, "regression")))  # 设置随机种子
tips = sns.load_dataset("tips")  # 导入内置数据tips

# 用regplot画图，参数约束少
sns.regplot(x="total_bill", y="tip", data=tips)  # 其中x和y为其横坐标和纵坐标的取值
plt.show()

# 用lmplot画图
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()