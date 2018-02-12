import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# 画图形：先确定范围，然后画多个图形，最后show
# x = np.linspace(0, 2 * np.pi, 50)
# plt.plot(x, np.sin(x), x, np.cos(x), x, np.sin(2 * x))
# plt.show()

# 这三个值表示：行、列、活跃区
# plt.subplot(2, 1, 1)
# plt.plot(x, np.sin(x), 'r')
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x), 'g')
# plt.show()

# 带离散点的sinx
# plt.scatter(x, np.sin(x))
# plt.show()

# 散点图
# x = np.random.rand(100)
# y = np.random.rand(100)
# # 每个点的大小
# size = np.random.rand(100) * 100
# color = np.random.rand(100)
# plt.scatter(x, y, size, color)
# plt.colorbar()
# plt.show()

# 加标签
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-', label='Cos(x)')
plt.legend()
plt.xlabel('Rads')
plt.ylabel('Amp')
plt.title('Sin an Cos Wave')
plt.show()
