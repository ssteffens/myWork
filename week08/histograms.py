# Histograms
# Author: Stefanie Steffens

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)      # will always return same random numbers. Otherwise plot will look different every time it's run
normData = np.random.normal(size = 10000)

plt.hist(normData)
plt.show()