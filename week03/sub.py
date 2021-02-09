# This program reads in two numbers and subtracts the first one from the second one
# Author: Stefanie Steffens

# As the input reads in a string, it needs to be converted to an int so that mathematical 
# operation can be performed

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
answer = number2 - number1
print('{} minus {} is {}'.format(number2, number1, answer))