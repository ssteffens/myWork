# This program prints out a list of salaries consisting of 10 random numbers
# AUthor: Stefanie Steffens

import numpy as np
salaries = np.random.randint(20000, 80000, 10)
print(salaries)

# Setting absolute values as variables

minSalary = 20000
maxSalary = 80000
numberOfEntires = 10

salariesNew = np.random.randint(minSalary, maxSalary, numberOfEntires)
print(salariesNew)
