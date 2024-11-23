import cairo
import math
import sys

# Border width
border = 40

# Distance between points
dist = 100

# Radius of each point
radius = 10

# Number of rows and columns
rows = 4
cols = 6

# Image dimensions
w = (cols - 1) * dist + radius * 2 + border * 2
h = (rows - 1) * dist + radius * 2 + border * 2

# Stroke and fill flags
stroke_on = True
fill_on = False

# Stroke and fill colors
stroke = (1., 1., 1., 1.)
fill = (0., 0., 0., 0.)

# Draw the grid
with cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) as sfc:
	ctx = cairo.Context(sfc)
	y = border + radius
	for i in range(0, rows):
		x = border + radius
		for j in range(0, cols):
			ctx.arc(x, y, radius, 0, 2 * math.pi)
			if fill_on:
				ctx.set_source_rgba(*fill)
				ctx.fill()
			if stroke_on:
				ctx.set_source_rgba(*stroke)
				ctx.stroke()
			x += dist
		y += dist
	sfc.write_to_png('grid.png')