import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize": (6, 6)})  # 设置面板的长宽

sns.palplot(sns.color_palette("Paired", 8))  # Paired为一种两两配对的颜色板
plt.show()