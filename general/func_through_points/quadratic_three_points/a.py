import numpy as np
from matplotlib import pyplot as plt
import math

x1 = -1
y1 = -1
x2 = 0
y2 = 0
x3 = 4
y3 = -10

A = np.array([
	[math.pow(x1, 2), x1, 1],
	[math.pow(x2, 2), x2, 1],
	[math.pow(x3, 2), x3, 1]
], np.float32)
b = np.array([y1, y2, y3], np.float32)
x = np.linalg.solve(A, b)
r, s, t = x[0], x[1], x[2]

x = np.linspace(-5, 5)
y = r * x ** 2 + s * x + t

plt.plot(x, y, color='red')
plt.plot(x1, y1, color='black', marker='o')
plt.plot(x2, y2, color='black', marker='o')
plt.plot(x3, y3, color='black', marker='o')
plt.show()