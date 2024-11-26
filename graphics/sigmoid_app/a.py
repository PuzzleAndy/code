# pip install matplotlib
# pip install numpy
# pip install opencv-python

from matplotlib import pyplot as plt
import numpy as np
import math
import cv2

def hsl2rgb(H, SL, L):
	C = (1 - abs(2 * L - 1)) * SL
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
	m = L - C / 2
	R, G, B = R1 + m, G1 + m, B1 + m
	return R, G, B

def rgb2hsl(R, G, B):
	Xmax = V = max(R, G, B)
	Xmin = min(R, G, B)
	C = Xmax - Xmin
	L = (Xmax + Xmin) / 2
	if C == 0:
		H = 0
	elif V == R:
		H = 60 * ((G - B) / C % 6)
	elif V == G:
		H = 60 * ((B - R) / C + 2)
	elif V == B:
		H = 60 * ((R - G) / C + 4)
	if L == 0 or L == 1:
		SL = 0
	else:
		SL = C / (1 - abs(2 * V - C - 1))
	return H, SL, L

def sigmoid(x, a, b, c, d):
	s = ((1 - d) - b) / ((1 - c) - a)
	if 0 <= x and x < a:
		p = (s * a) / b
		return b * math.pow(x * (1 / a), p)
	elif 1 - c < x and x <= 1:
		q = (s * c) / d
		return -d * math.pow(-(x - 1) * (1 / c), q) + 1
	else:
		return s * (x - a) + b

a, b = 0.25, 0.2
c, d = 0.25, 0.2
img_in = cv2.imread('cat.png')
img_out = np.empty(img_in.shape, img_in.dtype)
for i in range(0, img_in.shape[0]):
	for j in range(0, img_in.shape[1]):
		R = img_in[i, j, 2] / 255
		G = img_in[i, j, 1] / 255
		B = img_in[i, j, 0] / 255
		R = sigmoid(R, a, b, c, d)
		G = sigmoid(G, a, b, c, d)
		B = sigmoid(B, a, b, c, d)
		img_out[i, j] = (B * 255, G * 255, R * 255)
cv2.imwrite('out.png', img_out)