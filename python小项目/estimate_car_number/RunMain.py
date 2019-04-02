# 运行接口
import get_random_number
import matplotlib.pyplot as plt
import method_1
import method_2
import method_3
import method_4
import method_5
import calculate_average_value
import draw_histogram_plot_1
import draw_histogram_plot_2
import draw_histogram_plot_3
import draw_histogram_plot_4
import draw_histogram_plot_5
import put_average_car_number
import calculate_standard_deviation

test_number = 200
max_car_number = 1000
test_car_number = 10

The_method_1 = "Mean model"
The_method_2 = "Median model"
The_method_3 = "Symmetric model of two ends interval"
The_method_4 = "Average interval model"
The_method_5 = "Interval equalization Model"


def run_view():
    sample_collection_1 = get_random_number.get_random_number(max_car_number, test_car_number, test_number)
    sample_collection_2 = get_random_number.get_random_number(max_car_number, test_car_number, test_number)


# 数据处理方法一
    '''
    # 数据1
    number_1_1 = method_1.method_1(test_number, sample_collection_1)
    number_1_2 = method_2.method_2(test_number, sample_collection_1)
    number_1_3 = method_3.method_3(test_number, sample_collection_1)
    number_1_4 = method_4.method_4(test_number, sample_collection_1)
    number_1_5 = method_5.method_5(test_number, sample_collection_1)

    mean_number_1_1 = calculate_average_value.calculate_average_value(number_1_1)
    mean_number_1_2 = calculate_average_value.calculate_average_value(number_1_2)
    mean_number_1_3 = calculate_average_value.calculate_average_value(number_1_3)
    mean_number_1_4 = calculate_average_value.calculate_average_value(number_1_4)
    mean_number_1_5 = calculate_average_value.calculate_average_value(number_1_5)

    the_method_1_1 = The_method_1 + " (average = {})".format(mean_number_1_1)
    the_method_1_2 = The_method_1 + " (average = {})".format(mean_number_1_2)
    the_method_1_3 = The_method_1 + " (average = {})".f ormat(mean_number_1_3)
    the_method_1_4 = The_method_1 + " (average = {})".format(mean_number_1_4)
    the_method_1_5 = The_method_1 + " (average = {})".format(mean_number_1_5)

    # 数据2
    number_2_1 = method_1.method_1(test_number, sample_collection_2)
    number_2_2 = method_2.method_2(test_number, sample_collection_2)
    number_2_3 = method_3.method_3(test_number, sample_collection_2)
    number_2_4 = method_4.method_4(test_number, sample_collection_2)
    number_2_5 = method_5.method_5(test_number, sample_collection_2)

    mean_number_2_1 = calculate_average_value.calculate_average_value(number_2_1)
    mean_number_2_2 = calculate_average_value.calculate_average_value(number_2_2)
    mean_number_2_3 = calculate_average_value.calculate_average_value(number_2_3)
    mean_number_2_4 = calculate_average_value.calculate_average_value(number_2_4)
    mean_number_2_5 = calculate_average_value.calculate_average_value(number_2_5)

    the_method_2_1 = The_method_1 + " (average = {})".format(mean_number_2_1)
    the_method_2_2 = The_method_1 + " (average = {})".format(mean_number_2_2)
    the_method_2_3 = The_method_1 + " (average = {})".format(mean_number_2_3)
    the_method_2_4 = The_method_1 + " (average = {})".format(mean_number_2_4)
    the_method_2_5 = The_method_1 + " (average = {})".format(mean_number_2_5)
    '''


# 单个绘图
    '''
    # 数据1
    draw_histogram_plot_1.draw_histogram_plot_1(number_1_1, the_method_1_1)
    draw_histogram_plot_1.draw_histogram_plot_1(number_1_2, the_method_1_2)
    draw_histogram_plot_1.draw_histogram_plot_1(number_1_3, the_method_1_3)
    draw_histogram_plot_1.draw_histogram_plot_1(number_1_4, the_method_1_4)
    draw_histogram_plot_1.draw_histogram_plot_1(number_1_5, the_method_1_5)

    # 数据2
    draw_histogram_plot_1.draw_histogram_plot_1(number_2_1, the_method_2_1)
    draw_histogram_plot_1.draw_histogram_plot_1(number_2_2, the_method_2_2)
    draw_histogram_plot_1.draw_histogram_plot_1(number_2_3, the_method_2_3)
    draw_histogram_plot_1.draw_histogram_plot_1(number_2_4, the_method_2_4)
    draw_histogram_plot_1.draw_histogram_plot_1(number_2_5, the_method_2_5)
    '''

# 数据1,数据2统比较图
    '''
    draw_histogram_plot_2.draw_histogram_plot_2(number_1_1, number_1_2, number_1_3, number_1_4, number_1_5, number_2_1, number_2_2, number_2_3, number_2_4, number_2_5,
                                                The_method_1, The_method_2, The_method_3, The_method_4, The_method_5,
                                                mean_number_1_1, mean_number_1_2, mean_number_1_3, mean_number_1_4, mean_number_1_5,
                                                mean_number_2_1, mean_number_2_2, mean_number_2_3, mean_number_2_4, mean_number_2_5)
    '''

# 数据1,数据2统一绘图
    '''
    draw_histogram_plot_3.draw_histogram_plot_3(number_1_1, number_1_2, number_1_3, number_1_4, number_1_5, number_2_1, number_2_2, number_2_3, number_2_4, number_2_5,
                                                The_method_1, The_method_2, The_method_3, The_method_4, The_method_5,
                                                mean_number_1_1, mean_number_1_2, mean_number_1_3, mean_number_1_4, mean_number_1_5,
                                                mean_number_2_1, mean_number_2_2, mean_number_2_3, mean_number_2_4, mean_number_2_5)
    '''


# 数据处理方法二
    The_method = []
    # 数据1
    number_1 = []
    standard_deviation_1 = []
    mean_number_1 = []
    the_method_1 = []

    number_1.append(method_1.method_1(test_number, sample_collection_1))
    number_1.append(method_2.method_2(test_number, sample_collection_1))
    number_1.append(method_3.method_3(test_number, sample_collection_1))
    number_1.append(method_4.method_4(test_number, sample_collection_1))
    number_1.append(method_5.method_5(test_number, sample_collection_1))

    The_method.append(The_method_1)
    The_method.append(The_method_2)
    The_method.append(The_method_3)
    The_method.append(The_method_4)
    The_method.append(The_method_5)

    for i in range(0, 5):
        mean_number_1.append(calculate_average_value.calculate_average_value(number_1[i]))

    for i in range(0, 5):
        the_method_1.append(The_method_1 + " (average = {})".format(mean_number_1[i]))

    for i in range(0, 5):
        standard_deviation_1.append(calculate_standard_deviation.calculate_standard_deviation(number_1[i]))

    # 数据2
    number_2 = []
    standard_deviation_2 = []
    mean_number_2 = []
    the_method_2 = []

    number_2.append(method_1.method_1(test_number, sample_collection_2))
    number_2.append(method_2.method_2(test_number, sample_collection_2))
    number_2.append(method_3.method_3(test_number, sample_collection_2))
    number_2.append(method_4.method_4(test_number, sample_collection_2))
    number_2.append(method_5.method_5(test_number, sample_collection_2))

    for i in range(0, 5):
        mean_number_2.append(calculate_average_value.calculate_average_value(number_2[i]))

    for i in range(0, 5):
        the_method_2.append(The_method_2 + " (average = {})".format(mean_number_2[i]))

    for i in range(0, 5):
        standard_deviation_2.append(calculate_standard_deviation.calculate_standard_deviation(number_2[i]))

    # 统一绘图
    draw_histogram_plot_4.draw_histogram_plot_4(number_1, number_2, The_method, mean_number_1, mean_number_2)

    # 两次随机数据结果比较
    draw_histogram_plot_5.draw_histogram_plot_5(number_1, number_2, The_method, mean_number_1, mean_number_2)

    '''
    with open('average number', 'a') as f:
        for i in range(0, 5):
            f.write(The_method[i])
            f.write("       ")
        f.write("\n")
    '''
    put_average_car_number.put_average_car_number(The_method, mean_number_1, mean_number_2, standard_deviation_1, standard_deviation_2)


if __name__ == '__main__':
    run_view()
    plt.show()