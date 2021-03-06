import numpy as np
import matplotlib.pyplot as plt
import math

r = [38.6, 39.4, 39.4, 37.5, 35.1, 32.1, 28.7, 24.9, 21.2, 17.0, 13.0, 9.3, 6.7, 4.9, 3.8, 2.5, 1.6, 1.0, 0.7, 0.1, 0.6, 0.6, 0.7, 1.0, 1.3, 2.0, 2.2, 2.2, 2.0, 2.0, 1.7, 1.5
, 1.4, 1.3, 1.1, 1.1, 1.0, 1.0, 1.2, 1.2, 1.3, 1.4, 1.6, 1.6, 1.8, 1.9, 2.6, 2.1, 2.0,2.7, 2.6, 2.3, 2.5, 2.3, 2.0, 1.7, 1.3, 1.1, 1.0, 1.3, 2.3, 4.2, 6.5, 10.3, 15.5
, 20.0, 24.5, 29.0, 33.5, 35.9, 39.2, 41.0, 41.7]
k = []

for a in r:
    k.append(32.4 - (20*math.log10(a/41.7)))

theta = np.arange(0.0, float(2 * np.pi) + (np.pi)/36, np.pi/36)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, k)
ax.grid(True)

ax.set_title("Polar Plot", va='bottom')
plt.show()
