# simpson 3/8 rules
# sig(0~N/3-3)(f_i + 3f_i+1 + 3f_i+2 + f_i+3) * 3h/8


import numpy as np


def f(x):
    return np.sin(x)


x = np.linspace(0, np.pi, 1000)

h = x[1] - x[0]


def simpson38(x):
    integ = 0
    for i in range(int(len(x)/3) - 1):
        integ += f(x[3*i]) + 3 * f(x[3*i+1]) + 3 * f(x[3*i+2]) + f(x[3*i+3])     
    return (integ*h) * 3 / 8


print(simpson38(x))