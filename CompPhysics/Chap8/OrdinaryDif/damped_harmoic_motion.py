import numpy as np
import matplotlib.pyplot as plt


""" Boundary Condition """

# Over Damping
# c, m, k = 50, 10, 10

# Critical Damping
# c, m, k = 20, 10, 10

# Under Damping
c, m, k = 20, 100, 100 


tmax = 100
t = np.linspace(0.0, tmax, 10001)
r = np.zeros((len(t), 2))
r[0, 0] = 10
r[0, 1] = 0
h = t[1] - t[0]

""" f(r, t) = dr/dt """


def f(r, t):
    x = r[0]
    v = r[1]
    dxdt = v
    dvdt = (-c*v - k*x) / m
    return np.array([dxdt, dvdt], float)


""" EM funtion """


def EM(f, r, t):
    return r + h*f(r, t)


""" RK2nd funtion """


def RK2nd(f, r, t):
    alpha_1 = 0.3
    alpha_2 = 1 - alpha_1
    nu_21 = 1 / (alpha_2 * 2)
    c_1 = h * f(r, t)
    c_2 = h * f(r + c_1*nu_21, t + h*nu_21)
    return r + c_1*alpha_1 + c_2*alpha_2


""" RK4th function """


def RK4th(f, r, t):
    c_1 = h * f(r, t)
    c_2 = h * f(r + c_1*0.5, t + h*0.5)
    c_3 = h * f(r + c_2*0.5, t + h*0.5)
    c_4 = h * f(r + c_3, t + h)
    return r + (c_1 + c_2*2 + c_3*2 + c_4)/6.0


""" Culculate """


for i in range(0, len(t) - 1):
    """ EM """
    # r[i+1] = EM(f, r[i], t[i])
    """ RK2nd """
    # r[i+1] = RK2nd(f, r[i], t[i])
    """ RK4th """
    r[i+1] = RK4th(f, r[i], t[i])


""" Plotting """


plt.plot(t, r[:, 0], 'r-')
plt.xlim(0, tmax)
plt.show()