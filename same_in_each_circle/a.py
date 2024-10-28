import pyglet
from pyglet import shapes
from pyglet.gl import Config
import numpy as np
import ctypes
import math

ctypes.windll.shcore.SetProcessDpiAwareness(True)

is_down = False

dot_r = 10
circle_col = (245, 245, 245)
dot_col = (210, 210, 210)

class Circle:
	def __init__(self, cx, cy, r, lx, ly):
		self.c = np.array([cx, cy])
		self.r = r
		self.arc = shapes.Arc(cx, cy, r, thickness=2, color=circle_col)
		self.label = pyglet.text.Label(
			'0',
			font_name='Times New Roman',
			font_size=24,
			x=cx + lx, y=cy + ly,
			anchor_x='center', anchor_y='center')

class Dot:
	def __init__(self, cx, cy, r):
		self.c = np.array([cx, cy])
		self.r = r
		self.circle = shapes.Circle(cx, cy, r, color=dot_col)

w = 780
h = 610
config = Config(sample_buffers=1, samples=4, double_buffer=True)
try:
	config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True, )
	wnd = pyglet.window.Window(w, h, config=config)
except pyglet.window.NoSuchConfigException:
	wnd = pyglet.window.Window(w, h)

circles = []
circles.append(Circle(150, 280, 100, 0, 130))
circles.append(Circle(270, 190, 100, 0, -130))
circles.append(Circle(390, 280, 100, 0, 130))
circles.append(Circle(510, 190, 100, 0, -130))
circles.append(Circle(630, 280, 100, 0, 130))

num_first_row = 8
dots = []
dist = (630 - 150 + 100 * 2 - dot_r * 2) / (num_first_row - 1)
x1 = 50 + dot_r
y1 = 545 + dot_r
x2 = x1 + dist / 2
y2 = y1 - 50
for i in range(0, num_first_row):
	dots.append(Dot(x1 + dist * i, y1, dot_r))
for i in range(0, num_first_row - 1):
	dots.append(Dot(x2 + dist * i, y2, dot_r))

selection = None

@wnd.event
def on_mouse_press(x, y, button, modifiers):
	global is_down, selection
	is_down = True
	pt = np.array([x, y])
	selection = None
	for dot in dots:
		if np.linalg.norm(pt - dot.c) <= dot.r:
			selection = dot
			print('selected!')
			break

@wnd.event
def on_mouse_release(x, y, button, modifiers):
	global is_down, selection
	is_down = False
	selection = None

@wnd.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
	global selection
	if selection:
		selection.c += np.array([dx, dy])
		selection.circle.x += dx
		selection.circle.y += dy
		for circle in circles:
			count = 0
			for dot in dots:
				if np.linalg.norm(dot.c - circle.c) <= circle.r:
					count += 1
			circle.label.text = str(count)

@wnd.event
def on_draw():
	global holes
	wnd.clear()
	for circle in circles:
		circle.arc.draw()
		circle.label.draw()
	for dot in dots:
		dot.circle.draw()

pyglet.app.run()