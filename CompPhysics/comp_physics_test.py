import numpy as np
import matplotlib.pyplot as plt

M = 100
h = 1/100
tolerance = 1.0e-4

phi = np.zeros([M+1, M+1], float)
phitmp = np.zeros([M+1, M+1], float)
rho = np.zeros([M+1, M+1], float)
rhotmp = np.zeros([M+1, M+1], float)
electricfield_x = np.zeros([M+1, M+1], float)
electricfield_y = np.zeros([M+1, M+1], float)
x = np.linspace(0, 0.4, 101, float)
y = np.linspace(0, 0.4, 101, float)


rho[50, 50] = 1.0e4 / 1.6 #(rho = Q / A, )

delta = 1.0

while delta > tolerance:
    for i in range(1, M):
        for j in range(1, M):
            phitmp[i, j] = (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1] - rho[i, j]*((x[1]-x[0])*(y[1]-y[0]))) / 4.0
    delta = np.max(abs(phitmp - phi))
    phi, phitmp = phitmp, phi

for i in range(M):
    for j in range(M):
        if (i-50)**2 + (j-50)**2 > 2500:
            phi[i, j] = 0.0
            phitmp[i, j] = 0.0

for i in range(1, M):
    for j in range(1, M):
        electricfield_x[i, j] = (phi[i+1, j] - phi[i, j]) / (x[1] - x[0])
        electricfield_y[i, j] = (phi[i, j+1] - phi[i, j]) / (y[1] - y[0])


#data의 [i][j][0~3]은 각각 x좌표, y좌표, 전위, 전기장의 x성분, 전기장의 y성분의 크기를 가지고 있다 어쩌다 만들어봤어요...
data = np.zeros([101, 101, 5], float)
for i in range(100):
    for j in range(101):
        data[i, j, 0] = x[i]
        data[i, j, 1] = y[j]
        data[i, j, 2] = phi[i, j]
        data[i, j, 3] = electricfield_x[i, j]
        data[i, j, 4] = electricfield_y[i, j]

print(phi[50, 50])
print(electricfield_x[50, 50])
print(electricfield_y[50, 50])



for i in range(11):
    for j in range(11):
        plt.quiver(x[10*i], y[10*j], electricfield_x[10*i, 10*j], electricfield_y[10*i, 10*j], angles='xy', pivot='middle')
plt.ylim(0, y[100])
plt.xlim(0, x[100])
plt.grid('on')
plt.show()

for i in range(11):
    for j in range(11):
        plt.quiver(x[10*i], y[10*j], phi[10*i, 10*j], phi[10*i, 10*j], angles='xy', pivot='middle')
plt.ylim(0, y[100])
plt.xlim(0, x[100])
plt.grid('on')
plt.show()

print("뭔가 개망했지만 괜찮아 ㅎㅎ")

