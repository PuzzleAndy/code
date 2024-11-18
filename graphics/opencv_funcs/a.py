# License: CC0
# https://puzzleandy.com

import cv2

def bgr2rgb(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def bgr2rgba(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

def bgr2gray(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.imread('cow.jpg')
gray = bgr2gray(img)
bgr = bgr2rgb(img)
cv2.imwrite('gray.jpg', gray)
cv2.imwrite('bgr.jpg', bgr)


