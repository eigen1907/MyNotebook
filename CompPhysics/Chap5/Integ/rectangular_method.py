import numpy as np


def f(x):
    return np.exp(x)


x = np.linspace(0.0, 2.5, 1001)
divide = len(x)
h = x[1] - x[0]

integ = 0.0
for i in range(divide-1):
    integ += f((x[i+1] + x[i]) / 2.0)
integ *= h

print("integ = ", integ)