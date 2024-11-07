from matplotlib import pyplot as plt
import numpy as np
import math

# k > 0
def sigmoid(k, x):
	if x == 0:
		return 0
	return 1 / (1 + math.pow(1/x - 1, k))

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

def gen_smoothstep(N, x):
  x = clamp(x, 0, 1)
  res = 0
  for n in range(0, N + 1):
    res += (math.pow(-1, n) *
            math.comb(N + n, n) *
            math.comb(2 * N + 1, N - n) *
            math.pow(x, N + n + 1))
  return res

x = np.linspace(0, 1, 100)

k = 1.6
y = np.empty(len(x))
for i in range(0, len(x)):
	y[i] = sigmoid(k, x[i])
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('sigmoid.png')

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
	y[i] = gen_smoothstep(N, x[i])
plt.clf()
plt.plot(x, y, color='red')
plt.savefig('gen_smoothstep.png')