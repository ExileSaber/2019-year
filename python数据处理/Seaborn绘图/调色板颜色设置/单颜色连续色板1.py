import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

sns.palplot(sns.color_palette("Blues"))  # 由浅到深
sns.palplot(sns.color_palette("Blues_r"))  # 由深到浅
plt.show()