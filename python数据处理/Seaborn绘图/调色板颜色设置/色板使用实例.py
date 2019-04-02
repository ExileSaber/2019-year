import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

x, y = np.random.multivariate_normal([0, 0], [[1, -.5], [-.5, 1]], size=300).T  # 根据均值协方差得到数据
pal = sns.dark_palette("green", as_cmap=True)
sns.kdeplot(x, y, cmap=pal, shade=True)  # camp参数为导入颜色，shade参数设置是否填充
plt.show()