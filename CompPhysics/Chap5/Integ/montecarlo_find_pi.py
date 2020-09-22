from random import random, seed # seed는 random number를 순수한 의미의 random 넘버로 만들어주는 역할을 함.
import numpy as np

num_realization = 100
seed()
np = 1000
pi_res = 0

for num_rel in range(0,num_realization):
    ncircle = 0
    for i in range(0,np):
        x = random()
        y = random()
        if y <= (1.0 - x**2)**(0.5):
            ncircle += 1
    pi_tmp = 4.0 * ncircle / float(np)
    pi_res += pi_tmp
pi_res /= float(num_realization)

print("pi = ", pi_res)


# 다른 표현으로는 integ = (b-a)/N * sig(1~N)f(x_i) 을 하는 방법이 있음 => 보통 이방법을 주로 사용함
# 다트를 던져서 f보다 작은 부분만 확률적으로 더해서 구하는게 그 전 방법