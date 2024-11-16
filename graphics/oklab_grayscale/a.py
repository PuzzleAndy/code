import math
import numpy as np
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

def rgb_to_oklab_lum(R, G, B):

	l = 0.4122214708 * R + 0.5363325363 * G + 0.0514459929 * B
	m = 0.2119034982 * R + 0.6806995451 * G + 0.1073969566 * B
	s = 0.0883024619 * R + 0.2817188376 * G + 0.6299787005 * B

	l_ = math.cbrt(l)
	m_ = math.cbrt(m)
	s_ = math.cbrt(s)

	return 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_

def srgb_to_oklab_lum(sR, sG, sB):
	R, G, B = srgb_to_rgb(sR, sG, sB)
	return rgb_to_oklab_lum(R, G, B)

img_in = cv2.imread('horses.jpg')
img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
img_in = img_in.astype(np.float32) / 255
img_out = np.empty(img_in.shape, np.float32)
for i in range(img_in.shape[0]):
	for j in range(img_in.shape[1]):
		img_out[i, j] = srgb_to_oklab_lum(*img_in[i, j])
img_out = (np.clip(img_out, 0, 1) * 255).astype(np.uint8)
cv2.imwrite('out.jpg', img_out)