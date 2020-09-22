import numpy as np
import matplotlib.pyplot as plt


""" Boundary Condition """

b = 0.9
# b = 1.15
q = 0.5
omega_0 = 2/3

tmax = 100
t = np.linspace(0.0, tmax, 10001)
r = np.zeros((len(t), 2))
r[0, 0] = 30.0
r[0, 1] = 2 / 3
h = t[1] - t[0]


""" f(r, t) = dr/dt """


def f(r, t):
    theta = r[0]
    omega = r[1]
    dtheta_dt = omega
    domega_dt = b*np.cos(omega_0*t) - np.sin(theta) - q*omega
    return np.array([dtheta_dt, domega_dt], float)


""" RK4th function """


def RK4th(f, r, t):
    c_1 = h * f(r, t)
    c_2 = h * f(r + c_1*0.5, t + h*0.5)
    c_3 = h * f(r + c_2*0.5, t + h*0.5)
    c_4 = h * f(r + c_3, t + h)
    return r + (c_1 + c_2*2 + c_3*2 + c_4)/6.0


""" Culculate """


for i in range(0, len(t) - 1):
    """ RK4th """
    r[i+1] = RK4th(f, r[i], t[i])


""" Plotting """


plt.plot(t, r[:, 0], 'r-')
plt.xlim(0, tmax)
plt.show()