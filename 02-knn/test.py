import numpy as np
import operator as op

# 拼接数组
a = np.array([3, 4])
b = np.array([1, 2])
c = np.concatenate([a, b])

# 数组append
a = np.array([1, 2, 3])
b = np.array([4, 5])
c = np.append(a, b)

# 对象操作
obj = {}
# obj['sunhk'] = 1
# print(obj.get('sunhk'))
obj['sunhk'] = obj.get('sunhk', 0) + 1
print(obj)

# 空数组
a = np.array([])
b = np.append(a, 1)
print(b)

print(str(0))

# a = np.zeros((1, 3))
# print(type(a))
# a[0, :] = [4, 5, 6]
# a[1, :] = [1, 2, 3]
# print(a)

# 数组属性
# a = np.array([[1, 2], [3, 4]])
# b = np.tile(a, (1, 1))
# # print(b)
# a = np.array([14, 15, 13, 12, 11])

# 数组排序
# a = {"id": 1, "name": 0}
# print(sorted(a.items(), key=op.itemgetter(1)))

# 对象排序