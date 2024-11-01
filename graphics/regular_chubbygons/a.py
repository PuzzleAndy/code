import cairo
import math
import numpy as np

# Image dimensions
w = 500
h = 500

# Number of sides for the regular chubbygon
n = 3

# Radius of the inscribed regular polygon
r = 100

# Distance from the regular polygon's center
# to the center of each circular arc
d = 100

# Center of the regular chubbygon
c = np.array([w / 2, h / 2])

with cairo.ImageSurface(cairo.FORMAT_RGB24, 500, 500) as sfc:
	ctx = cairo.Context(sfc)
	ctx.set_line_width(2)
	ctx.set_source_rgba(1, 1, 1, 1)

	# Supplementary angles, where alpha is half the
	# interior angle of the inscribed regular polygon
	alpha = math.pi / n
	beta = math.pi - alpha

	# Radius of the regular chubbygon
	R = math.sqrt(r**2 + d**2 - 2 * r * d * math.cos(beta))

	# Half the difference between the initial
	# and final angles of the circular arc
	gamma = math.acos((d**2 + R**2 - r**2) / (2 * d * R))

	# Initial and final angles of the circular arc
	start = end = None
	if n % 2 == 0:
		start = math.pi + alpha - gamma
		end = math.pi + alpha + gamma
	else:
		start = math.pi - gamma
		end = math.pi + gamma

	# For each side of the regular chubbygon
	delta = 0
	for i in range(0, n):

		# Center of the circular arc
		c2 = np.empty(2)
		if n % 2 == 0:
			c2[0] = c[0] + d * math.cos(delta + alpha)
			c2[1] = c[1] + d * math.sin(delta + alpha)
		else:
			c2[0] = c[0] + d * math.cos(delta)
			c2[1] = c[1] + d * math.sin(delta)

		# Draw the circular arc
		ctx.arc(c2[0], c2[1], R, delta + start, delta + end)

		# Rotate to the next side of the regular chubbygon
		delta += math.tau / n

	ctx.stroke()
	sfc.write_to_png('chubbygon.png')