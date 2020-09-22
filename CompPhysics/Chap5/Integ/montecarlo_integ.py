# 다른 표현으로는 integ = (b-a)/N * sig(1~N)f(x_i) 을 하는 방법이 있음 => 보통 이방법을 주로 사용함
# sin(x) => 0~pi
from random import random, seed
import numpy as np


def f(x):
    return np.sin(x)


seed()

num_realization = 100

num_point = 10000

integ_res = 0.0

for sample in range(0, num_realization):
    integ_tmp = 0
    for i in range(0, num_point):
        x = random() * np.pi
        integ_tmp += f(x)
    integ_tmp *= (np.pi)
    integ_tmp /= num_point
    integ_res += integ_tmp
integ_res /= num_realization


print(integ_res)