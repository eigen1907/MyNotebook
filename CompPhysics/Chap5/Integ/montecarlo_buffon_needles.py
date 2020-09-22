# Buffon's needle
# 길이가 1인 바늘은 던지는건데 위치를 표현하기 위해서는 끝에서 부터 거리 D와 각도 theta를 알아야함
# 가까운쪽을 D로 놓을거임 0 <= D <= 1/2, 0 <= theta <= pi
# 1/2sin(theta) >= D이면 바늘이 벽면에 닿은거임
from random import random, seed
from numpy import empty
from math import pi, sin, cos
from matplotlib import pyplot as plt


def plot_needles(n_needle):
    plt. figure(figsize=(8, 4))
    Lmin = 0.0
    Lmax = 3.0
    topline_x = [Lmin, Lmax]
    topline_y = [1.0, 1.0]
    bottomline_x = [Lmin, Lmax]
    bottomline_y = [0, 0]

    plt.plot(topline_x, topline_y, 'b', linewidth=3)
    plt.plot(bottomline_x, bottomline_y, 'b', linewidth=3)

    center_x = empty(n_needle, float)
    i = 0

    while i < n_needle:
        center_x[i] = random() * Lmax
        x = [center_x[i] - cos(theta[i]) * 0.5, center_x[i] + cos(theta[i]) * 0.5]
        y = [center_y[i] - sin(theta[i]) * 0.5, center_y[i] + sin(theta[i]) * 0.5]
        plt.plot(x, y, 'r')
        i += 1
    plt.xlim(-0.5, 3.5)
    plt.ylim(-0.5, 1.5)

    plt.show()


n = [10, 100, 500, 1000]


for np in n:
    seed()
    theta = empty(np, float)
    center_y = empty(np, float)
    D = empty(np, float)
    i = 0

    ncount = 0.0
    while i < np:
        theta[i] = pi * random()
        center_y[i] = random()
        if center_y[i] > 0.5:
            D[i] = 1.0 - center_y[i]
        else:
            D[i] = center_y[i]
        if D[i] <= sin(theta[i]) / 2.0:
            ncount += 1.0
        i += 1
    p = ncount / np
    print("pi = ", 2.0/p)

    plot_needles(np)
