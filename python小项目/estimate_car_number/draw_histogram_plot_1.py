
import matplotlib.pyplot as plt
import seaborn as sns

def draw_histogram_plot_1(number, the_method):
    fig, ax = plt.subplots()
    sns.set(color_codes=True)  # 设置柱形图之间分隔线
    sns.axes_style("white")
    sns.distplot(number, bins=20, kde=True, rug=True, axlabel="estimate_car_number", hist=True)
    ax.set_title(the_method)
    plt.show()