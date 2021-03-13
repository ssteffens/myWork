# This program reads in a number from an existing text file using a function
# Author: Stefanie Steffens

filename = "count.txt"

def readNumber():
    with open (filename, "rt") as f:
        number = int(f.read())
        return number

num = readNumber()
print(num)