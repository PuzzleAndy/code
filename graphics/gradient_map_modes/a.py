import cv2
from matplotlib import pyplot as plt
import numpy as np
import math

def lerp(a, b, t):
	return (1 - t) * a + t * b

n = 50

def plot(path_in, path_out):
	img = cv2.imread(path_in, cv2.IMREAD_GRAYSCALE)
	w = img.shape[1]
	x = np.linspace(0, 1, n)
	y = np.empty(n)
	for i in range(0, n):
		u = i * (w - 1) / (n - 1)
		if u.is_integer():
			y[i] = img[0, int(u)]
		else:
			frac_part, int_part = math.modf(u)
			a = img[0, int(int_part)]
			b = img[0, int(int_part) + 1]
			y[i] = lerp(a, b, frac_part)
	plt.clf()
	plt.plot(x, y, color='red')
	plt.savefig(path_out)

plot('id.jpg', 'plots/id.jpg')
plot('perceptual.jpg', 'plots/perceptual.jpg')
plot('linear.jpg', 'plots/linear.jpg')
plot('classic.jpg', 'plots/classic.jpg')
plot('smooth.jpg', 'plots/smooth.jpg')