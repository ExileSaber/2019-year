import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

sns.palplot(sns.hls_palette(8, l=.5, s=.9))  # l越大越亮，s越大越饱和
plt.show()