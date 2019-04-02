import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})

sns.palplot(sns.color_palette("hls", 8))  # 将hls颜色空间分成8份,指定为8个颜色
plt.show()