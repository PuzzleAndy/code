# License: CC0
# https://puzzleandy.com

# pip install opencv-python
# pip install numpy

import cv2
import numpy as np
import math

w = 300
h = 300

def dist(p2, p1):
	return np.linalg.norm(p2 - p1)

def cart2polar(p, c):
	return dist(p, c), math.atan2((p[1] - c[1]), (p[0] - c[0]))

def deg2rad(theta):
	return theta * math.pi / 180

def norm_angle(theta):
	return theta - math.tau * math.floor(theta / math.tau)

def hor(mini, maxi):
	img = np.empty((w, h), np.float32)
	for i in range(0, h):
		for j in range(0, w):
			img[i, j] = np.clip((j - mini) / (maxi - mini), 0, 1)
	return img

def vert(mini, maxi):
	img = np.empty((w, h), np.float32)
	for i in range(0, h):
		for j in range(0, w):
			img[i, j] = np.clip((i - mini) / (maxi - mini), 0, 1)
	return img

def circle(r, c):
	img = np.empty((w, h), np.float32)
	for i in range(0, h):
		for j in range(0, w):
			p = np.array([j, i])
			polar_r, theta = cart2polar(p, c)
			norm_theta = norm_angle(theta)
			img[i, j] = min(polar_r / r, 1)
	return img

def ellipse(a, b, c, theta):
	img = np.empty((w, h), np.float32)
	for i in range(0, h):
		for j in range(0, w):
			p = np.array([j, i])
			polar_r, theta = cart2polar(p, c)
			norm_theta = norm_angle(theta + theta_off)
			ellipse_r = (a * b) / math.sqrt((b * math.cos(norm_theta))**2 + (a * math.sin
	(norm_theta))**2)
			img[i, j] = min(polar_r / ellipse_r, 1)
	return img

mini = w / 4
maxi = 2 * w / 4
hor_img = hor(mini, maxi)
cv2.imwrite('hor.png', hor_img * 255)

mini = w / 4
maxi = 2 * w / 4
vert_img = vert(mini, maxi)
cv2.imwrite('vert.png', vert_img * 255)

a = 200
b = 100
c = np.array([w / 2, h / 3])
theta_off = deg2rad(20)
ellipse_img = ellipse(a, b, c, theta_off)
cv2.imwrite('ellipse.png', ellipse_img * 255)

r = 200
c = np.array([w / 2, h / 2])
circle_img = circle(r, c)
cv2.imwrite('circle.png', circle_img * 255)

cv2.waitKey(0)