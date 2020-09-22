import numpy as np
import matplotlib.pyplot as plt

# nonlinear equation 풀때 쓰는 방법

# Constant
T = np.linspace(0.01, 2.0, 1000, float)
accuracy = 1e-6
y = np.zeros(1000, float)
key = 0
for i in T:
    m_0 = 1.0
    error = 1.0

    while accuracy < error:
        m_1 = np.tanh(m_0/i)
        error = abs((m_0 - m_1) / (1 - i*np.cosh(m_0/i)**2))
        m_0 = m_1
    y[key] = m_1
    key += 1

plt.plot(T, y, "r")
plt.show()
