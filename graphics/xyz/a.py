# pip install numpy

import numpy as np
import math

def compand(v):
	if v <= 0.0031308:
		return 12.92 * v
	else:
		return 1.055 * math.pow(v, 1 / 2.4) - 0.055

def inv_compand(V):
	if V <= 0.04045:
		return V / 12.92
	else:
		return math.pow((V + 0.055) / 1.055, 2.4)

def rgb_to_srgb(R, G, B):
	return (
		compand(R),
		compand(G),
		compand(B)
	)

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

# sRGB D65
def xyz_to_rgb(X, Y, Z):
	RGB = np.array([
		[ 3.2404542, -1.5371385, -0.4985314],
		[-0.9692660,  1.8760108,  0.0415560],
		[ 0.0556434, -0.2040259,  1.0572252]
	]).dot(np.array([X, Y, Z], np.float32) / 100)
	return RGB[0], RGB[1], RGB[2]

def xyz_to_srgb(X, Y, Z):
	R, G, B = xyz_to_rgb(X, Y, Z)
	return rgb_to_srgb(R, G, B)

def srgb_to_xyz(sR, sG, sB):
	R, G, B = srgb_to_rgb(sR, sG, sB)
	return rgb_to_xyz(R, G, B)

sR, sG, sB = 0, 0, 0.1
X, Y, Z = srgb_to_xyz(sR, sG, sB)
print(X, Y, Z)
sR, sG, sB = xyz_to_srgb(X, Y, Z)
print(sR, sG, sB)