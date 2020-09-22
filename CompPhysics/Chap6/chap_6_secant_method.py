import numpy as np
import matplotlib.pyplot as plt

accuracy = 1.0e-6


def f(x):
    return (np.exp(x)*np.log(x)) - x**2


def dfdx(x_a, x_b):
    return (f(x_b) - f(x_a)) / (x_b - x_a)


x_1 = 2.5
x_2 = 2.2
y = []

for i in range(10000):
    x_tmp = x_2 - (f(x_2) / dfdx(x_1, x_2))
    x_1 = x_2
    x_2 = x_tmp
    y.append(x_2)
    if accuracy >= abs(x_2 - x_1):
        break
print(x_2)
plt.plot(y)
plt.show()
