import numpy as np
from scipy.optimize import LinearConstraint, milp, Bounds
import math

# minimize p + n + d
c = np.array([1, 1, 1])

A = np.array([
    [1, 5, 10], # p + 5*n + 10*d = total
    [1, 1, 1], # p + n + d = number of coins
])

# total bounded above and below by 100. number of coins by 21
bu = np.array([100, 21])
bl = np.array([100, 21])

constraints = LinearConstraint(A, bl, bu)

# p, n, and d are integers (indicated by 1)
integrality = np.array([1, 1, 1])

# at least one of each coin
bounds = Bounds(lb=1)

# solve
res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)

p, n, d = res.x
print(f'{p} pennies, {n} nickles, {d} dimes')