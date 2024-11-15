# pip install numpy

import numpy as np

# sRGB D65
def rgb_to_xyz(rgb):
	return np.array([
		[.4124564, .3575761, .1804375],
		[.2126729, .7151522, .0721750],
		[.0193339, .1191920, .9503041]
	]).dot(rgb)

# sRGB D65
def xyz_to_rgb(xyz):
	return np.array([
		[ 3.2404542, -1.5371385, -0.4985314],
		[-0.9692660,  1.8760108,  0.0415560],
		[ 0.0556434, -0.2040259,  1.0572252]
	]).dot(xyz)

rgb = np.array([1, 1, 1], np.float32)
xyz = rgb_to_xyz(rgb)
print(xyz)
rgb = xyz_to_rgb(xyz)
print(rgb)