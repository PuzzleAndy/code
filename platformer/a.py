import pyglet
from pyglet import shapes
import numpy as np
import ctypes
from pyglet.window import key
import math

ctypes.windll.shcore.SetProcessDpiAwareness(2)

left = np.array([-1, 0], np.float32)
right = np.array([1, 0], np.float32)
up = np.array([0, 1], np.float32)
down = np.array([0, -1], np.float32)

class Line:

	def __init__(self, x1, y1, x2, y2):
		self.p1 = np.array([x1, y1], np.float32)
		self.p2 = np.array([x2, y2], np.float32)

	def is_hor(self):
		return self.p1[1] == self.p2[1]

class Rect:

	def __init__(self, cx, cy, hx, hy):
		self.c = np.array([cx, cy], np.float32)
		self.h = np.array([hx, hy], np.float32)

class Hero:

	def __init__(self, cx, cy, hx, hy):
		self.shape = shapes.Rectangle(cx - hx, cy - hy, cx + hx, cy + hy)
		self.rect = Rect(cx, cy, hx, hy)
		self.pos = np.array([cx, cy], np.float32)
		self.vel = np.array([0, 0], np.float32)

class Edge:

	def __init__(self, x1, y1, x2, y2):
		self.shape = shapes.Line(x1, y1, x2, y2)
		self.line = Line(x1, y1, x2, y2)

wnd = pyglet.window.Window(500, 500)
keys = key.KeyStateHandler()
wnd.push_handlers(keys)
hero = Hero(15, 15, 15, 15)
edges = [
	Edge(0, 0, 500, 0),
	Edge(250, 100, 500, 100),
]

def rect_hor_line_hit(rect, line):
	line_min_x = min(line.p1[0], line.p2[0])
	line_max_x = max(line.p1[0], line.p2[0])
	if rect.c[0] + rect.h[0] <= line_min_x:
		return False
	if rect.c[0] - rect.h[0] >= line_max_x:
		return False
	if rect.c[1] - rect.h[1] >= line.p1[1]:
		return False
	if rect.c[1] + rect.h[1] <= line.p1[1]:
		return False
	return True

def rect_hor_line_sep(rect, line):
	line_min_x = min(line.p1[0], line.p2[0])
	line_max_x = max(line.p1[0], line.p2[0])
	dist = [
		(rect.c[0] + rect.h[0]) - line_min_x,
		line_max_x - (rect.c[0] - rect.h[0]),
		line.p1[1] - (rect.c[1] - rect.h[1]),
		(rect.c[1] + rect.h[1]) - line.p1[1]
	]
	direct = [left, right, up, down]
	min_dist = min(dist)
	min_direct = direct[dist.index(min_dist)]
	return min_dist, min_direct

@wnd.event
def on_draw():
	global x, y
	wnd.clear()

	if keys[key.A]:
		hero.rect.c[0] -= 3
	if keys[key.D]:
		hero.rect.c[0] += 3
	if keys[key.W] and hero.vel[1] == 0:
		hero.vel[1] = 14

	hero.vel[1] -= 1
	hero.rect.c[1] += hero.vel[1]

	for i in range(0, 10):
		min_dist = math.inf
		min_direct = None
		for edge in edges:
			dist = None
			if edge.line.is_hor():
				if rect_hor_line_hit(hero.rect, edge.line):
					dist, direct = rect_hor_line_sep(hero.rect, edge.line)
			if dist is not None:
				if dist < min_dist:
					min_dist = dist
					min_direct = direct
		if min_dist == math.inf:
			break
		hero.rect.c += min_dist * min_direct
		if (min_direct == left).all() or (min_direct == right).all():
			hero.vel[0] = 0
		if (min_direct == up).all() or (min_direct == down).all():
			hero.vel[1] = 0

	hero.shape.position = hero.rect.c - hero.rect.h
	hero.shape.draw()
	for edge in edges:
		edge.shape.draw()

pyglet.app.run()