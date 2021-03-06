# Functions with flexible arguments
# Author: Stefanie Steffens

print ("hi", 55, 343, {}, sep=":")

# flexible number of arguments are indicated by *

def average(*numbers):
    sumOf = sum(numbers)
    return sumOf / len(numbers)

ave = average(12,12, 343234, 234)
print ("average is", ave)


# flexible number of names arguments

def fun(arg1 = 0, arg2 = 1): 
    return arg1 - arg2

print (fun(10)) # if arguments are not specified, defined arguments are used (arg1 = 0, arg2 = 1)


def funkyArgs(**args):
    print (args)

funkyArgs(name = "Joe", age = 33, courses = [])