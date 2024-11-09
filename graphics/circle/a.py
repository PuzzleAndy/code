import numpy as np
from matplotlib import pyplot as plt
import math

EPS = 0.0001

u = 0.5
v = 0.25

x1 = 0
y1 = 0
x2 = u
y2 = v
x3 = 1
y3 = 1

A1 = np.array([
	[x1**2 + y1**2, x1, y1, 1],
	[x2**2 + y2**2, x2, y2, 1],
	[x3**2 + y3**2, x3, y3, 1]
])

M11 = np.linalg.det(np.delete(A1, 0, 1))
M12 = np.linalg.det(np.delete(A1, 1, 1))
M13 = np.linalg.det(np.delete(A1, 2, 1))
M14 = np.linalg.det(np.delete(A1, 3, 1))

x0 = 0.5 * (M12 / M11)
y0 = -0.5 * (M13 / M11)
r0 = math.sqrt(x0**2 + y0**2 + M14 / M11)

x = np.linspace(x0 - r0, x0 + r0, 500)

y_pos = np.empty(len(x))
y_neg = np.empty(len(x))
for i in range(0, len(x)):
	y_pos[i] = y0 + math.sqrt(r0**2 - (x[i] - x0)**2)
	y_neg[i] = y0 - math.sqrt(r0**2 - (x[i] - x0)**2)

if (abs(y1 - (y0 + math.sqrt(r0**2 - (x1 - x0)**2))) < EPS
and abs(y2 - (y0 + math.sqrt(r0**2 - (x2 - x0)**2))) < EPS
and abs(y3 - (y0 + math.sqrt(r0**2 - (x3 - x0)**2))) < EPS):
	plt.plot(x, y_pos)

if (abs(y1 - (y0 - math.sqrt(r0**2 - (x1 - x0)**2))) < EPS
and abs(y2 - (y0 - math.sqrt(r0**2 - (x2 - x0)**2))) < EPS
and abs(y3 - (y0 - math.sqrt(r0**2 - (x3 - x0)**2))) < EPS):
	plt.plot(x, y_neg)

plt.plot(u, v, 'ro')
plt.savefig('plot.png')