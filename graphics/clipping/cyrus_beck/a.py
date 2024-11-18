# License: CC0
# https://puzzleandy.com

# pip install numpy

import numpy as np

def rot270(a):
	return np.array([a[1], -a[0]], np.float32)

def clip(P1, P2, V):

	t1 = 0
	t2 = 1

	# For each edge
	for i in range(len(V)):

		Pt = P1
		Q = V[i]
		
		j = (i + 1) % len(V)
		N = rot270(V[j] - V[i])

		num = np.dot(N, Pt - Q)
		den = np.dot(N, P2 - P1)

		# If line is point or parallel to edge
		if den == 0:
			# If line outside
			if num > 0:
				return None, None, None, None
		else:
			t = -num / den
			# If entering
			if den < 0:
				if t <= 1:
					t1 = max(t, t1)
					if t1 > t2:
						return None, None
			# Else exiting
			else:
				if t >= 0:
					t2 = min(t, t2)
					if t1 > t2:
						return None, None

	P3 = P1 + t1 * (P2 - P1)
	P4 = P1 + t2 * (P2 - P1)

	return P3, P4

P1 = np.array([0, -2], np.float32)
P2 = np.array([2, 2], np.float32)
V = np.array([(0, 0), (4, 0), (4, 4), (0, 4)], np.float32)
P3, P4 = clip(P1, P2, V)
print(P3[0], P3[1], P4[0], P4[1])