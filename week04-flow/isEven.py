# This program reads in a number and outputs whether the number is even or odd
# Author: Stefanie Steffens

number = int(input('Enter a number: '))

if (number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))