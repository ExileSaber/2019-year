# 区间均分模型
import numpy as np


def method_5(test_number, sample_collection):
    """此处test_number为样本数量，sample_collection为所有样本集合，此列表中的元素为各个样本的车牌号
    """

    number = np.zeros(test_number)
    for i in range(test_number):
        max_test_car_number = np.max(sample_collection[i])
        number[i] = (1 + 1 / (2 * test_number)) * max_test_car_number
    return number