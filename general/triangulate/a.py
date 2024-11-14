# License: CC0
# https://puzzleandy.com

# pip install panda3d
# pip install pyglet

from panda3d.core import Triangulator
import pyglet
from pyglet.gl import *
from pyglet.math import Mat4
from pyglet import shapes
import ctypes

w = 500
h = 500

ctypes.windll.shcore.SetProcessDpiAwareness(True)

config = Config(sample_buffers=1, samples=4, double_buffer=True)
try:
	config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True, )
	wnd = pyglet.window.Window(w, h, config=config)
except pyglet.window.NoSuchConfigException:
	wnd = pyglet.window.Window(w, h)

triangulator = Triangulator()
verts = [
	(0, 0), (2, 1), (0, 2), (1, 1)
]
for i in range(0, len(verts)):
	triangulator.add_vertex(verts[i])
	triangulator.add_polygon_vertex(i)
triangulator.triangulate()
tris = []
for i in range(0, triangulator.get_num_triangles()):
	v0 = triangulator.get_vertex(triangulator.get_triangle_v0(i))
	v1 = triangulator.get_vertex(triangulator.get_triangle_v1(i))
	v2 = triangulator.get_vertex(triangulator.get_triangle_v2(i))
	tris.append(shapes.Triangle(
		v0[0], v0[1],
		v1[0], v1[1],
		v2[0], v2[1]))

@wnd.event
def on_draw():
	global tris
	wnd.clear()
	wnd.projection = Mat4.orthogonal_projection(
		0, 3, 0, 3, -1, 1
	)
	for tri in tris:
		tri.draw()

pyglet.app.run()