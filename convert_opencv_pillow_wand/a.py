# License: CC0
# https://puzzleandy.com

import cv2
import PIL.Image
import numpy as np
import wand.image
from itertools import combinations

# OpenCV
arr_in_1 = cv2.imread('a.jpg') 
arr_in_1 = cv2.cvtColor(arr_in_1, cv2.COLOR_BGR2RGB)

# Pillow
img_in_2 = PIL.Image.open('a.jpg')
arr_in_2 = np.array(img_in_2)

# Wand
arr_in_3 = None
with wand.image.Image(filename='a.jpg') as img_in_3:
	arr_in_3 = np.array(img_in_3)

def all_equal(f, arr):
	return all([f(i, j) for i, j in combinations(arr, 2)])

print(all_equal(np.array_equiv, [arr_in_1, arr_in_2, arr_in_3]))

# OpenCV
arr_out_1 = cv2.cvtColor(arr_in_1, cv2.COLOR_BGR2RGB)
cv2.imwrite('cv.jpg', arr_out_1)

# Pillow
img_out_2 = PIL.Image.fromarray(np.uint8(arr_in_1))
img_out_2.save('pil.jpg')

# Wand
with wand.image.Image.from_array(arr_in_3) as img_out_3:
	img_out_3.save(filename='wand.jpg')