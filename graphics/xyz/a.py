# pip install numpy

import numpy as np

# sRGB D65
def rgb_to_xyz(RGB):
	return np.array([
		[.4124564, .3575761, .1804375],
		[.2126729, .7151522, .0721750],
		[.0193339, .1191920, .9503041]
	]).dot(RGB)

# sRGB D65
def xyz_to_rgb(XYZ):
	return np.array([
		[ 3.2404542, -1.5371385, -0.4985314],
		[-0.9692660,  1.8760108,  0.0415560],
		[ 0.0556434, -0.2040259,  1.0572252]
	]).dot(XYZ)

RGB = np.array([1, 1, 1], np.float32)
XYZ = rgb_to_xyz(RGB)
print(XYZ)
RGB = xyz_to_rgb(XYZ)
print(RGB)