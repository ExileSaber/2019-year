import numpy as np
x = np.zeros(10)
y = np.arange(10, 50, 2)
z = np.tile(np.array([1]), (5, 5)).astype(np.int32)
z += z

a = np.arange(15)
b = np.arange(1, 16)
c = a - b