# Variable scope
# Author: Stefanie Steffens

# variables defined within a function can only be used within that function

def cube(num):
    var = 66
    print ("in function var is", var)
    return num**3

var = cube(22)
print("outside function var is", var)