# License: CC0
# https://puzzleandy.com

import cv2
import numpy as np
from blend_modes import multiply

def resize(img, w, h, interp=None):
	return cv2.resize(img, (w, h), interpolation=interp)

img_1 = cv2.imread('building.jpg', -1)
img_1 = cv2.cvtColor(img_1, cv2.COLOR_RGB2RGBA)
img_1 = img_1.astype(float)
img_2 = cv2.imread('gradient.jpg', -1)
img_2 = cv2.cvtColor(img_2, cv2.COLOR_RGB2RGBA)
img_2 = img_2.astype(float)
img_2 = resize(img_2, img_1.shape[1], img_1.shape[0])
img_out = multiply(img_1, img_2, 1)
cv2.imwrite('out.png', img_out.astype(np.uint8))
cv2.waitKey()