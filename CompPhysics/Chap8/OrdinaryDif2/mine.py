import numpy as np
import matplotlib.pyplot as plt

m = 9.1094e-31
hbar = 1.0546e-34
e = 1.6022e-19
L = 5.2918e-11
N = 1001
h = L/N
k = e
x = np.linspace(0, L, N)
r = np.zeros((len(x), 3), float)
r_2 = np.zeros((len(x), 3), float)
r[0, 0], r_2[0, 0] = 0, 0
r[0, 1], r_2[0, 1] = 1, 1
r[0, 2], r_2[0, 2] = 0, 0


def f(r, x, E):
    psi = r[0]
    phi = r[1]
    V = r[2]
    fpsi = phi
    fphi = (2*m/hbar**2) * (V - E)*psi
    fV = k * x
    return np.array([fpsi, fphi, fV], float)


def RK4th(f, r, x, E):
    c1 = h*f(r, x, E)
    c2 = h*f(r + c1*0.5, x + h*0.5, E)
    c3 = h*f(r + c2*0.5, x + h*0.5, E)
    c4 = h*f(r + c3, x + h, E)

    return r + (c1 + c2*2 + c3*2 + c4)/6.0

E_1 = 0
E_2 = e
tolerance = e / 1000
while abs(E_1 - E_2) > tolerance:
    for i in range(0, len(x) - 1):
        r[i+1] = RK4th(f, r[i], x[i], E_1)
        r_2[i+1] = RK4th(f, r[i], x[i], E_2)
    E_1, E_2 = E_2, E_2 - r_2[N-1, 0]*(E_2 - E_1) / (r_2[N-1, 0] - r[N-1, 0])    
print(E_1, E_2)


r = np.zeros((len(x), 3), float)
r[0, 0] = 0
r[0, 1] = 1
r[0, 2] = 0
for i in range(len(x) - 1):
    r[i+1] = RK4th(f, r[i], x[i], E_1)

integ = 0
for i in range(len(x)):
    integ += hbar * r[i, 0]**2
r[i, 0] /= np.sqrt(integ)


print(r[:, 0])

plt.plot(x, r[:, 0])
plt.xlim(0, 7e-13)
plt.show()


