import math
import numpy as np
import cv2

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
	return rgb_to_oklab(R, G, B)

def oklab_to_srgb(L, a, b):
	R, G, B = oklab_to_rgb(L, a, b)
	return rgb_to_srgb(R, G, B)

def lerp(a, b, t):
	return (1 - t) * a + t * b

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

left_sRGB = np.array([1, 1, 1], np.float32)
right_sRGB = np.array([0, 0, 1], np.float32)
H, S, V = rgb2hsv(*left_sRGB)
left_HSV = np.array([H, S, V], np.float32)
H, S, V = rgb2hsv(*right_sRGB)
right_HSV = np.array([H, S, V], np.float32)
left_HSV[0] = right_HSV[0]
L, a, b = srgb_to_oklab(*left_sRGB)
left_Oklab = np.array([L, a, b], np.float32)
L, a, b = srgb_to_oklab(*right_sRGB)
right_Oklab = np.array([L, a, b], np.float32)

w = 500
h = 151
img = np.empty((h, w, 3), np.float32)

for i in range(0, w):
	t = i / (w - 1)
	for j in range(0, math.floor(h / 2)):
		HSV = lerp(left_HSV, right_HSV, t)
		img[j, i] = hsv2rgb(left_HSV[0], HSV[1], HSV[2])
	for j in range(math.ceil(h / 2), h):
		Oklab = lerp(left_Oklab, right_Oklab, t)
		img[j, i] = oklab_to_srgb(*Oklab)
for j in range(0, w):
	img[math.floor(h / 2), j] = (0, 0, 0)

img = np.clip(img, 0, 1) * 255
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite('gradient.png', img)