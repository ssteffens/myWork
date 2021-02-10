# This program prints out a random fruit
# Author: Stefanie Steffens

import random

fruits = ['Apple', 'Banana', 'Orange', 'Cherry', 'Blueberry', 'Strawberry']

# To display a random number between 0 and length of list - 1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))