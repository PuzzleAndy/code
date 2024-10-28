# License: CC0
# https://puzzleandy.com

def lerp(p0, p1, x):
	return (1 - x) * p0 + x * p1

def bilerp(
	p00, p10, p01, p11,
	x, y):
	q0 = lerp(p00, p10, x)
	q1 = lerp(p01, p11, x)
	return lerp(q0, q1, y)

def trilerp(
	p000, p100, p010, p110,
	p001, p101, p011, p111,
	x, y, z):
	q0 = bilerp(p000, p100, p010, p110, x, y)
	q1 = bilerp(p001, p101, p011, p111, x, y)
	return lerp(q0, q1, z)

# 0 4
#  3
lerp(0, 4, 0.75)

# 0  4  8  12
#   3    11
#      7
bilerp(0, 4, 8, 12, 0.75, 0.50)

# 0  4  8  12  16  20  24  28
#   3    11      19      27
#      7             23
#            11
trilerp(0, 4, 8, 12, 16, 20, 24, 28, 0.75, 0.50, 0.25)