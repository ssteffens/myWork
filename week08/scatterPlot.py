# Scatter Plots

import numpy as np
import matplotlib.pyplot as plt


xpoints = np.array(range(1,101))



randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints)

plt.show()