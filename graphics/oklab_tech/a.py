import math
import numpy as np

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

def rgb_to_oklab(R, G, B):

	l = 0.4122214708 * R + 0.5363325363 * G + 0.0514459929 * B
	m = 0.2119034982 * R + 0.6806995451 * G + 0.1073969566 * B
	s = 0.0883024619 * R + 0.2817188376 * G + 0.6299787005 * B

	l_ = math.cbrt(l)
	m_ = math.cbrt(m)
	s_ = math.cbrt(s)

	return (
		0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
		1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
		0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
	)

def oklab_to_rgb(L, a, b):

	l_ = L + 0.3963377774 * a + 0.2158037573 * b
	m_ = L - 0.1055613458 * a - 0.0638541728 * b
	s_ = L - 0.0894841775 * a - 1.2914855480 * b

	l = l_ * l_ * l_
	m = m_ * m_ * m_
	s = s_ * s_ * s_

	return (
		+4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
		-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
		-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
	)

def srgb_to_oklab(sR, sG, sB):
	R, G, B = srgb_to_rgb(sR, sG, sB)
	print(R, G, B)
	return rgb_to_oklab(R, G, B)

def oklab_to_srgb(L, a, b):
	R, G, B = oklab_to_rgb(L, a, b)
	return rgb_to_srgb(R, G, B)

sR, sG, sB = 0, 0, 0.1
L, a, b = srgb_to_oklab(sR, sG, sB)
print(L, a, b)
sR, sG, sB = oklab_to_srgb(L, a, b)
print(sR, sG, sB)