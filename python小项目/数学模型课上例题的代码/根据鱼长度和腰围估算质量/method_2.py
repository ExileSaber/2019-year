import numpy as np   # 科学计算库

'''
     设置样本数据，真实数据需要在这里处理
'''

# 样本初始数据
w = np.array([24.8, 21.3, 27.9, 24.8, 21.6, 31.8, 22.9, 21.6])  # 胸围
M = np.array([765, 482, 1162, 737, 482, 1389, 652, 454])  # 质量
L = np.array([36.8, 31.8, 43.8, 36.8, 32.1, 45.1, 35.9, 32.1])  # 身长

# 计算样本数据(Xi,Yi)，根据 M = k * L * L * L 的公式
Xi = L * L * L
Yi = M

'''
    设定拟合函数和偏差函数
    函数的形状确定过程：
    1.先画样本图像
    2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
'''

# 需要拟合的函数func :指定函数的形状
def func(p, x):
    k = p
    return k * x

# 偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p, x, y):
    return func(p, x)-y