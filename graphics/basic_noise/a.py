# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install pillow

import numpy as np
from PIL import Image

def white_noise_mat(w, h):
	return np.random.random_sample((h, w))

def white_noise_im(w, h):
	mat = white_noise_mat(w, h)
	return Image.fromarray(np.uint8(mat * 255))

def rgb_noise_mat(w, h):
	return np.random.random_sample((h, w, 3))

def rgb_noise_im(w, h):
	mat = rgb_noise_mat(w, h)
	return Image.fromarray(np.uint8(mat * 255))

def rgba_noise_mat(w, h):
	return np.random.random_sample((h, w, 4))

def rgba_noise_im(w, h):
	mat = rgba_noise_mat(w, h)
	return Image.fromarray(np.uint8(mat * 255))

w = 500
h = 500
im = rgb_noise_im(w, h)
im.save('out.png')