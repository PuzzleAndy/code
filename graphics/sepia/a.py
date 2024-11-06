# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install opencv-python

import math
import numpy as np
import cv2

def lerp(a, b, t):
	return (1 - t) * a + t * b

class ColStop:
	def __init__(self, loc, col):
		self.loc = loc
		self.col = col

class AlphaStop:
	def __init__(self, loc, alpha):
		self.loc = loc
		self.alpha = alpha

col_stops = [
	ColStop(0, np.array([0, 0, 0])),
	ColStop(0.5, np.array([134 / 255, 122 / 255, 101 / 255])),
	ColStop(1, np.array([1, 1, 1])),
]
col_mids = [0.5, 0.5]
alpha_stops = [
	AlphaStop(0, 1),
	AlphaStop(1, 1)
]
alpha_mids = [0.5]

loc = 0.25
def gradient_map_pixel(col_stops, col_mids, alpha_stops, alpha_mids, loc):
	col = None
	alpha = None

	if loc < col_stops[0].loc:
		col = col_stops[0].col
	elif loc > col_stops[-1].loc:
		col = col_stops[-1].col
	else:
		for i in range(0, len(col_stops)):
			if loc == col_stops[i].loc:
				col = col_stops[i].col
				break
		if col is None:
			for i in range(0, len(col_stops) - 1):
				if col_stops[i].loc < loc and loc < col_stops[i + 1].loc:
					t = (loc - col_stops[i].loc) / (col_stops[i + 1].loc - col_stops[i].loc)
					u = t**(math.log(0.5) / math.log(col_mids[i]))
					col = lerp(col_stops[i].col, col_stops[i + 1].col, u)
					break

	if loc < alpha_stops[0].loc:
		alpha = alpha_stops[0].alpha
	elif loc > alpha_stops[-1].loc:
		alpha = alpha_stops[-1].alpha
	else:
		for i in range(0, len(alpha_stops)):
				if loc == alpha_stops[i].loc:
					alpha = alpha_stops[i].alpha
					break
		if alpha is None:
			for i in range(0, len(alpha_stops) - 1):
				if alpha_stops[i].loc < loc and loc < alpha_stops[i + 1].loc:
					t = (loc - alpha_stops[i].loc) / (alpha_stops[i + 1].loc - alpha_stops[i].loc)
					u = t**(math.log(0.5) / math.log(alpha_mids[i]))
					alpha = lerp(alpha_stops[i].alpha, alpha_stops[i + 1].alpha, u)
					break
	return np.array([col[0], col[1], col[2], alpha])

def rgba2bgra(img):
	return cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)

def gradient_map(col_stops, col_mids, alpha_stops, alpha_mids, img):
	img_out_shape = (img.shape[0], img.shape[1], 4)
	img_out = np.empty(img_out_shape, dtype=img.dtype)
	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			loc = img[i, j] / 255
			col = gradient_map_pixel(col_stops, col_mids, alpha_stops, alpha_mids, loc)
			img_out[i, j] = col * 255
	img_out = rgba2bgra(img_out)
	return img_out

img_in = cv2.imread('flowers.jpg', cv2.IMREAD_GRAYSCALE)
img_out = gradient_map(col_stops, col_mids, alpha_stops, alpha_mids, img_in) 
cv2.imwrite('flowers_sepia.jpg', img_out)

img_in = cv2.imread('jellyfish.jpg', cv2.IMREAD_GRAYSCALE)
img_out = gradient_map(col_stops, col_mids, alpha_stops, alpha_mids, img_in) 
cv2.imwrite('jellyfish_sepia.jpg', img_out)

img_in = cv2.imread('woman.jpg', cv2.IMREAD_GRAYSCALE)
img_out = gradient_map(col_stops, col_mids, alpha_stops, alpha_mids, img_in) 
cv2.imwrite('woman_sepia.jpg', img_out)