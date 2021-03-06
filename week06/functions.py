# Functions -  Cubes (Kubikzahl)
# Author: Stefanie Steffens


def cube(num):
    print ("in cube")
    return num ** 3

for i in range(1,11):
    print(i, "cubed is:", cube(i))