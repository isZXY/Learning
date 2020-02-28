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
