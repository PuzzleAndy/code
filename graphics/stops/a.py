# License: CC0
# https://puzzleandy.com

# pip install numpy

import math
import numpy as np

def lerp(a, b, t):
	return (1 - t) * a + t * b

class ColStop:
	def __init__(self, loc, col):
		self.loc = loc
		self.col = col

class AlphaStop:
	def __init__(self, loc, alpha):
		self.loc = loc
		self.alpha = alpha

col_stops = [
	ColStop(0, np.array([0, 0, 0])),
	ColStop(1, np.array([1, 1, 1])),
]
col_mids = [0.25]
alpha_stops = [
	AlphaStop(0, 1),
	AlphaStop(1, 1)
]
alpha_mids = [0.5]

loc = 0.25

if loc < col_stops[0].loc:
	col = col_stops[0].col
elif loc > col_stops[-1].loc:
	col = col_stops[-1].col
else:
	for i in range(0, len(col_stops) - 1):
		if col_stops[i].loc < loc and loc < col_stops[i + 1].loc:
			t = (loc - col_stops[i].loc) / (col_stops[i + 1].loc - col_stops[i].loc)
			u = t**(math.log(0.5) / math.log(col_mids[i]))
			col = lerp(col_stops[i].col, col_stops[i + 1].col, u)
			print(col)
			break

if loc < alpha_stops[0].loc:
	alpha = alpha_stops[0].alpha
elif loc > alpha_stops[-1].loc:
	alpha = alpha_stops[-1].alpha
else:
	for i in range(0, len(alpha_stops) - 1):
		if alpha_stops[i].loc < loc and loc < alpha_stops[i + 1].loc:
			t = (loc - alpha_stops[i].loc) / (alpha_stops[i + 1].loc - alpha_stops[i].loc)
			u = t**(math.log(0.5) / math.log(alpha_mids[i]))
			alpha = lerp(alpha_stops[i].alpha, alpha_stops[i + 1].alpha, u)
			print(alpha)
			break