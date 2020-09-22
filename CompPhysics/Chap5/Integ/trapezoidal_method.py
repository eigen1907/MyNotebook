import numpy as np


def f(x):
    return np.exp(x)


x = np.linspace(0.0, 2.5, 1001)
divide = len(x)
h = x[1] - x[0]
integ = f(x[0]) + f(x[divide-1])
integ /= 2.0

for i in range(1, divide-1):
    integ += f(x[i])
integ *= h

print("integ = ", integ)
