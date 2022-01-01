from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import math

Ts = 1/50
t = np.arange(0, 1, Ts)
a = 1
x = np.tan(2*math.pi*t*a)
print(x)
y = fft(x)
print(y)
fs = 1/Ts
freq = np.arange(0, fs, fs/len(y))
yinv = ifft(y)
print(yinv)

fig,ax = plt.subplots(2,1)

ax[0].plot(freq,abs(y))
ax[1].plot(freq,abs(yinv))

plt.show()
