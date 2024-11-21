import numpy as np

def rot(v):
	return np.array([
		v[0] * math.cos(theta) - v[1] * math.sin(theta),
		v[0] * math.sin(theta) + v[1] * math.cos(theta)
	], v.dtype)

def rot90(v):
	return np.array([-v[1], v[0]], v.dtype)

def rot180(v):
	return np.array([-v[0], -v[1]], v.dtype)

def rot270(v):
	return np.array([v[1], -v[0]], v.dtype)

v = np.array([2, 1], np.float32)
print(rot90(v))
print(rot180(v))
print(rot270(v))