from matplotlib import pyplot as plt
import numpy as np
import math

def clamp(x, mini=0, maxi=1):
	if x < mini:
		return mini
	if x > maxi:
		return maxi
	return x

def smoothstep(x, edge0=0, edge1=1):
	x = clamp((x - edge0) / (edge1 - edge0))
	return x * x * (3 - 2 * x)

def smootherstep(x, edge0=0, edge1=1):
	x = clamp((x - edge0) / (edge1 - edge0))
	return x * x * x * (x * (6 * x - 15) + 10)

def general_smoothstep(N, x):
  x = clamp(x, 0, 1)
  res = 0
  for n in range(0, N + 1):
    res += (math.pow(-1, n) *
            math.comb(N + n, n) *
            math.comb(2 * N + 1, N - n) *
            math.pow(x, N + n + 1))
  return res

# k > 0
def sigmoid_1(k, x):
	if x == 0:
		return 0
	return 1 / (1 + math.pow(1/x - 1, k))

def sigmoid_2(x, a, b, c, d):
	s = ((1 - d) - b) / ((1 - c) - a)
	if 0 <= x and x < a:
		p = (s * a) / b
		return b * math.pow(x * (1 / a), p)
	elif 1 - c < x and x <= 1:
		q = (s * c) / d
		return -d * math.pow(-(x - 1) * (1 / c), q) + 1
	else:
		return s * (x - a) + b

x = np.linspace(0, 1, 100)

y = np.empty(len(x))
for i in range(0, len(x)):
	y[i] = smoothstep(x[i])
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('smoothstep.png')

y = np.empty(len(x))
for i in range(0, len(x)):
	y[i] = smootherstep(x[i])
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('smootherstep.png')

N = 5
y = np.empty(len(x))
for i in range(0, len(x)):
	y[i] = general_smoothstep(N, x[i])
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('general_smoothstep.png')

k = 1.6
y = np.empty(len(x))
for i in range(0, len(x)):
	y[i] = sigmoid_1(k, x[i])
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('sigmoid_1.png')

a, b = 0.3, 0.2
c, d = 0.3, 0.2
y = np.empty(len(x))
for i in range(0, len(x)):
	y[i] = sigmoid_2(x[i], a, b, c, d)
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('sigmoid_2.png')