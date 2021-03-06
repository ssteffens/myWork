# Anonymous functions (lambda)
# Author: Stefanie Steffens

isMax = True
if isMax:   
    fun = lambda num : num * 2
else: 
    fun = lambda num: num * 3

var = fun(10)
print(var)