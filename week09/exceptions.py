# This program demonstrates how to use try/except
# Author: Stefanie Steffens

# Syntax error:
# var = 2 +

# File not found error: 
# filename = "data.txt"
# with open(filename) as f: 
#    print(f.read())

# requires to enter the file name into command line after the programm.py. sys.argv[1] reads second file 
# on list in command line
import sys
filename = sys.argv[1]

try: 
    with open(filename) as f: 
        print(f.read())
    var = 10/0
# if run with file name that does not exist
except FileNotFoundError:
    print("File (", filename,") does not exist", sep = '') # sep removes blank spaces around file name
except ZeroDivisionError: 
    print("Division by 0 not allowed")
except: 
    print("An exception occurred")
finally: 
    print("The end")