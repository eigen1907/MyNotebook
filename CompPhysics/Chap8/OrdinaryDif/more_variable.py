#내용은 간단함 f(x, t) 였던 것들은 f(r, t)로 바꾸어 주면 됨 r = (x, y, z, ...) [즉 벡터로 생각하면 됨]
import numpy as np
import matplotlib.pyplot as plt


def f(r, t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + np.sin(t)**2
    return np.array([fx, fy], float)


def RK4th(f, r, t, tau):
    c_1 = tau * f(r, t)
    c_2 = tau * f(r + c_1*0.5, t + tau*0.5)
    c_3 = tau * f(r + c_2*0.5, t + tau*0.5)
    c_4 = tau * f(r + c_3, t + tau)
    return r + (c_1 + c_2*2 + c_3*2 + c_4)/6.0


tmax = 10.0
t = np.linspace(0.0, tmax, 10001)
r = np.zeros((len(t), 2))
tau = t[1] - t[0]

r[0, 0], r[0, 1] = 1.0, 1.0

for i in range(0, len(t) - 1):
    r[i+1] = RK4th(f, r[i], t[i], tau)

plt.plot(t, r[:, 0], 'b-')
plt.plot(t, r[:, 1], 'r-')
plt.xlim(0, tmax)
plt.show()
