import numpy as np
import math
import cv2
from enum import Enum

class HorPos:
	LEFT = 0
	MIDDLE = 1
	RIGHT = 2

class VertPos:
	BOTTOM = 0
	MIDDLE = 1
	TOP = 2

hor_pos = HorPos.LEFT
vert_pos = VertPos.BOTTOM

def noise(w, h, s, num_components, hor_pos=HorPos.MIDDLE, vert_pos=VertPos.MIDDLE):
	img = np.random.random_sample((math.ceil(h / s), math.ceil(w / s), num_components))
	img = np.uint8(img * 255)
	img = cv2.resize(img, (img.shape[1] * s, img.shape[0] * s), interpolation=cv2.INTER_NEAREST)
	if hor_pos == HorPos.LEFT:
		x = 0
	elif hor_pos == HorPos.RIGHT:
		x = s - w % s
	else:
		x = math.floor((s - w % s) / 2)
	if vert_pos == VertPos.BOTTOM:
		y = 0
	elif vert_pos == VertPos.TOP:
		y = s - h % s
	else:
		y = math.floor((s - h % s) / 2)
	img = img[y:y + h, x:x + w]
	return img

def grayscale_noise(w, h, s):
	return noise(w, h, s, 1)

def rgb_noise(w, h, s):
	return noise(w, h, s, 3)

def rgba_noise(w, h, s):
	return noise(w, h, s, 4)

w = 2500
h = 1642
s = 10
img = rgb_noise(w, h, s)
cv2.imwrite('out.png', img)