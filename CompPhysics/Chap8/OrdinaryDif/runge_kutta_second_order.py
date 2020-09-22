#이것 또한 마찬가지! 하지만 nu_21을 포함한 c_1과 c_2를 이용해서 계산 -> 더 정확함
#alpha에 따른 차이는 거의 없지만 0.5로 두고 (alpha_1 = alpha_2) 푸는게 일반적이고 정확함
import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    y = -x**3 + np.sin(t)
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
    c_2 = tau * f(x[i] + c_1*nu_21, t[i] + tau*nu_21)
    x[i+1] = x[i] + c_1*alpha_1 + c_2*alpha_2

plt.plot(t, x, 'r-')
plt.xlim(0, tmax)
plt.show()
