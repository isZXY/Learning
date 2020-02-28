import numpy as np

#######################################矩阵#######################################
a = np.array([[2, 33, 4],
              [3, 3, 4]], float)
print(a)


#零矩阵
a = np.zeros((4,5))
print(a)


#空矩阵
a = np.empty((3, 5))
print(a)


#范围生成
a = np.arange(12).reshape((3, 4))
print(a)


#线性
a = np.linspace(1, 10, 20)
#linespace(开始值，终止值，需要的格式（自动计算步长）)
#后面也可加.reshape()
print(a)




#######################################Numpy基本计算#######################################
a = np.array([10, 20, 30, 40])
b = np.arange(4)


# 加减法
c = a - b  
# [10 19 28 37]


# 乘方
c = b ** 2  
# [0 1 4 9]


# 对b里的每一个值计算sin函数后乘10
c = 10 * np.sin(b)
# cos,tan同理
# 是弧度制
# [0.         8.41470985 9.09297427 1.41120008]


# 输出一个矩阵，该矩阵输出每一个元素是否满足b<3，是True或False
print(b < 3)
# [ True  True  True False]


# 逐个数字相乘和矩阵乘法
a = np.array([[10, 20],
              [6, 4]])
b = np.arange(4).reshape((2, 2))
c = a * b  # 逐个数字相乘
print(c)
c_dot = np.dot(a, b)  # 矩阵乘法
print(c_dot)
# [[ 0 20]
#  [12 12]]
# [[40 70]
#  [ 8 18]]


# 随机生成0-1的数
a = np.random.random((2, 4))
print(a)
print(np.sum(a, axis=0))  # 最小值
# axis代表在行/列分别执行
print(np.max(a))  # 最大值
# [[0.35887414 0.52273135 0.90675385 0.07984126]
#  [0.81033916 0.65081447 0.09235465 0.26689238]]
# 3.6886012435758095
# 0.07984126472710662
# 0.906753848261088


# 求平均值、中位数
print(np.median(A))  # 中位数
print(np.mean(A))  # 平均值
# 7.5
# 7.5


# 寻找最值的索引
A = np.arange(2, 14).reshape((3, 4))
print(np.argmax(A))
print(np.argmin(A))
# 11
# 0

# 求平均值、中位数
print(np.median(A))  # 中位数
print(np.mean(A))  # 平均值
# 7.5
# 7.5


# 累加/累差
print(np.cumsum(A))  # 累加
print(np.diff(A))
# [ 2  5  9 14 20 27 35 44 54 65 77 90]
# [[1 1 1]
# [1 1 1]
# [1 1 1]]


# 排序
np.sort(A)


# 输出非零的行列
np.nonzero(A)


#矩阵转置
np.transpose(A)
A.T   # 功能也是
# [[1 1 1]转置
# [[1 1 1]
# [[1 1 1]


#clip功能
A = np.arange(2, 14).reshape((3, 4))
print(np.clip(A, 5, 9))
# [[5 5 5 5]
#  [6 7 8 9]
#  [9 9 9 9]]
# 所有低于5的值变成5，高于9的值变成9


# 合并列矩阵
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

print(np.vstack((A, B)))
# [[1 1 1]
#  [2 2 2]]

# 合并行矩阵
print(np.hstack((A, B)))
# [1 1 1 2 2 2]
