# This program reads in a number and rounds it upwards to the nearest integer
# Author: Stefanie Steffens

# First need to import math module
import math

numberToCeil = float(input("Enter a float number: "))
ceiledNumber = math.ceil(numberToCeil)
print('{} rounded up is {}.'.format(numberToCeil, ceiledNumber))