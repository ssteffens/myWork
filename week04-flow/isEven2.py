# This program prompts to user to enter a number and outputs whether the number is even or odd. 
# The program keeps prompting to enter a number until the user enters -1
# Author: Stefanie Steffens

number = int(input('Enter a number (-1 to quit): '))
while number != -1:
    if (number % 2) == 0:
        print("{} is an even number".format(number))
    else:
        print("{} is an odd number".format(number))
    number = int(input('Enter another number (-1 to quit): '))