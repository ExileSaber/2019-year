# 获取test_number个样本，和每个样本中test_car_number个车牌号
import random
import numpy as np


def get_random_number(max_car_number, test_car_number, test_number):
    """此处max_number为实际车辆的最大值（假设已经知道的情况下），test_car_number为你样本抽取的车牌的数量,test_number为样本数量
    """

    sample_collection = np.zeros((test_number, test_car_number), dtype=int)  # 所有样本集合，列表中的元素仍然是列表
    for i in range(0, test_number):
        for j in range(0, test_car_number):
            sample_collection[i][j] = random.randint(1, max_car_number)
    return sample_collection