# This program plots the function y = x ** 2
# Author: Stefanie Steffens

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "x squared")
plt.show()
