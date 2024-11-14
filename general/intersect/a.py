# pip install shapely

from shapely.geometry import Polygon
from shapely import box
import pyglet

wnd = pyglet.window.Window()

@wnd.event
def on_draw():
	wnd.clear()

rect = box(0, 0, 1, 1)
tri = Polygon([(0,1), (1,0), (1,1)])
print(tri.intersects(rect))
pyglet.app.run()