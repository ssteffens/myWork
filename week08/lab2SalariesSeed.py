# This program outputsa list of salaries consisting of 10 random numbers. The same numbers will be returned
# whenever the program is run. 
# Author: Stefanie Steffens

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntires = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntires)
print(salaries)