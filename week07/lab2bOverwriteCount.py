# This program overwrites a number in an existing file
# Author: Stefanie Steffens

filename = "count.txt"

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number))

writeNumber(0)