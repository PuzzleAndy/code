# License: CC0
# https://puzzleandy.com

# pip install matplotlib
# pip install scipy
# pip install numpy

import math
from matplotlib import pyplot as plt
from scipy.interpolate import *
import numpy as np

midpoint = 0.2
is_smoothing = False

px = np.array([0, midpoint, 1])
py = np.array([0, 0.5, 1])

class Func:
	def __init__(self, func, label):
		self.func = func
		self.label = label

class Pow:
	def __init__(self, px, py):
		self.px = px
		self.py = py
	def __call__(self, x):
		return x**(math.log(py[1]) / math.log(px[1]))

funcs = []
funcs.append(Func(Pow(px, py), 'Pow'))
for k in range(2, len(px)):
	funcs.append(Func(InterpolatedUnivariateSpline(px, py, k=k), 'InterpolatedUnivariateSpline' + str(k)))
	if is_smoothing:
		funcs.append(Func(UnivariateSpline(px, py, k=k), 'UnivariateSpline' + str(k)))
funcs.append(Func(Rbf(px, py), 'Rbf'))
funcs.append(Func(Akima1DInterpolator(px, py), 'Akima1DInterpolator'))
funcs.append(Func(PchipInterpolator(px, py), 'PchipInterpolator'))

x = np.linspace(0, 1, 300)
for func in funcs:
	plt.clf()
	plt.plot(x, np.clip(func.func(x), 0, 1))
	plt.plot(px[1], py[1],'ro') 
	plt.savefig(func.label + '.png')