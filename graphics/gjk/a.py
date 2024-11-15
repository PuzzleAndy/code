# License: CC0
# https://puzzleandy.com

# pip install numpy

import numpy as np
import math
import random

class Polygon:

	def __init__(self, vertices):
		self.vertices = vertices

	def support(self, direction):
		furthestDistance = float('-inf')
		furthestVertex = None
		for v in self.vertices:
			distance = np.dot(v, direction)
			if distance > furthestDistance:
				furthestDistance = distance
				furthestVertex = v

		return furthestVertex

class Circle:

	def __init__(self, center, radius):
		self.center = center
		self.radius = radius

	def support(self, direction):
		return self.center + self.radius * (direction / np.linalg.norm(direction))

NO_INTERSECTION = 0
FOUND_INTERSECTION = 1
STILL_EVOLVING = 2

def tripleProduct(a, b, c):
	return np.array([
		a[1] * (b[0] * c[1] - b[1] * c[0]),
		a[0] * (b[1] * c[0] - b[0] * c[1])
	], np.float32)

def f():
	vertices = np.empty((0, 2), np.float32)
	direction = np.empty(2, np.float32)
	shapeA = Polygon(np.array([(0, 0), (1, 0), (1, 1)], np.float32))
	shapeB = Circle(np.array([5, 0], np.float32), 2)

	while True:
		if len(vertices) == 0:
			theta = random.random() * math.tau
			direction = np.array([math.cos(theta), math.sin(theta)])
		elif len(vertices) == 1:
			direction = -direction
		elif len(vertices) == 2:
			b = vertices[1]
			c = vertices[0]

			# line cb is the line formed by the first two vertices
			cb = b - c;
			# line c0 is the line from the first vertex to the origin
			c0 = -c

			# use the triple-cross-product to calculate a direction perpendicular
			# to line cb in the direction of the origin
			direction = tripleProduct(cb, c0, cb)

		else:
			# calculate if the simplex contains the origin
			a = vertices[2]
			b = vertices[1]
			c = vertices[0]

			a0 = a * -1 # v2 to the origin
			ab = b - a  # v2 to v1
			ac = c - a  # v2 to v0

			abPerp = tripleProduct(ac, ab, ab)
			acPerp = tripleProduct(ab, ac, ac)

			if np.dot(abPerp, a0) > 0:
				# the origin is outside line ab
				# get rid of c and add a new support in the direction of abPerp
				vertices = np.delete(vertices, 0)
				direction = abPerp

			elif np.dot(acPerp, a0) > 0:
				# the origin is outside line ac
				# get rid of b and add a new support in the direction of acPerp
				vertices = np.delete(vertices, 1)
				direction = acPerp

			else:
				# the origin is inside both ab and ac,
				# so it must be inside the triangle!
				return True

		if not np.any(direction):
			return True
		newVertex = shapeA.support(direction) - shapeB.support(-direction)
		vertices = np.vstack([vertices, newVertex])
		if np.dot(direction, newVertex) <= 0:
			return False

print(f())