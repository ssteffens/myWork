# This program reads in two numbers and divides the first one by the second. 
# The result is given as an integer and the remainder. 
# Author: Stefanie Steffens

number1 = int(input('Enter first number: '))
number2 = int(input('Enter the number you want to divide by: '))
answer = int(number1/number2)
remainder = number1%number2

print('{} divided by {} is {} with remainder {} '.format(number1, number2, answer, remainder))