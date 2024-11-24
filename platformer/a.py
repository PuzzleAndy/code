# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install pyglet

import numpy as np
import pyglet
from pyglet import shapes
import ctypes
from pyglet.window import key
import math

ctypes.windll.shcore.SetProcessDpiAwareness(2)

def perp(v):
	return (v[1], -v[0])

def norm(v):
	return v / np.linalg.norm(v)

left = np.array([-1, 0], np.float32)
right = np.array([1, 0], np.float32)
up = np.array([0, 1], np.float32)
down = np.array([0, -1], np.float32)

# shapes

class Circ:

	def __init__(self, cx, cy, r):
		self.c = np.array([cx, cy], np.float32)
		self.r = r

class HorLine:

	def __init__(self, cx, cy, hx):
		self.c = np.array([cx, cy], np.float32)
		self.hx = hx

class VertLine:

	def __init__(self, cx, cy, hy):
		self.c = np.array([cx, cy], np.float32)
		self.hy = hy

class Rect:

	def __init__(self, cx, cy, hx, hy):
		self.c = np.array([cx, cy], np.float32)
		self.h = np.array([hx, hy], np.float32)

	def p(self):
		return [
			self.c + (-self.h[0], -self.h[1]),
			self.c + (self.h[0], -self.h[1]),
			self.c + (self.h[0], self.h[1]),
			self.c + (-self.h[0], self.h[1])
		]

class Tri:

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.p = np.array([(x1, y1), (x2, y2), (x3, y3)], np.float32)

# hero.py

class Hero:

	def __init__(self, cx, cy, hx, hy):
		self.shape = shapes.Rectangle(cx - hx, cy - hy, cx + hx, cy + hy)
		self.rect = Rect(cx, cy, hx, hy)
		self.pos = np.array([cx, cy], np.float32)
		self.vel = np.array([0, 0], np.float32)
		self.on_ground = False
		self.is_alive = True

class Saw:

	def __init__(self, cx, cy, r):
		self.shape = shapes.Circle(cx, cy, r)
		self.circ = Circ(cx, cy, r)

class Spike:

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.shape = shapes.Triangle(x1, y1, x2, y2, x3, y3)
		self.tri = Tri(x1, y1, x2, y2, x3, y3)

# plat.py

class HorLinePlat:

	def __init__(self, x1, x2, y):
		self.shape = shapes.Line(x1, y, x2, y)
		cx = (x1 + x2) / 2
		hx = abs((x2 - x1) / 2)
		self.line = HorLine(cx, y, hx)

class VertLinePlat:

	def __init__(self, x, y1, y2):
		self.shape = shapes.Line(x, y1, x, y2)
		cy = (y1 + y2) / 2
		hx = abs((y2 - y1) / 2)
		self.line = VertLine(x, cy, hy)

wnd = pyglet.window.Window(500, 500)
keys = key.KeyStateHandler()
wnd.push_handlers(keys)
hero = Hero(15, 15, 15, 15)
enemies = [
	Saw(200, 0, 50),
	Spike(420, 100, 440, 100, 430, 130)
]
plats = [
	HorLinePlat(0, 500, 0),
	HorLinePlat(250, 500, 100)
]

class Proj:

	def __init__(self, p, axis):
		self.mini = math.inf
		self.maxi = -math.inf
		for i in range(len(p)):
			proj = p[i].dot(axis)
			self.mini = min(proj, self.mini)
			self.maxi = max(proj, self.maxi)

def projs_overlap(proj1, proj2):
	if proj1.maxi < proj2.mini:
		return False
	if proj1.mini > proj2.maxi:
		return False
	return True

def rect_tri_hit(rect, tri):
	axes = np.empty((5, 2), np.float32)
	axes[0] = (1, 0)
	axes[1] = (0, 1)
	for i in range(3):
		axes[i + 2] = perp(norm(tri.p[(i + 1) % 3] - tri.p[i]))
	for axis in axes:
		rect_proj = Proj(rect.p(), axis)
		tri_proj = Proj(tri.p, axis)
		if not projs_overlap(rect_proj, tri_proj):
			return False
	return True

def closest_on_rect_to_circ(rect, circ):
	rect_min_x = rect.c[0] - rect.h[0]
	rect_min_y = rect.c[1] - rect.h[1]
	rect_max_x = rect.c[0] + rect.h[0]
	rect_max_y = rect.c[1] + rect.h[1]
	return np.array([
		np.clip(circ.c[0], rect_min_x, rect_max_x),
		np.clip(circ.c[1], rect_min_y, rect_max_y)
	], np.float32)
	
def dist(pt1, pt2):
	return np.linalg.norm(pt2 - pt1)

def rect_circ_hit(rect, circ):
	pt = closest_on_rect_to_circ(rect, circ)
	return dist(circ.c, pt) < circ.r
	
def rect_hor_line_hit(rect, line):
	line_min_x = line.c[0] - line.hx
	line_max_x = line.c[0] + line.hx
	rect_min_x = rect.c[0] - rect.h[0]
	rect_min_y = rect.c[1] - rect.h[1]
	rect_max_x = rect.c[0] + rect.h[0]
	rect_max_y = rect.c[1] + rect.h[1]
	
	if rect_max_x <= line_min_x:
		return False
	if rect_min_x >= line_max_x:
		return False
	if rect_min_y >= line.c[1]:
		return False
	if rect_max_y <= line.c[1]:
		return False
	return True

def rect_hor_line_sep(rect, line):
	line_min_x = line.c[0] - line.hx
	line_max_x = line.c[0] + line.hx
	rect_min_x = rect.c[0] - rect.h[0]
	rect_min_y = rect.c[1] - rect.h[1]
	rect_max_x = rect.c[0] + rect.h[0]
	rect_max_y = rect.c[1] + rect.h[1]
	min_dist = math.inf

	dist = rect_max_x - line_min_x
	if dist < min_dist:
		min_dist = dist
		min_direct = left

	dist = line_max_x - rect_min_x
	if dist < min_dist:
		min_dist = dist
		min_direct = right

	dist = line.c[1] - rect_min_y
	if dist < min_dist:
		min_dist = dist
		min_direct = up
	
	dist = rect_max_y - line.c[1]
	if dist < min_dist:
		min_dist = dist
		min_direct = down

	return min_dist, min_direct

def step(dt):

	if not hero.is_alive:
		return

	hero.vel[0] = 0
	if keys[key.A]:
		hero.vel[0] = -400
	if keys[key.D]:
		hero.vel[0] = 400
	if keys[key.W] and hero.on_ground:
		hero.vel[1] = 1300

	hero.vel[1] -= 18
	hero.rect.c += hero.vel * dt

	for enemy in enemies:
		if type(enemy) is Saw:
			if rect_circ_hit(hero.rect, enemy.circ):
				hero.is_alive = False
		elif type(enemy) is Spike:
			if rect_tri_hit(hero.rect, enemy.tri):
				hero.is_alive = False

	hero.on_ground = False
	for i in range(0, 10):
		min_dist = math.inf
		min_direct = None
		for plat in plats:
			dist = None
			if type(plat) is HorLinePlat:
				if rect_hor_line_hit(hero.rect, plat.line):
					dist, direct = rect_hor_line_sep(hero.rect, plat.line)
			if dist is not None:
				if dist < min_dist:
					min_dist = dist
					min_direct = direct
		if min_dist == math.inf:
			break
		hero.rect.c += min_dist * min_direct
		if (min_direct == left).all() or (min_direct == right).all():
			hero.vel[0] = 0
		if (min_direct == up).all():
			if hero.vel[1] <= 0:
				hero.on_ground = True
			hero.vel[1] = 0
		if (min_direct == down).all():
			hero.vel[1] = 0

@wnd.event
def on_draw():
	wnd.clear()

	dt = (1 / 60) / 5
	for i in range(0, 5):
		step(dt)

	hero.shape.position = hero.rect.c - hero.rect.h
	if hero.is_alive:
		hero.shape.draw()
	for enemy in enemies:
		enemy.shape.draw()
	for plat in plats:
		plat.shape.draw()

pyglet.app.run()