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
	X = (1 - abs(Hp % 2 - 1))
	R1, G1, B1 = (None, None, None)
	if 0 <= Hp < 1:
		R1, G1, B1 = 1, X, 0
	elif 1 <= Hp < 2:
		R1, G1, B1 = X, 1, 0
	elif 2 <= Hp < 3:
		R1, G1, B1 = 0, 1, X
	elif 3 <= Hp < 4:
		R1, G1, B1 = 0, X, 1
	elif 4 <= Hp < 5:
		R1, G1, B1 = X, 0, 1
	elif 5 <= Hp < 6:
		R1, G1, B1 = 1, 0, X
	return np.array([R1, G1, B1])

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
	screen.fill(list(rgb * 255))
	pygame.display.flip()
	H = (H + 0.85) % 360
	clock.tick(60)