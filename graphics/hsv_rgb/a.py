# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install opencv-python

import numpy as np
import cv2

def hsv2rgb(H, SV, V):
	C = V * SV
	Hp = H / 60
	X = C * (1 - abs(Hp % 2 - 1))
	if 0 <= Hp < 1:
		R1, G1, B1 = C, X, 0
	elif 1 <= Hp < 2:
		R1, G1, B1 = X, C, 0
	elif 2 <= Hp < 3:
		R1, G1, B1 = 0, C, X
	elif 3 <= Hp < 4:
		R1, G1, B1 = 0, X, C
	elif 4 <= Hp < 5:
		R1, G1, B1 = X, 0, C
	elif 5 <= Hp < 6:
		R1, G1, B1 = C, 0, X
	m = V - C
	R, G, B = R1 + m, G1 + m, B1 + m
	return R, G, B

def rgb2hsv(R, G, B):
	Xmax = V = max(R, G, B)
	Xmin = min(R, G, B)
	C = Xmax - Xmin
	if C == 0:
		H = 0
	elif V == R:
		H = 60 * ((G - B) / C % 6)
	elif V == G:
		H = 60 * ((B - R) / C + 2)
	elif V == B:
		H = 60 * ((R - G) / C + 4)
	if V == 0:
		SV = 0
	else:
		SV = C / V
	return H, SV, V

def bgr2rgb(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_in = cv2.imread('gradient.jpg')
img_in = bgr2rgb(img_in)
img_out = np.empty(img_in.shape, img_in.dtype)
for i in range(0, img_in.shape[0]):
	for j in range(0, img_in.shape[1]):
		H, SV, V = rgb2hsv(*(img_in[i, j] / 255))
		R, G, B = hsv2rgb(H, SV / 2, V)
		img_out[i, j] = np.array([R, G, B]) * 255
img_out = bgr2rgb(img_out)
cv2.imwrite('out.jpg', img_out)