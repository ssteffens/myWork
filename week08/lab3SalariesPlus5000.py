# This program outputs a list of salaries consisting of 10 random numbers as well as a second list 
# containing the salaries plus 5000. 
# The same numbers will be returned whenever the program is run. 
# Author: Stefanie Steffens

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntires = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntires)
salariesPlus = salaries + 5000
print(salaries)
print(salariesPlus)