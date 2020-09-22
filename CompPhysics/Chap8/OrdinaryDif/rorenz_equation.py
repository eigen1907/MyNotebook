import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



sigma = 10.0
ran = 28.0
b = 8/3

tmax = 50.0
t = np.linspace(0.0, tmax, 100001)
r = np.zeros((len(t), 3))
tau = t[1] - t[0]
r[0, 0], r[0, 1], r[0, 2] = 0.0, 1.0, 0.0


def f(r, t):
    x = r[0]
    y = r[1]
    z = r[2]
    dxdt = sigma*(y - x)
    dydt = ran*x - y - x*z
    dzdt = x*y - b*z
    return np.array([dxdt, dydt, dzdt], float)


def RK4th(f, r, t):
    c_1 = tau * f(r, t)
    c_2 = tau * f(r + c_1*0.5, t + tau*0.5)
    c_3 = tau * f(r + c_2*0.5, t + tau*0.5)
    c_4 = tau * f(r + c_3, t + tau)
    return r + (c_1 + c_2*2 + c_3*2 + c_4)/6.0


for i in range(0, len(t) - 1):
    r[i+1] = RK4th(f, r[i], t[i])


plt.plot(t, r[:, 1], 'r-')
plt.xlim(0, tmax)
plt.show()

plt.plot(r[:, 0], r[:, 2], 'b-')
plt.show()

plt.plot(r[:, 0], r[:, 1], "r-")
plt.show()

plt.plot(r[:, 1], r[:, 2], 'g-')
plt.show()

fig = plt.figure()								# 이건 꼭 입력해야한다.
ax = fig.gca(projection='3d')				    
ax.plot(r[:, 0], r[:, 1], r[:, 2], "r-")		# 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.legend()										# 오른쪽 위에 나오는 글자 코드다. 이거 없애면 글자 사라진다. 없애도 좋다.

plt.show()

