# This program keeps reading in numbers until the user enters a 0.
# All entered numbers are appended into a list. The program then prints out each of the numbers entered
# and the average of them. 
# Author: Stefanie Steffens

numbers = []

number = int(input("Enter a number (0 to quit) "))

while number !=0:
    numbers.append(number)
    number = int(input("Enter another (0 to quit):"))

for value in numbers: 
    print (value)

average = float(sum(numbers)) / len(numbers)
print("The average is {}".format(average))