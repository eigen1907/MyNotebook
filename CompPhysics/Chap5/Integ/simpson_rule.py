# simpson rule 적분
# sig(0~N/2-2)(f_2i + 4f_2i+1 + f_2i+2) * h/3

import numpy as np


def f(x):
    return np.sin(x)


x = np.linspace(0, np.pi, 1000)

h = x[1] - x[0]


def simpson(x):
    integ = 0
    for i in range((int(len(x)/2) - 1)):
        integ += f(x[2*i]) + 4 * f(x[2*i+1]) + f(x[2*i+2])   
    return (integ*h)/3


print(simpson(x))
print(len(x)/2 - 1)