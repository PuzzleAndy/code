# License: CC0
# https://puzzleandy.com

# pip install pygame
# pip install numpy

import math
import pygame
import numpy as np

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

pygame.init()
screen = pygame.display.set_mode((200, 200))
H = 0
clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit
	rgb = hue2rgb(H)
	screen.fill(list(np.array(rgb) * 255))
	pygame.display.flip()
	H = (H + 0.85) % 360
	clock.tick(60)