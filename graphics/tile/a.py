# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install opencv-python

import numpy as np
import cv2
import math
from enum import Enum

class HorAlign(Enum):
	LEFT = 1
	MIDDLE = 2
	RIGHT = 3

class VertAlign(Enum):
	BOTTOM = 1
	MIDDLE = 2
	TOP = 3

class Rect:
	def __init__(self):
		self.mini = np.empty(2, np.int64)
		self.maxi = np.empty(2, np.int64)

def ceil_odd(x):
	return math.ceil(x) // 2 * 2 + 1

img_out_w = 300
img_out_h = 300
hor_align = HorAlign.MIDDLE
vert_align = VertAlign.MIDDLE

img_in = cv2.imread('dog.jpg')
img_in_w = img_in.shape[1]
img_in_h = img_in.shape[0]

hor_reps = None
vert_reps = None
rect = Rect()

if hor_align == HorAlign.LEFT:
	hor_reps = math.ceil(img_out_w / img_in_w)
	rect.mini[0] = 0
	rect.maxi[0] = img_out_w
elif hor_align == HorAlign.MIDDLE:
	hor_reps = ceil_odd(img_out_w / img_in_w)
	tiling_w = img_in_w * hor_reps
	rect.mini[0] = (tiling_w - img_out_w) / 2
	rect.maxi[0] = rect.mini[0] + img_out_w
elif hor_align == HorAlign.RIGHT:
	hor_reps = math.ceil(img_out_w / img_in_w)
	tiling_w = img_in_w * hor_reps
	rect.maxi[0] = tiling_w
	rect.mini[0] = rect.maxi[0] - img_out_w

if vert_align == VertAlign.BOTTOM:
	vert_reps = math.ceil(img_out_h / img_in_h)
	rect.mini[1] = 0
	rect.maxi[1] = img_out_h
elif vert_align == VertAlign.MIDDLE:
	vert_reps = ceil_odd(img_out_h / img_in_h)
	tiling_h = img_in_h * vert_reps
	rect.mini[1] = (tiling_h - img_out_h) / 2
	rect.maxi[1] = rect.mini[1] + img_out_h
elif vert_align == VertAlign.TOP:
	vert_reps = math.ceil(img_out_h / img_in_h)
	tiling_h = img_in_h * vert_reps
	rect.maxi[1] = tiling_h
	rect.mini[1] = rect.maxi[1] - img_out_h

tiling = np.tile(img_in, (vert_reps, hor_reps, 1))

img_out = tiling[rect.mini[1]:rect.maxi[1], rect.mini[0]:rect.maxi[0]]
cv2.imwrite('out.jpg', img_out)