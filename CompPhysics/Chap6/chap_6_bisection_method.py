import numpy as np
import matplotlib.pyplot as plt
        
def f(x):
    return np.exp(x) * np.log(x) - x**2


def bisection(a, b, error, x):
    x = (a + b) / 2
    if f(x) * f(a) < 0:
        b = x
    else:
        a = x
    error = abs(a - b)
    return [a, b, error, x]


accuracy = 1e-6

error = 5

a_0 = 1

b_0 = 2

x_0 = 3/2
    
y = []

while error > accuracy:
    [a_0, b_0, error, x_0] = bisection(a_0, b_0, error, x_0)
    y.append(x_0)
    print(a_0, b_0)

plt.plot(y)
plt.show()