import numpy as np
import matplotlib.pyplot as plt

M = 100
V = 1.0
tolerance = 1.0e-4

phi = np.zeros([M+1, M+1], float)
phi[0, :] = V
phitmp = np.zeros([M+1, M+1], float)
phitmp[0, :] = V

delta = 1.0

while delta > tolerance:
    for i in range(1, M):
        for j in range(1, M):
            phitmp[i, j] = (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1]) / 4.0
    delta = np.max(abs(phitmp - phi))
    phi, phitmp = phitmp, phi

plt.imshow(phi)
plt.show()