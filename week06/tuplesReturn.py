# Tuples as return types
# Author: Stefanie Steffens

def passBackTuple(): 
    return (1,2,3)


x, y, z = passBackTuple()
print("x is ", x, "y is", y)