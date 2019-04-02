

import matplotlib.pyplot as plt
import seaborn as sns

def draw_histogram_plot_4(number_1, number_2, The_method, mean_number_1, mean_number_2):
    fig = plt.figure(figsize=(25, 15))  # 设置画图区域大小
    sns.set(color_codes=True)  # 设置柱形图之间分隔线
    sns.axes_style("white")
    ax = []

    ax.append(fig.add_subplot(2, 5, 1))
    ax.append(fig.add_subplot(2, 5, 2))
    ax.append(fig.add_subplot(2, 5, 3))
    ax.append(fig.add_subplot(2, 5, 4))
    ax.append(fig.add_subplot(2, 5, 5))
    ax.append(fig.add_subplot(2, 5, 6))
    ax.append(fig.add_subplot(2, 5, 7))
    ax.append(fig.add_subplot(2, 5, 8))
    ax.append(fig.add_subplot(2, 5, 9))
    ax.append(fig.add_subplot(2, 5, 10))


# 数据1的图
    for i in range(0, 5):
        sns.distplot(number_1[i], bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_1[i]), hist=True,
                     ax=ax[i])
        ax[i].set_title(The_method[i])


# 数据2的图
    for i in range(0, 5):
        sns.distplot(number_2[i], bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_2[i]), hist=True, ax=ax[i+5])

    # plt.show()