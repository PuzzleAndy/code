import math
from matplotlib import pyplot as plt
import numpy as np

def ease_in_sine(x):
	return 1 - math.cos((x * math.pi) / 2)

def ease_out_sine(x):
	return math.sin((x * math.pi) / 2)

def ease_in_out_sine(x):
	return -(math.cos(math.pi * x) - 1) / 2

def ease_in_quad(x):
	return x * x

def ease_out_quad(x):
	return 1 - (1 - x) * (1 - x)

def ease_in_out_quad(x):
	if x < 0.5:
		return 2 * x * x
	else:
		return 1 - math.pow(-2 * x + 2, 2) / 2

def ease_in_cubic(x):
	return x * x * x

def ease_out_cubic(x):
	return 1 - math.pow(1 - x, 3)

def ease_in_out_cubic(x):
	if x < 0.5:
		return 4 * x * x * x
	else:
		return 1 - math.pow(-2 * x + 2, 3) / 2

def ease_in_quart(x):
	return x * x * x * x

def ease_out_quart(x):
	return 1 - math.pow(1 - x, 4)

def ease_in_out_quart(x):
	if x < 0.5:
		return 8 * x * x * x * x
	else:
		return 1 - math.pow(-2 * x + 2, 4) / 2

def ease_in_quint(x):
	return x * x * x * x * x

def ease_out_quint(x):
	return 1 - math.pow(1 - x, 5)

def ease_in_out_quint(x):
	if x < 0.5:
		return 16 * x * x * x * x * x
	else:
		return 1 - math.pow(-2 * x + 2, 5) / 2

def ease_in_expo(x):
	if x == 0:
		return 0
	else:
		return math.pow(2, 10 * x - 10)

def ease_out_expo(x):
	if x == 1:
		return 1
	else:
		return 1 - math.pow(2, -10 * x)

def ease_in_out_expo(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	elif x < 0.5:
		return math.pow(2, 20 * x - 10) / 2
	else:
		return (2 - math.pow(2, -20 * x + 10)) / 2

def ease_in_circ(x):
	return 1 - math.sqrt(1 - math.pow(x, 2))

def ease_out_circ(x):
	return math.sqrt(1 - math.pow(x - 1, 2))

def ease_in_out_circ(x):
	if x < 0.5:
		return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2
	else:
		return (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2

def ease_in_back(x):
	c1 = 1.70158
	c3 = c1 + 1
	return c3 * x * x * x - c1 * x * x

def ease_out_back(x):
	c1 = 1.70158
	c3 = c1 + 1
	return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

def ease_in_out_back(x):
	c1 = 1.70158
	c2 = c1 * 1.525
	if x < 0.5:
		return (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2
	else:
		return (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2

def ease_in_elastic(x):
	c4 = (2 * math.pi) / 3
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)

def ease_out_elastic(x):
	c4 = (2 * math.pi) / 3
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

def ease_in_out_elastic(x):
	c5 = (2 * math.pi) / 4.5
	if x == 0:
		return 0
	elif x == 1:
		return 1
	elif x < 0.5:
		return -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2
	else:
		return (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1

def ease_in_bounce(x):
	return 1 - ease_out_bounce(1 - x)

def ease_out_bounce(x):
	n1 = 7.5625
	d1 = 2.75
	if x < 1 / d1:
		return n1 * x * x
	elif x < 2 / d1:
		return n1 * math.pow(x - 1.5 / d1, 2) + 0.75
	elif x < 2.5 / d1:
		return n1 * math.pow(x - 2.25 / d1, 2) + 0.9375
	else:
		return n1 * math.pow(x - 2.625 / d1, 2) + 0.984375

def ease_in_out_bounce(x):
	if x < 0.5:
		return (1 - ease_out_bounce(1 - 2 * x)) / 2
	else:
		return (1 + ease_out_bounce(2 * x - 1)) / 2

x = np.linspace(0, 1, 300)

# ease_in_sine
y = np.vectorize(ease_in_sine, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_sine.png')

# ease_out_sine
y = np.vectorize(ease_out_sine, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_sine.png')

# ease_in_out_sine
y = np.vectorize(ease_in_out_sine, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_sine.png')

# ease_in_quad
y = np.vectorize(ease_in_quad, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_quad.png')

# ease_out_quad
y = np.vectorize(ease_out_quad, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_quad.png')

# ease_in_out_quad
y = np.vectorize(ease_in_out_quad, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_quad.png')

# ease_in_cubic
y = np.vectorize(ease_in_cubic, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_cubic.png')

# ease_out_cubic
y = np.vectorize(ease_out_cubic, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_cubic.png')

# ease_in_out_cubic
y = np.vectorize(ease_in_out_cubic, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_cubic.png')

# ease_in_quart
y = np.vectorize(ease_in_quart, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_quart.png')

# ease_out_quart
y = np.vectorize(ease_out_quart, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_quart.png')

# ease_in_out_quart
y = np.vectorize(ease_in_out_quart, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_quart.png')

# ease_in_quint
y = np.vectorize(ease_in_quint, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_quint.png')

# ease_out_quint
y = np.vectorize(ease_out_quint, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_quint.png')

# ease_in_out_quint
y = np.vectorize(ease_in_out_quint, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_quint.png')

# ease_in_expo
y = np.vectorize(ease_in_expo, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_expo.png')

# ease_out_expo
y = np.vectorize(ease_out_expo, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_expo.png')

# ease_in_out_expo
y = np.vectorize(ease_in_out_expo, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_expo.png')

# ease_in_circ
y = np.vectorize(ease_in_circ, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_circ.png')

# ease_out_circ
y = np.vectorize(ease_out_circ, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_circ.png')

# ease_in_out_circ
y = np.vectorize(ease_in_out_circ, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_circ.png')

# ease_in_back
y = np.vectorize(ease_in_back, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_back.png')

# ease_out_back
y = np.vectorize(ease_out_back, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_back.png')

# ease_in_out_back
y = np.vectorize(ease_in_out_back, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_back.png')

# ease_in_elastic
y = np.vectorize(ease_in_elastic, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_elastic.png')

# ease_out_elastic
y = np.vectorize(ease_out_elastic, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_elastic.png')

# ease_in_out_elastic
y = np.vectorize(ease_in_out_elastic, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_elastic.png')

# ease_in_bounce
y = np.vectorize(ease_in_bounce, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_bounce.png')

# ease_out_bounce
y = np.vectorize(ease_out_bounce, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_out_bounce.png')

# ease_in_out_bounce
y = np.vectorize(ease_in_out_bounce, otypes=[float])(x)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('ease_in_out_bounce.png')