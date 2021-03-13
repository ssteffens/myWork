# This program creates a list called "Ages" containing 10 random numbers between 21 and 65 and a list of
# salaries between 20000 and 80000. The arrays are plotted into a scatter plot. An additional line is
#plotted for function y = x**2 in a different colour. 
# Author: Stefanie Steffens

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000

minAge = 21
maxAge = 65

numberOfEntires = 10

np.random.seed(1)
ages = np.random.randint(minAge, maxAge, numberOfEntires)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntires)

plt.scatter(ages, salaries)

xpoints = np.array(range(21,65))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = "red")

plt.show()