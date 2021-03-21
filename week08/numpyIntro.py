# Numpy introduction

import numpy as np

listOfNumbers = [1, 2, 3, 6]
numbers = np.array([1,2,4,5])

# To add 3 to all values in numpy array: 
# numbers = numbers + 3

# To multiply all values in numpy array by 3
# numbers = numbers * 3

# To multiply values with values of another array: 
# numbers = numbers * np.array([1,4,5,6])

print(listOfNumbers)
print(numbers)


# Random number generator: Enter number range to, from and how many random numbers should be returned
randomNumbers = np.random.randint(100, 200, 5)
print(randomNumbers)

# Random number generator - Normal Distribution: 
normDistribution = np.random.normal(size = 10)
print(normDistribution)


