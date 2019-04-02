# 最小二乘法
import numpy as np   # 科学计算库
import matplotlib.pyplot as plt  # 绘图库
from scipy.optimize import leastsq  # 引入最小二乘法算法
import seaborn as sns
import pandas as pd
import method_1
import method_2
import method_3

'''
    主要部分：附带部分说明
    1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
    2.官网的原话（第二个值）：Value of the cost function at the solution
    3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
    4.返回值元组中第一个值的数量跟需要求解的参数的数量一致
'''

# k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0 = 0.5

# 把error函数中除了p0以外的参数打包到args中(使用要求)
Para = []  # 储存leastq函数的返回值
Para.append(leastsq(method_1.error, p0, args=(method_1.Xi, method_1.Yi)))  # leastsq第一个参数是线性函数，第二个参数是线性回归起始值，第三个参数是数据
Para.append(leastsq(method_1.error, p0, args=(method_2.Xi, method_2.Yi)))
Para.append(leastsq(method_1.error, p0, args=(method_3.Xi, method_3.Yi)))


# 读取结果
k = []  # 线性函数中 k 值
for i in range(0, 3):
    k.append(Para[i][0][0])

for i in range(0, 3):
    print("--------------------------------------------")
    print("第{}种数学模型的结果".format(i+1))
    print("k=", k[i])
    print("cost：" + str(Para[i][1]))
    print("求解的拟合直线为:")
    print("y=" + str(round(k[i], 6)) + "x")


print("")
print("--------------------------------------------")
print("--------------------------------------------")
print("")
print("第一种数学模型 M = k * w * w * l 的拟合优度")
average_y_1 = np.mean(method_1.Yi)
fitting_y_1 = []
for i in range(0, 8):
    fitting_y_1.append(k[0] * method_1.Xi[i])

sum_1 = 0
sum_2 = 0
for i in range(0, 8):
    sum_1 = sum_1 + (method_1.Yi[i] - fitting_y_1[i])**2
    sum_2 = sum_2 + (method_1.Yi[i] - average_y_1)**2
R_1 = 1 - sum_1 / sum_2
print(round(R_1, 6))


print("--------------------------------------------")
print("第二种数学模型 M = k * L * L * L 的拟合优度")
average_y_2 = np.mean(method_2.Yi)
fitting_y_2 = []
for i in range(0, 8):
    fitting_y_2.append(k[1] * method_2.Xi[i])

sum_1 = 0
sum_2 = 0
for i in range(0, 8):
    sum_1 = sum_1 + (method_2.Yi[i] - fitting_y_2[i])**2
    sum_2 = sum_2 + (method_2.Yi[i] - average_y_2)**2
R_2 = 1 - sum_1 / sum_2
print(round(R_2, 6))


print("--------------------------------------------")
print("第三种数学模型 M = k * w * w * w 的拟合优度")
average_y_3 = np.mean(method_3.Yi)
fitting_y_3 = []
for i in range(0, 8):
    fitting_y_3.append(k[2] * method_3.Xi[i])

sum_1 = 0
sum_2 = 0
for i in range(0, 8):
    sum_1 = sum_1 + (method_3.Yi[i] - fitting_y_3[i])**2
    sum_2 = sum_2 + (method_3.Yi[i] - average_y_3)**2
R_3 = 1 - sum_1 / sum_2
print(round(R_3, 6))


'''
   绘图，看拟合效果.
'''

# 单个画图
# method_1
# 画样本点
plt.figure(figsize=(6, 6))  # 指定图像比例： 6：6
plt.scatter(method_1.Xi, method_1.Yi, color="green", label="Sample Data", linewidth=2)  # 参数一，二为点的数据，label参数为说明

# 画拟合直线
x = np.linspace(12000, 45000)  # 在12000，45000画线
y = k[0] * x  # 函数式
plt.plot(x, y, color="red", label="Fitting curve", linewidth=2)  # 参数一，二为拟合直线的数据，label参数为说明
plt.legend(loc='lower right')  # 绘制图例
plt.title("By: Exile Saber, Method_1: M = k * w * w * l, k = {}".format(round(k[0], 6)))  # 标头说明


# method_2
# 画样本点
plt.figure(figsize=(6, 6))  # 指定图像比例： 6：6
plt.scatter(method_2.Xi, method_2.Yi, color="green", label="Sample Data", linewidth=2)

# 画拟合直线
x = np.linspace(12000, 125000)
y = k[1] * x  # 函数式
plt.plot(x, y, color="red", label="Fitting curve", linewidth=2)
plt.legend(loc='lower right')  # 绘制图例
plt.title("By: Exile Saber, Method_2: M = k * l * l * l, k = {}".format(round(k[1], 6)))


# method_3
# 画样本点
plt.figure(figsize=(6, 6))  # 指定图像比例： 6：6
plt.scatter(method_3.Xi, method_3.Yi, color="green", label="Sample Data", linewidth=2)

# 画拟合直线
x = np.linspace(8000, 32768)
y = k[2] * x  # 函数式
plt.plot(x, y, color="red", label="Fitting curve", linewidth=2)
plt.legend(loc='lower right')  # 绘制图例
plt.title("By: Exile Saber, Method_3: M = k * w * w * w, k = {}".format(round(k[2], 6)))

plt.show()

'''
方法二，用 Seaborn 做回归分析画图
'''
fig = plt.figure(figsize=(24, 6))  # 设置画图区域大小
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# method_1
matrix = [method_1.Yi, method_1.Xi]
matrix[:] = map(list, zip(*matrix[::-1]))

data = pd.DataFrame(matrix, columns=["value", "quality"])  # 转化为DataFrame类型，并设置其上方信息栏
sns.regplot(x="value", y="quality", data=data, ax=ax1)  # 其中x和y为其横坐标和纵坐标的取值
ax1.set_title("By: Exile Saber, Method_1: M = k * w * w * l")


# method_2
matrix = [method_2.Yi, method_2.Xi]
matrix[:] = map(list, zip(*matrix[::-1]))

data = pd.DataFrame(matrix, columns=["value", "quality"])  # 转化为DataFrame类型，并设置其上方信息栏
sns.regplot(x="value", y="quality", data=data, ax=ax2)  # 其中x和y为其横坐标和纵坐标的取值
ax2.set_title("By: Exile Saber, Method_2: M = k * l * l * l")


# method_3
matrix = [method_3.Yi, method_3.Xi]
matrix[:] = map(list, zip(*matrix[::-1]))

data = pd.DataFrame(matrix, columns=["value", "quality"])  # 转化为DataFrame类型，并设置其上方信息栏
sns.regplot(x="value", y="quality", data=data, ax=ax3)  # 其中x和y为其横坐标和纵坐标的取值
ax3.set_title("By: Exile Saber, Method_3: M = k * w * w * w")

plt.show()
