# This program floors a float number = rounds it downwards to the nearest integer
# Author: Stefanie Steffens

# First need to import math module
import math

numberToFloor = float(input("Enter a float number: "))
flooredNumber = math.floor (numberToFloor)
print ('{} floored is {}'.format(numberToFloor, flooredNumber))