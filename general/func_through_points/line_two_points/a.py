# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install matplotlib

import numpy as np
from matplotlib import pyplot as plt

x1 = -1
y1 = -5
x2 = 2
y2 = 10

x = np.linspace(-5, 5, 100)
y = (y2 - y1) / (x2 - x1) * (x - x1) + y1

plt.plot(x, y, color='red')
plt.plot(x1, y1, color='black', marker='o')
plt.plot(x2, y2, color='black', marker='o')
plt.show()