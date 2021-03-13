# This program counts how many time the program has been run and increases the count with each run
# Author: Stefanie Steffens

filename = "count.txt"

def readNumber():
    with open (filename, "rt") as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number))

num = readNumber()

writeNumber(num+1)

numNew = readNumber()
print("We have run this program {} times".format(numNew))
