# This program reads in a number and outputs whether the number is even or odd
# Author: Stefanie Steffens

number = int(input('Enter a number: '))

# The program divided the entered number by 2 and determines whether the remained is 0 (so the number 
# is even or not (so the number is odd)
if (number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))