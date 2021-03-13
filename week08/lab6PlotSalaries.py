# This program plots a histogram of salaries created randomly. The same salaries returned
# whenever the program is run. 
# Author: Stefanie Steffens

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntires = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntires)
#print(salaries)

plt.hist(salaries)
plt.show()