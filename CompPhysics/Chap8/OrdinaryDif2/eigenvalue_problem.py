import numpy as np
import matplotlib.pyplot as plt

m = 9.1094e-31
hbar = 1.0546e-34
e = 1.6022e-19
L = 5.2918e-11
N = 1001
h = L/N
x = np.linspace(0, L, N)


def V(x):
    return 0.0


def f(r, x, E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2) * (V(x) - E)*psi
    return np.array([fpsi, fphi], float)


def RK4th(f, r, x, E):
    c1 = h*f(r, x, E)
    c2 = h*f(r + c1*0.5, x + h*0.5, E)
    c3 = h*f(r + c2*0.5, x + h*0.5, E)
    c4 = h*f(r + c3, x + h, E)

    return r + (c1 + c2*2 + c3*2 + c4)/6.0


def solve(E):
    psi = 0.0
    phi = 1.0
    r = np.array([psi, phi], float)
    for i in x:
        r = RK4th(f, r, x, E)
    return r[0]


E_1 = 0.0
E_2 = e

psi_2 = solve(E_1)

tolerance = e / 1000

while abs(E_1 - E_2) > tolerance:
    psi_1, psi_2 = psi_2, solve(E_2)
    E_1, E_2 = E_2, E_2 - psi_2*(E_2 - E_1) / (psi_2 - psi_1)

print("E = ", E_2, ",(", E_2/e, "eV)")

r = np.zeros((len(x), 2))

r[0, 0] = 0
r[0, 1] = 1

for i in range(len(x)-1):
    r[i+1] = RK4th(f, r[i], x[i], E_2)


integ = 0
for i in range(len(x)-1):
    integ += h*r[i, 0]**2

normalized_psi = r[:, 0] / np.sqrt(integ)

plt.plot(x, normalized_psi)
plt.xlim(0, L)
plt.show()
