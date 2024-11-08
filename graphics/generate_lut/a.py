# License: CC0
# https://puzzleandy.com

# pip install opencv-python
# pip install numpy

import cv2
import numpy as np
import math

# n is a square number
n = 64

sqrt_n = int(math.sqrt(n))
img = np.empty((n * sqrt_n, n * sqrt_n, 3), np.uint8)
for i in range(0, sqrt_n):
	for j in range(0, sqrt_n):
		for u in range(0, n):
			for v in range(0, n):
				R = v / (n - 1) * 255
				G = u / (n - 1) * 255
				B = (i * sqrt_n + j) / (n - 1) * 255
				img[n * i + u, n * j + v] = (B, G, R)
cv2.imwrite('neutral.png', img)