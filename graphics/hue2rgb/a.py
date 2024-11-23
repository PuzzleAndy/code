# License: CC0
# https://puzzleandy.com

# pip install pygame
# pip install numpy

import math
import pyglet
import numpy as np
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

def hue2rgb(H):
	C = 1
	Hp = H / 60
	X = 1 - abs(Hp % 2 - 1)
	R, G, B = None, None, None
	if 0 <= Hp < 1:
		R, G, B = 1, X, 0
	elif 1 <= Hp < 2:
		R, G, B = X, 1, 0
	elif 2 <= Hp < 3:
		R, G, B = 0, 1, X
	elif 3 <= Hp < 4:
		R, G, B = 0, X, 1
	elif 4 <= Hp < 5:
		R, G, B = X, 0, 1
	elif 5 <= Hp < 6:
		R, G, B = 1, 0, X
	return R, G, B

H = 0
wnd = pyglet.window.Window(500, 500)

@wnd.event
def on_draw():
	global H
	RGB = hue2rgb(H)
	pyglet.gl.glClearColor(RGB[0], RGB[1], RGB[2],1)
	H = (H + 0.85) % 360
	wnd.clear()

pyglet.app.run()