# This program will generate prime numbers using a function
# Author: Stefanie Steffens

import math

primes = []
upto = 101

#Function
def isPrime(candidate):
    # check if it is a prime
    for divisor in range(2, math.floor(math.sqrt(candidate))):
        if candidate % divisor == 0: 
            return False
    return True


candidates = range(2,upto+1)

# Call function
for candidate in candidates:
    if isPrime(candidate):
        primes.append(candidate)
print (primes)