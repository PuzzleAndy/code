# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install matplotlib

import math
import numpy as np
from matplotlib import pyplot as plt

x1 = 1
y1 = 1
x2 = 4
y2 = 20

b = math.pow(y2 / y1, 1 / (x2 - x1))
a = y1 / math.pow(b, x1)

x = np.linspace(-5, 5, 100)
y = a * b ** x

plt.plot(x, y, color='red')
plt.plot(x1, y1, color='black', marker='o')
plt.plot(x2, y2, color='black', marker='o')
plt.show()