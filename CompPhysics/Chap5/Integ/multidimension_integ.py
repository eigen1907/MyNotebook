import numpy as np
from random import random

x_i = 0.0
x_f = 1.0
y_i = 0.0
y_f = 1.0
z_i = 0.0
z_f = 1.0
number = 10000


def f(x, y, z):
    return x + y + z


def montecarlo(f):
    integ = 0.0
    for i in range(number):
        x = (x_f - x_i) * random()
        y = (y_f - y_i) * random()
        z = (z_f - z_i) * random()
        integ += f(x, y, z)
    integ *= (x_f - x_i)*(y_f - y_i)*(z_f - z_i)
    integ /= number
    return integ


print(montecarlo(f))