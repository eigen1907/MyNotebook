import matplotlib.pyplot as plt
import numpy as np


def wanted_f(x):
    return x**2


def two_point_diff(f, x, h):
    return (f(x+h)-f(x))/h


def three_point_diff(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)


def second_diff(f, x, h):
    return (f(x+h) + f(x-h) - 2*f(x)) / h**2


x = np.linspace(-2, 2, 100)
y_two = np.zeros(len(x), float)
y_three = np.zeros(len(x), float)
y_second = np.zeros(len(x), float)
y = np.zeros(len(x), float)
h = 0.1
count = 0

for i in x:
    y_two[count] = two_point_diff(wanted_f, i, h)
    y_three[count] = three_point_diff(wanted_f, i, h)
    y_second[count] = second_diff(wanted_f, i, h)
    y[count] = wanted_f(i)
    count += 1

plt.plot(x, y_two, 'ro', mfc='none', ms=7)
plt.plot(x, y_three, 'gs', mfc='none', ms=5)
plt.plot(x, y_second, 'yx', mfc='none', ms=5)
plt.plot(x, y, 'b-', lw=2)
plt.show()