import numpy as np
import matplotlib.pyplot as plt

g = 9.81
t_i = 0.0
t_f = 10.0
N = 100
h = (t_f -t_i) / N

def f():
    return (-g)

t = np.linspace(t_i, t_f, N, float)

x = np.zeros([N], float)
for i in range(1, N-1):
    x[i] = 20

x_tmp = np.copy(x)

w = 0.8
tolerance = 1e-6
delta = 1.0

while delta > tolerance:
    for i in range(1, N-1):
        x_tmp[i] = (x[i+1] + x[i-1] - f()*h**2) / 2.0
    x, x_tmp = x_tmp, x
    delta = np.amax(abs(x - x_tmp))

plt.plot(t, x)
plt.show()

