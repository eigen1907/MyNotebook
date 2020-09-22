# euler method와 마찬가지로 dy/dx = f(x, y)의 꼴을 품 대신 predictor를 사용해서 계산
import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return -x ** 3 + np.sin(t)


tmax = 10.0
t = np.linspace(0.0, tmax, 1001)
x = np.zeros(len(t), float)
h = t[1] - t[0]

for i in range(0, len(t)-1):
    predictor = x[i] + h*f(x[i],t[i])
    x[i+1] = x[i] + h*(f(x[i], t[i])+f(predictor, t[i+1]))/2.0

plt.plot(t, x)
plt.xlim(0,tmax)
plt.show()