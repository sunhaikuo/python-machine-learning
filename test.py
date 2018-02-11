import numpy as np
# import math
# import time
# num = 1000000
# a = np.random.rand(num)
# b = np.random.rand(num)

# tic = time.time()
# c = np.dot(a, b)
# toc = time.time()
# print('Vectorized ' + str((toc - tic) * 1000) + ' ms')

# c = 0
# tic = time.time()
# for i in range(num):
#     c += a[i] * b[i]
# toc = time.time()
# print('For Loop:' + str((toc - tic) * 1000) + ' ms')

# 初始一个5*2的矩阵
# print(np.zeros((5, 2)))

# 对某个数取自然对数，下面这个值是取e的平方
# print(math.exp(2))

# 对每一个矩阵元素取e
# c = np.zeros((5, 2))
# u = np.exp(c)
# print(u)

# 一行两列
# dw1 = np.array([1, 2])
# 二行一列
# dw2 = np.array([[1], [2]])
# 解出矩阵是几行几列
# print(dw1.shape)
# 矩阵相乘
# print(np.dot(dw1, dw2))

# 矩阵的转置
# dw1 = np.array([[1, 2, 3], [3, 4, 3], [5, 6, 3], [7, 8, 3]])
# dw2 = np.transpose(dw1)
# print(dw1.shape, dw2.shape)
# dw3 = np.dot(dw1, dw2)
# print(dw3)
# print(dw3.shape)

# 2.15-计算食物中各营养所占的比例
# A = np.array([[56, 0], [1.2, 104], [1.8, 135]])
# print(A)
# # 把各列加和，注：axis=0代表垂直相加
# cal = A.sum(axis=0)
# print(cal)
# # 再和上面相除, 注：加不加cal.reshape(1, 2)都一样
# percentage = (A / cal) * 100
# print(percentage)

# 2.16-关于python中的向量说明
# a = np.random.rand(3, 2)
# print(a)
# print(a.shape)
# a的转置
# print(a.T)
# 也表示a的转置
# print(np.transpose(a))
# 验证矩阵是否为相应维度的，如果是，则通过，什么都不打印，如果不是，则会报错
# assert (a.shape == (3, 2))

# log函数
import math
# 这是以log以e为底
# print(math.log(2.71))
# log以2为底
print(math.log(1 / 64, 2))
