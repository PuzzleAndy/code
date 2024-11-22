from pyglet import *

w = 600
h = 600

wnd = window.Window(w, h)
img = image.load('motorcycle.jpg')
sprite = sprite.Sprite(img, x=0, y=0)
sprite.scale = 0.01
sprite.scale = 10
print(sprite.width)
scale = 0.1
min_scale = 0.05
@wnd.event
def on_draw():
	global scale
	sprite.scale = scale
	sprite.x = wnd.width / 2 - sprite.width / 2
	sprite.y = wnd.height / 2 - sprite.height / 2
	wnd.clear()
	sprite.draw()

@wnd.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
	global scale
	scale += scroll_y / 20
	if scale <= min_scale:
		scale -= scroll_y / 20

app.run()