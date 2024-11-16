import numpy as np
import math
import cv2

def inv_compand(V):
	if V <= 0.04045:
		return V / 12.92
	else:
		return math.pow((V + 0.055) / 1.055, 2.4)

def srgb_to_rgb(sR, sG, sB):
	return (
		inv_compand(sR),
		inv_compand(sG),
		inv_compand(sB)
	)

# sRGB D65
def rgb_to_xyz(R, G, B):
	XYZ = np.array([
		[.4124564, .3575761, .1804375],
		[.2126729, .7151522, .0721750],
		[.0193339, .1191920, .9503041]
	]).dot(np.array([R, G, B], np.float32)) * 100
	return XYZ[0], XYZ[1], XYZ[2]

def xyz_to_lab_lum(X, Y, Z):

	# Reference white
	Yr = 100

	yr = Y / Yr

	eps = 216 / 24389
	kappa = 24389 / 27

	if yr > eps:
		fy = math.cbrt(yr)
	else:
		fy = (kappa * yr + 16) / 116

	L = 116 * fy - 16
	return L

def srgb_to_xyz(sR, sG, sB):
	R, G, B = srgb_to_rgb(sR, sG, sB)
	return rgb_to_xyz(R, G, B)

def srgb_to_lab_lum(R, G, B):
	X, Y, Z = srgb_to_xyz(R, G, B)
	return xyz_to_lab_lum(X, Y, Z)

img_in = cv2.imread('horses.jpg')
img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
img_in = img_in.astype(np.float32) / 255
img_out = np.empty(img_in.shape, np.float32)
for i in range(img_in.shape[0]):
	for j in range(img_in.shape[1]):
		img_out[i, j] = srgb_to_lab_lum(*img_in[i, j]) / 100
img_out = (np.clip(img_out, 0, 1) * 255).astype(np.uint8)
cv2.imwrite('out.jpg', img_out)
