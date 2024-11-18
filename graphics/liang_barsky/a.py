# License: CC0
# https://puzzleandy.com

def clamp(x, mini=0, maxi=1):
	return min(max(x, mini), maxi)

# Liang-Barsky
def clip(xmin, ymin, xmax, ymax, x1, y1, x2, y2):

	dx = x2 - x1
	dy = y2 - y1
	p = [-dx, dx, -dy, dy]
	q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
	u1 = 0
	u2 = 1

	# If line parallel to AABB
	if p[0] == 0 or p[2] == 0:
		# If line completely outside AABB
		if any(qi < 0 for qi in q):
			return None, None, None, None
		# Else line at least partially inside AABB
		else:
			x3 = clamp(x1, xmin, xmax)
			y3 = clamp(y1, ymin, ymax)
			x4 = clamp(x2, xmin, xmax)
			y4 = clamp(y2, ymin, ymax)

	# For each edge
	for i in range(4):
		t = q[i] / p[i]
		# If line proceeds outside to inside AABB
		if p[i] < 0:
			u1 = max(u1, t)
			if u1 > u2:
				return None
		# Else line proceeds inside to outside AABB
		else:
			u2 = min(u2, t)
			if u1 > u2:
				return None

	x3 = x1 + u1 * dx
	y3 = y1 + u1 * dy
	x4 = x1 + u2 * dx
	y4 = y1 + u2 * dy

	return x3, y3, x4, y4

print(clip(0, 0, 4, 4, 0, -2, 2, 2))