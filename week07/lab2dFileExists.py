# This program checks whether a file exists
# Author: Stefanie Steffens

import os

filename = "count.txt"

if(os.path.exists(filename)): 
    print("File exists")
else:
    print("Does not exist")