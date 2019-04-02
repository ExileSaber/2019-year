import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6)/2
sns.boxplot(data=data)
plt.show()
