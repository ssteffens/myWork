# Matplotlib Instroduction


# x-square function f(x) = x ** 2
import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "x squared")
plt.plot(xpoints, xpoints, label = "straight", color = "blue")
plt.legend()
#plt.show()

# To save plot: 
plt.savefig("testPlot")