# License: CC0
# https://puzzleandy.com

# pip install matplotlib
# pip install numpy

from matplotlib import pyplot as plt
import numpy as np
import sys

def lerp(a, b, t):
	return (1 - t) * a + t * b

class Bez:

	def __init__(self, pts):
		self.pts = pts

	def de_casteljau(self, t):
		pts = np.copy(self.pts)
		for i in range(0, len(pts)):
			for j in range(0, len(pts) - 1 - i):
				pts[j] = lerp(pts[j], pts[j + 1], t)
		return pts[0]

	def split(self, t):
		left = np.empty((len(self.pts), 2), np.float32)
		right = np.empty((len(self.pts), 2), np.float32)
		pts = np.copy(self.pts)
		for i in range(0, len(pts)):
			for j in range(0, len(pts) - 1 - i):
				if j == 0:
					left[i] = pts[j]
				if j == len(pts) - 1 - i - 1:
					right[i] = pts[j + 1]
				pts[j] = lerp(pts[j], pts[j + 1], t)
		left[-1] = pts[0]
		right[-1] = pts[0]
		return Bez(left), Bez(right)

bez = Bez(np.array([(0, 0), (1, 0), (1, 1), (2, 1)], np.float32))

plt.clf()
pts = []
for t in np.linspace(0, 1, 100):
	pts.append(bez.de_casteljau(t))
x, y = zip(*pts)
plt.plot(x, y)
plt.savefig('de_casteljau.png')

plt.clf()
left, right = bez.split(0.33)
pts = []
for t in np.linspace(0, 1, 100):
	pts.append(left.de_casteljau(t))
x, y = zip(*pts)
plt.plot(x, y, color='red')
pts = []
for t in np.linspace(0, 1, 100):
	pts.append(right.de_casteljau(t))
x, y = zip(*pts)
plt.plot(x, y, color='blue')
plt.savefig('split.png')