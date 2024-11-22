# License: CC0
# https://puzzleandy.com

# pip install numpy
# pip install matplotlib

import numpy as np
from matplotlib import pyplot as plt

y = np.array([
	5.73, 6.3, 6.93, 7.63, 8.39,
	9.23, 10.2, 11.2, 12.3, 13.5, 
	14.9, 16.4, 18, 19.8, 21.8,
	23.9, 26.3, 29, 31.9, 35,
	38.6, 42.4, 46.7, 51.3, 56.4,
	62.1, 68.3, 75.1, 82.6, 90.9,
	100,
	110, 121, 133, 146, 161,
	177, 195, 214, 236, 259,
	285, 314, 345, 380, 418,
	459, 505, 556, 612, 673,
	740, 814, 895, 985, 1080,
	1190, 1310, 1440, 1590, 1740])

x = np.empty(len(y), np.float32)
i = -np.where(y == 100)[0][0]
for j in range(0, len(y)):
	x[j] = i
	i += 1

plt.plot(x, y, color='red')
plt.show()