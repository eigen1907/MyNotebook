import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(x) * np.log(x) - x**2


def dfdx(x):
    return np.exp(x) * (np.log(x) + 1/x) - 2*x


accuracy = 1.0e-12

x = 3.0
delta = 1.0
y = []

for i in range(1000):
    x -= f(x) / dfdx(x)
    delta = abs(f(x) / dfdx(x))
    y.append(x)
    if delta <= accuracy:
        break

print("x= ", x)

plt.plot(y, 'ro-')
plt.show()