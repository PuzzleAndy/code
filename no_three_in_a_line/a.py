# License: CC0
# https://puzzleandy.com

# pip install pyglet
# pip install numpy

import pyglet
from pyglet import shapes
from pyglet.gl import Config
import numpy as np
from itertools import combinations
import math
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Border width
border = 50

# Distance between points
dist = 150

# Radius of each point
radius = 13

# Number of columns
cols = 5

# Window dimensions
w = (cols - 1) * dist + radius * 2 + border * 2
h = math.ceil((cols - 1) * dist * math.sqrt(3) / 2 + radius * 2 + border * 2)

# Are a, b, c collinear?
EPS = 0.001
def are_collinear(a, b, c):
	return abs(np.cross(b - a, c - a)) < EPS

config = Config(sample_buffers=1, samples=4, double_buffer=True)
try:
	config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True, )
	wnd = pyglet.window.Window(w, h, config=config)
except pyglet.window.NoSuchConfigException:
	wnd = pyglet.window.Window(w, h)

class Hole:
	def __init__(self, pt, circle):
		self.pt = pt
		self.circle = circle
		self.is_filled = False

holes = []

y = h - (border + radius)
for i in range(0, cols):
	x = w / 2 - dist / 2 * i
	for j in range(0, i + 1):
		pt = np.array([x, y])
		circle = shapes.Circle(x, y, radius, color=(75, 75, 75))
		holes.append(Hole(pt, circle))
		x += dist
	y -= dist * math.sqrt(3) / 2

@wnd.event
def on_draw():
	global holes
	wnd.clear()
	for hole in holes:
		hole.circle.draw()

@wnd.event
def on_mouse_press(x, y, button, modifiers):
	global holes
	pt = np.array([x, y])
	for hole in holes:
		if hole.is_filled:
			hole.circle.color = (0, 255, 0)
	for hole in holes:
		if np.linalg.norm(hole.pt - pt) <= radius:
			if not hole.is_filled:
				hole.is_filled = True
				hole.circle.color = (0, 255, 0)
				break
			else:
				hole.is_filled = False
				hole.circle.color = (75, 75, 75)

	filled_holes = []
	for hole in holes:
		if hole.is_filled:
			filled_holes.append(hole)

	for triple in combinations(filled_holes, 3):
		if are_collinear(triple[0].pt, triple[1].pt, triple[2].pt):
			triple[0].circle.color = (255, 0, 0)
			triple[1].circle.color = (255, 0, 0)
			triple[2].circle.color = (255, 0, 0)

pyglet.app.run()