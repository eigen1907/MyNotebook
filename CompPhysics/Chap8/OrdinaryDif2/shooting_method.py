# 미분방정식의 경계값을 줬을 때(대충 값던져주면) 초기값을 찾아가는 방법
# 초기 값을 찾기 위해 secant method를 이용함
import numpy as np
import matplotlib.pyplot as plt

gravity = 9.81


def f(r, t):
    x = r[0]
    v = r[1]
    dxdt = v
    dvdt = -gravity
    return np.array([dxdt, dvdt], float)


def RK4th(f, r, t, tau):
    c_1 = tau * f(r, t)
    c_2 = tau * f(r + c_1*0.5, t + tau*0.5)
    c_3 = tau * f(r + c_2*0.5, t + tau*0.5)
    c_4 = tau * f(r + c_3, t + tau)
    return r + (c_1 + c_2*2 + c_3*2 + c_4)/6.0


def g(f, vec, t, tau, h):
    for i in range(len(t)-1):
        vec = RK4th(f, vec, t, tau)
    return vec[0] - h


"""v_0를 찾기 위한 secant method"""


def secant_method(g, f, v_1, v_2, h):
    tolerance = 1.0e-10
    while abs(v_2 - v_1) > tolerance:
        g_1 = g(f, [0, v_1], t, tau, h)
        g_2 = g(f, [0, v_2], t, tau, h)
        v_tmp = v_2 - ((g_2) * (v_2 - v_1)) / (g_2 - g_1)
        v_1 = v_2
        v_2 = v_tmp
    return (v_1 + v_2) / 2.0


v_1 = 1.0
v_2 = 40.0

t = np.linspace(0, 10, 1001)
tau = t[1] - t[0]

v_0 = secant_method(g, f, v_1, v_2, 0.0)

print("v_0=", v_0)

r = np.zeros((len(t), 2), float)
r[0, 0], r[0, 1] = 0.0, v_0
for i in range(0, len(t) - 1):
    r[i+1] = RK4th(f, r[i], t[i], tau)

plt.plot(t, r[:, 0], 'r-')
plt.xlim(0, 10)
plt.show() 