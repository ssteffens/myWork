# This program outputs a list of salaries consisting of 10 random numbers as well as a second list 
# containing the salaries plus 5% increase 
# The same numbers will be returned whenever the program is run. 
# Author: Stefanie Steffens

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntires = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntires)
salariesPlus = (salaries * 1.05).astype(int)
print(salaries)
print(salariesPlus)