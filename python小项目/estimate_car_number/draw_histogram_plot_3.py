
import matplotlib.pyplot as plt
import seaborn as sns

def draw_histogram_plot_3(number_1_1, number_1_2, number_1_3, number_1_4, number_1_5, number_2_1, number_2_2, number_2_3, number_2_4, number_2_5,
                          the_method_1, the_method_2, the_method_3, the_method_4, the_method_5,
                          mean_number_1_1, mean_number_1_2, mean_number_1_3, mean_number_1_4, mean_number_1_5,
                          mean_number_2_1, mean_number_2_2, mean_number_2_3, mean_number_2_4, mean_number_2_5):
    fig = plt.figure(figsize=(25, 15))  # 设置画图区域大小
    sns.set(color_codes=True)  # 设置柱形图之间分隔线
    sns.axes_style("white")

    ax1 = fig.add_subplot(2, 5, 1)
    ax2 = fig.add_subplot(2, 5, 2)
    ax3 = fig.add_subplot(2, 5, 3)
    ax4 = fig.add_subplot(2, 5, 4)
    ax5 = fig.add_subplot(2, 5, 5)
    ax6 = fig.add_subplot(2, 5, 6)
    ax7 = fig.add_subplot(2, 5, 7)
    ax8 = fig.add_subplot(2, 5, 8)
    ax9 = fig.add_subplot(2, 5, 9)
    ax10 = fig.add_subplot(2, 5, 10)

# 数据1的图
    sns.distplot(number_1_1, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_1_1), hist=True, ax=ax1)
    ax1.set_title(the_method_1)

    sns.distplot(number_1_2, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_1_2), hist=True, ax=ax2)
    ax2.set_title(the_method_2)

    sns.distplot(number_1_3, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_1_3), hist=True, ax=ax3)
    ax3.set_title(the_method_3)

    sns.distplot(number_1_4, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_1_4), hist=True, ax=ax4)
    ax4.set_title(the_method_4)

    sns.distplot(number_1_5, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_1_5), hist=True, ax=ax5)
    ax5.set_title(the_method_5)


# 数据2的图
    sns.distplot(number_2_1, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_2_1), hist=True, ax=ax6)

    sns.distplot(number_2_2, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_2_2), hist=True, ax=ax7)

    sns.distplot(number_2_3, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_2_3), hist=True, ax=ax8)

    sns.distplot(number_2_4, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_2_4), hist=True, ax=ax9)

    sns.distplot(number_2_5, bins=20, kde=True, rug=True, axlabel="average:{}".format(mean_number_2_5), hist=True, ax=ax10)

    plt.show()