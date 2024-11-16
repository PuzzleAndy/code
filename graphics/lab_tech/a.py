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

def xyz_to_lab(X, Y, Z):

	# Reference white
	Xr = 95.047
	Yr = 100
	Zr = 108.883

	xr = X / Xr
	yr = Y / Yr
	zr = Z / Zr

	eps = 216 / 24389
	kappa = 24389 / 27

	if xr > eps:
		fx = math.cbrt(xr)
	else:
		fx = (kappa * xr + 16) / 116

	if yr > eps:
		fy = math.cbrt(yr)
	else:
		fy = (kappa * yr + 16) / 116

	if zr > eps:
		fz = math.cbrt(zr)
	else:
		fz = (kappa * zr + 16) / 116

	L = 116 * fy - 16
	a = 500 * (fx - fy)
	b = 200 * (fy - fz)

	return L, a, b

def lab_to_xyz(L, a, b):

	# Reference white
	Xr = 95.04
	Yr = 100
	Zr = 108.883

	fy = (L + 16) / 116
	fx = a / 500 + fy
	fz = fy - b / 200

	eps = 216 / 24389
	kappa = 24389 / 27

	fx3 = math.pow(fx, 3)
	if fx3 > eps:
		xr = fx3
	else:
		xr = (116 * fx - 16) / kappa

	if L > kappa * eps:
		yr = math.pow((L + 16) / 116, 3)
	else:
		yr = L / kappa

	fz3 = math.pow(fz, 3)
	if fz3 > eps:
		zr = fz3
	else:
		zr = (116 * fz - 16) / kappa

	X = xr * Xr
	Y = yr * Yr
	Z = zr * Zr

	return X, Y, Z

def xyz_to_srgb(X, Y, Z):
	R, G, B = xyz_to_rgb(X, Y, Z)
	return rgb_to_srgb(R, G, B)

def srgb_to_xyz(sR, sG, sB):
	R, G, B = srgb_to_rgb(sR, sG, sB)
	return rgb_to_xyz(R, G, B)

def lab_to_srgb(L, a, b):
	X, Y, Z = lab_to_xyz(L, a, b)
	return xyz_to_srgb(X, Y, Z)

def srgb_to_lab(sR, sG, sB):
	X, Y, Z = srgb_to_xyz(sR, sG, sB)
	return xyz_to_lab(X, Y, Z)

sR, sG, sB = 0, 0, 0.1
L, a, b = srgb_to_lab(sR, sG, sB)
print(L, a, b)
sR, sG, sB = lab_to_srgb(L, a, b)
print(sR, sG, sB)
