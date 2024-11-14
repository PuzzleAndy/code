# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install matplotlib

import math
from matplotlib import pyplot as plt
import numpy as np

def pow2(n):
	return 2 ** n

def odd(n):
	return 2 * n + 1

def is_even(n):
	return n % 2 == 0

# f is increasing
# the domain of f is N
# the image of f is [f(0), inf)
def inc_nat_floor(f, x):
	prev = f(0)
	if x < prev:
		return None
	if x == prev:
		return prev
	i = 1
	while True:
		y = f(i)
		if x <= y:
			return prev
		prev = y
		i += 1

# f is increasing
# the domain of f is N
# the image of f is [f(0), inf)
def inc_nat_ceil(f, x):
	prev = f(0)
	if x <= prev:
		return prev
	i = 1
	while True:
		y = f(i)
		if x <= y:
			return y
		prev = y
		i += 1

# f is increasing
# the domain of f is Z
# the image of f is (-inf, inf)
def inc_int_floor(f, x):
	prev = f(0)
	if x == prev:
		return prev
	if x > prev:
		i = 1
		while True:
			y = f(i)
			if x <= y:
				return prev
			prev = y
			i += 1
	else:
		i = -1
		while True:
			y = f(i)
			if x >= y:
				return y
			prev = y
			i -= 1

# f is increasing
# the domain of f is Z
# the image of f is (-inf, inf)
def inc_int_ceil(f, x):
	prev = f(0)
	if x == prev:
		return prev
	if x > prev:
		i = 1
		while True:
			y = f(i)
			if x <= y:
				return y
			prev = y
			i += 1
	else:
		i = -1
		while True:
			y = f(i)
			if x >= y:
				return prev
			prev = y
			i -= 1

def pow2_floor(x):
	return inc_nat_floor(pow2, x)

def pow2_ceil(x):
	return inc_nat_ceil(pow2, x)

def odd_floor(x):
	return inc_int_floor(odd, x)

def odd_ceil(x):
	return inc_int_ceil(odd, x)

x = np.linspace(0, 16, 100)
y1 = np.vectorize(pow2_ceil, otypes=[float])(x)
y2 = np.vectorize(pow2_floor, otypes=[float])(x)
plt.clf()
plt.plot(x, y1, color='red', label='ceil')
plt.plot(x, y2, color='blue', label='floor')
plt.legend(loc='best')
plt.savefig('pow2.png')

x = np.linspace(-5, 5, 100)
y1 = np.vectorize(odd_ceil, otypes=[float])(x)
y2 = np.vectorize(odd_floor, otypes=[float])(x)
plt.clf()
plt.plot(x, y1, color='red', label='ceil')
plt.plot(x, y2, color='blue', label='floor')
plt.legend(loc='best')
plt.savefig('odd.png')