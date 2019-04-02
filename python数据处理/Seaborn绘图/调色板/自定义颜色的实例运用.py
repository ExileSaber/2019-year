import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

data = np.random.normal(size=(20, 8)) + np.arange(8)/2
sns.boxplot(data=data, palette=sns.color_palette("hls", 8))
plt.show()