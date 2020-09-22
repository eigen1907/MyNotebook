# 주요 내용은 다차 미분이 된 미분방정식(심지어 변수도 다양한)을 풀어보자
# d^2(r)/dt^2 = f(r, dr/dt, t)로 표현
# dr/dt를 하나의 변수 s로 표현해서 결국 f(r, s, t)로 표현 (s또한 벡터로서 다양한 변수들의 미분을 모아놓은게 되겠죠)

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 0.1


def f(r, t):
    x = r[0]
    v = r[1]
    f_x = v
    f_v = -(g/l)*np.sin(x)
    return np.array([f_x, f_v], float)


def RK4th(f, r, t, tau):
    c_1 = tau * f(r, t)
    c_2 = tau * f(r + c_1*0.5, t + tau*0.5)
    c_3 = tau * f(r + c_2*0.5, t + tau*0.5)
    c_4 = tau * f(r + c_3, t + tau)
    return r + (c_1 + c_2*2 + c_3*2 + c_4)/6.0


def f_v(x, v, t):
    return -g*np.sin(x)/l


def Modified_RK4th(f, r, t, tau):
    x = r[0]
    v = r[1]
    c_1 = tau*f_v(x, v, t)
    c_2 = tau*f_v(x + tau*v/2.0, v + c_1/2.0, t + tau/2.0)
    c_3 = tau*f_v(x + tau*v/2.0 + tau*c_1/4.0, v + c_2/2.0, t + tau/2.0)
    c_4 = tau*f_v(x + tau*v + tau*c_2/2.0, v + c_3, t + tau)
    x += tau*v + tau*(c_1 + c_2 + c_3)/6.0
    v += (c_1 + 2*c_2 + 2*c_3 + c_4)/6.0
    return [x, v]


tmax = 5.0
t = np.linspace(0.0, tmax, 10001)
r = np.zeros((len(t), 2))
tau = t[1] - t[0]

r[0, 0], r[0, 1] = np.pi - 0.1, 0.0

for i in range(0, len(t) - 1):
    # r[i+1] = RK4th(f, r[i], t[i], tau)
    r[i+1] = Modified_RK4th(f_v, r[i], t[i], tau)

plt.plot(t, r[:, 0], 'r-')
plt.plot(t, r[:, 1], 'b-')
plt.xlim(0, tmax)
plt.show()

plt.plot(r[:, 0], r[:, 1], 'b-')
plt.xlim(-4, 4)
plt.show()