import matplotlib.pyplot as plt
import math

def circle(x1, y1, x2, y2, x3, y3):
	ma = (y2 - y1) / (x2 - x1)
	mb = (y3 - y2) / (x3 - x2)
	x = (ma * mb * (y1 - y3) + mb * (x1 + x2) - ma * (x2 + x3)) / (2 * (mb - ma))
	y = - (1 / ma) * (x - (x1 + x2) / 2) + (y1 + y2) / 2
	r = math.sqrt(math.pow(x1 - x, 2) + math.pow(y1 - y, 2))
	return x, y, r

x1 = 0
y1 = 0
x2 = 1
y2 = 1
x3 = 2
y3 = 0

x, y, r = circle(0, 0, 1, 1, 2, 0)
fig, ax = plt.subplots()
ax.add_patch(plt.Circle((x, y), r))
plt.plot(x1, y1, color='black', marker='o')
plt.plot(x2, y2, color='black', marker='o')
plt.plot(x3, y3, color='black', marker='o')
ax.set_box_aspect(1)
plt.axis([-5, 5, -5, 5])
plt.show()