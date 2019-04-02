import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})

current_palette = sns.color_palette()  # 默认颜色
sns.palplot(current_palette)  # 画出设置的颜色
plt.show()