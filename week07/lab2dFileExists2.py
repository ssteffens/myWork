# This program checks whether a file exists -  as per lab solution. If the file exists, the content is updated to 0.
# Author: Stefanie Steffens

import os.path
filename = "count.txt"

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number))

if not os.path.isfile(filename): 
    print("File does not exist")
else:
    writeNumber(0)