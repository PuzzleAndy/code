# License: CC0
# https://puzzleandy.com

# pip install opencv-python
# pip install numpy

import cv2
import numpy as np

def resize(img, scale, interp=None):
	return cv2.resize(img, None, fx=scale, fy=scale, interpolation=interp)

def resize_width(img, w, interp=None):
	scale = w / img.shape[1]
	return resize(img, scale, interp)

def resize_height(img, h, interp=None):
	scale = h / img.shape[0]
	return resize(img, scale, interp)

def resize_max_width(img, w, interp=None):
	scale = w / img.shape[1]
	if scale < 1:
		return resize(img, scale, interp)
	return img

def resize_max_height(img, h, interp=None):
	scale = h / img.shape[0]
	if scale < 1:
		return resize(img, scale, interp)
	return img

def resize_min_width(img, w, interp=None):
	scale = w / img.shape[1]
	if scale > 1:
		return resize(img, scale, interp)
	return img

def resize_min_height(img, h, interp=None):
	scale = h / img.shape[0]
	if scale > 1:
		return resize(img, scale, interp)
	return img

def resize_min(img, w, h, interp=None):
	scale = np.array([w / img.shape[1], h / img.shape[0]])
	mini = min(scale[0], scale[1])
	if mini < 1:
		return resize(img, mini, interp)
	return img

def resize_max(img, w, h, interp=None):
	scale = np.array([w / img.shape[1], h / img.shape[0]])
	maxi = max(scale[0], scale[1])
	if maxi > 1:
		return resize(img, maxi, interp)
	return img

img_in = cv2.imread('a.jpg')
img_out_1 = resize(img_in, 0.1)
img_out_2 = resize_width(img_in, 500)
img_out_3 = resize_height(img_in, 500)
img_out_4 = resize_min_width(img_in, 500)
img_out_5 = resize_min_height(img_in, 500)
img_out_6 = resize_max_width(img_in, 500)
img_out_7 = resize_max_height(img_in, 500)
img_out_8 = resize_min(img_in, 500, 500)
img_out_9 = resize_max(img_in, 500, 500)

cv2.imwrite('percent_10.jpg', img_out_1)
cv2.imwrite('width_500.jpg', img_out_2)
cv2.imwrite('height_500.jpg', img_out_3)
cv2.imwrite('width.jpg', img_out_4)
cv2.imwrite('height.jpg', img_out_5)
cv2.imwrite('min_width.jpg', img_out_6)
cv2.imwrite('min_height.jpg', img_out_7)
cv2.imwrite('min.jpg', img_out_8)
cv2.imwrite('max.jpg', img_out_9)

cv2.waitKey(0)