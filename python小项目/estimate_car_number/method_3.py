# 两端间隔对称模型
import numpy as np

def method_3(test_number, sample_collection):
    """此处test_number为样本数量，sample_collection为所有样本集合，此列表中的元素为各个样本的车牌号
    """

    number = np.zeros(test_number)
    for i in range(test_number):
        max_test_car_number = np.max(sample_collection[i])
        min_test_car_number = np.min(sample_collection[i])
        number[i] = max_test_car_number + min_test_car_number-1
    return number