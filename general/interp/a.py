# License: CC0
# https://puzzleandy.com

# pip install matplotlib
# pip install scipy
# pip install numpy

from matplotlib import pyplot as plt
from scipy.interpolate import *
import numpy as np

px = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
py = np.array([0, 1, 0, 0.1, 0, 1])

is_piecewise_linear = False
is_smoothing = False

class Func:
	def __init__(self, func, label):
		self.func = func
		self.label = label

funcs = []
if is_piecewise_linear:
	funcs.append(Func(interp1d(px, py, kind='linear'), 'linear'))
	funcs.append(Func(interp1d(px, py, kind='nearest'), 'nearest'))
	funcs.append(Func(interp1d(px, py, kind='nearest-up'), 'nearest-up'))
	funcs.append(Func(interp1d(px, py, kind='zero'), 'zero'))
	funcs.append(Func(interp1d(px, py, kind='slinear'), 'slinear'))
	funcs.append(Func(interp1d(px, py, kind='previous'), 'previous'))
	funcs.append(Func(interp1d(px, py, kind='next'), 'next'))
for k in range(2, len(px)):
	funcs.append(Func(InterpolatedUnivariateSpline(px, py, k=k), 'InterpolatedUnivariateSpline' + str(k)))
	if is_smoothing:
		funcs.append(Func(UnivariateSpline(px, py, k=k), 'UnivariateSpline' + str(k)))
funcs.append(Func(Rbf(px, py), 'Rbf'))
funcs.append(Func(Akima1DInterpolator(px, py), 'Akima1DInterpolator'))
funcs.append(Func(PchipInterpolator(px, py), 'PchipInterpolator'))

x = np.linspace(0, 1, 100)
for func in funcs:
	plt.clf()
	plt.plot(x, func.func(x))
	for i in range(1, len(px) - 1):
		plt.plot(px[i], py[i],'ro') 
	plt.savefig(func.label + '.png')

