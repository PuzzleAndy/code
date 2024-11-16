# License: CC0
# https://puzzleandy.com

import cv2
import numpy as np

def rgb_to_yuv_lum(R, G, B):
	Y = 0.299 * R + 0.587 * G + 0.114 * B
	return Y

img_in = cv2.imread('horses.jpg')
img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
img_in = img_in.astype(np.float32) / 255
img_out = np.empty(img_in.shape, np.float32)
for i in range(img_in.shape[0]):
	for j in range(img_in.shape[1]):
		img_out[i, j] = rgb_to_yuv_lum(*img_in[i, j])
img_out = (np.clip(img_out, 0, 1) * 255).astype(np.uint8)
cv2.imwrite('out.jpg', img_out)