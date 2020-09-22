import numpy as np
import matplotlib.pyplot as plt

M = 100
h = 0.01
tolerance = 1.0e-6

phi = np.zeros([M+1, M+1], float)
phitmp = np.zeros([M+1, M+1], float)
rho = np.zeros([M+1, M+1], float)

for i in range(60, 80):
    for j in range(20, 40):
        rho[i, j] = 1.0
        rho[j, i] = -1.0


delta = 1.0

while delta > tolerance:
    for i in range(1, M):
        for j in range(1, M):
            phitmp[i, j] = (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1] - rho[i, j]*(h**2)) / 4.0
    delta = np.max(abs(phitmp - phi))
    phi, phitmp = phitmp, phi

plt.imshow(phi)
plt.show()