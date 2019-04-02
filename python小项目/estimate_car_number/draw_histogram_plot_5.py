# 比较图
import matplotlib.pyplot as plt
import seaborn as sns

def draw_histogram_plot_5(number_1,
                          number_2,
                          The_method,
                          mean_number_1,
                          mean_number_2):
    fig = plt.figure(figsize=(25, 5))  # 设置画图区域大小
    sns.set(color_codes=True)  # 设置柱形图之间分隔线
    sns.axes_style("white")
    ax = []

    ax.append(fig.add_subplot(1, 5, 1))
    ax.append(fig.add_subplot(1, 5, 2))
    ax.append(fig.add_subplot(1, 5, 3))
    ax.append(fig.add_subplot(1, 5, 4))
    ax.append(fig.add_subplot(1, 5, 5))
    ax.append(fig.add_subplot(1, 5, 1))
    ax.append(fig.add_subplot(1, 5, 2))
    ax.append(fig.add_subplot(1, 5, 3))
    ax.append(fig.add_subplot(1, 5, 4))
    ax.append(fig.add_subplot(1, 5, 5))

# 数据1的图
    for i in range(0, 5):
        sns.distplot(number_1[i], bins=20, kde=True, rug=False, hist=False, ax=ax[i])
        ax[i].set_title(The_method[i])


# 数据2的图
    for i in range(0, 5):
        sns.distplot(number_2[i], bins=20, kde=True, rug=False, hist=False, ax=ax[i+5])

    # plt.show()