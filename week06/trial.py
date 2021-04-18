
number = 20
squarelist = []

# Approach/Consideration 1: Need to determine the integer square number smaller than number and identify 
# the root. 
# Does not work for numbers < 1 because the squarelist would get populated with 0, i.e. X0 would be 0
# and formula would be invalid as divisor 2*x0 would result in 0. Therefore, for numbers <1, x0 is set to 1.


if number < 1:
    squarelist.append(1)
else: 
    for i in range(0,round(number+1)):
        square = i*i
        if square > number:         
            break
        squarelist.append(i) 
        

print(squarelist)

x0 = squarelist[-1]
#lowerNumber = squarelist[-2]
#print(lowerNumber, higherNumber)

# Square root estimation function: 
#Trying to find where f(x) = x**2 - a equals 0

#Formula as per: https://en.wikipedia.org/wiki/Newton%27s_method#Square_root

#x1 = x0 - (f(x0)/f'(x0)) = x0 - ((x0**2 - a)/(2*x0)
# The result of x1 is then reentered into the formula (need loop) to calculate x2, etc. 

sqrt = x0 - ((x0 ** 2 - number)/(2*x0))
print(sqrt)


# Number of iterations: 5
xprev = x0
count = 1

while count < 6: 
    xnew = xprev - ((xprev ** 2 - number)/(2*xprev))
    xprev = xnew
    print(xnew)
    count += 1
    if number%xprev == 0:
        break


