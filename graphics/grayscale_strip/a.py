# License: CC0
# https://puzzleandy.com

# pip install opencv-python

import cv2
import numpy as np

w = 500
h = 75

def hue2rgb(H):
	C = 1
	Hp = H / 60
	X = 1 - abs(Hp % 2 - 1)
	R, G, B = None, None, None
	if 0 <= Hp < 1:
		R, G, B = 1, X, 0
	elif 1 <= Hp < 2:
		R, G, B = X, 1, 0
	elif 2 <= Hp < 3:
		R, G, B = 0, 1, X
	elif 3 <= Hp < 4:
		R, G, B = 0, X, 1
	elif 4 <= Hp < 5:
		R, G, B = X, 0, 1
	elif 5 <= Hp < 6:
		R, G, B = 1, 0, X
	return R, G, B

img = np.empty((h, w, 3), np.uint8)
for i in range(0, w):
	L = i / (w - 1)
	L *= 255
	for j in range(0, h):
		img[j, i] = (L, L, L)
cv2.imwrite('grayscale_strip.jpg', img)
		