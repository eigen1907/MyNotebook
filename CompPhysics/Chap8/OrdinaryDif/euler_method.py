# dy/dx = f(y, x)의 꼴을 풀 수 있음
import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return -x ** 3 + np.sin(t)


h = 0.001
tmax = 10.0

t = 0.0
x = 0.0

t_plot = []
x_plot = []


i = 0

while t <= tmax:
    x = x + h*f(x, t)
    t += h
    t_plot.append(t)
    x_plot.append(x)

print("t=", t, "x=", x)

plt.plot(t_plot, x_plot)
plt.xlim(0, 10)
plt.show()