import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

sns.palplot(sns.light_palette("green"))  # 由浅到深
sns.palplot(sns.dark_palette("purple"))  # 由深到浅
sns.palplot(sns.light_palette("navy", reverse=True))  # 由深到浅
plt.show()