import numpy as np
from matplotlib import pyplot as plt
import math

pts = np.array([(-4, -100), (-1, 20), (0, -4), (1, 20), (4, 0)])

A = np.empty((len(pts), len(pts)), np.float32)
for i in range(0, len(pts)):
	for j in range(0, len(pts)):
		A[i, j] = math.pow(pts[i][0], j)
b = np.empty(len(pts), np.float32)
for i in range(0, len(pts)):
	b[i] = pts[i, 1]
x = np.linalg.solve(A, b)
poly = np.polynomial.Polynomial(x)

x = np.linspace(-5, 5)
y = poly(x)

plt.plot(x, y, color='red')
for i in range(0, len(pts)):
	plt.plot(pts[i, 0], pts[i, 1], color='black', marker='o')
plt.show()