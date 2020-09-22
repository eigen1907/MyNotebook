import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    y = -x**3+np.sin(t)
    return y


tmax = 10.0
t = np.linspace(0.0, tmax, 1001)
x = np.zeros(len(t), float)
tau = t[1] - t[0]

alpha_1 = 0.2
alpha_2 = 1 - alpha_1
nu_21 = 1 / (alpha_2 * 2)

for i in range(0, len(t)-1):
    c_1 = tau * f(x[i], t[i])
    c_2 = tau * f(x[i] + c_1*0.5, t[i] + tau*0.5)
    c_3 = tau * f(x[i] + c_2*0.5, t[i] + tau*0.5)
    c_4 = tau * f(x[i] + c_3, t[i] + tau)
    x[i+1] = x[i] + (c_1 + c_2*2 + c_3*2 + c_4) / 6.0

plt.plot(t, x, 'r-')
plt.xlim(0, tmax)
plt.show()