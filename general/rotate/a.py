import numpy as np

def rot(x, y):
	xp = x * math.cos(theta) - y * math.sin(theta)
	yp = x * math.sin(theta) + y * math.cos(theta)
	return xp, yp

def rot90(x, y):
	xp = -y
	yp = x
	return xp, yp

def rot180(x, y):
	xp = -x
	yp = -y
	return xp, yp

def rot270(x, y):
	xp = y
	yp = -x
	return xp, yp

print(rot90(2, 1))
print(rot180(2, 1))
print(rot270(2, 1))