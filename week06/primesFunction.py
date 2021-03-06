# This program will generate prime numbers using a function
# Author: Stefanie Steffens

import math

primes = []
upto = 101

#Function
def isPrime(candidate):
    # check if it is a prime, if it is, return True (see line 15)
    for divisor in range(2, math.floor(math.sqrt(candidate))):
        if candidate % divisor == 0: 
            return False
    return True


candidates = range(2,upto+1)    # All numbers from 2 to "upto + 1" as indicated in line 7, +1 is required
                                # last number in range is exclusive

# Call function
for candidate in candidates:
    if isPrime(candidate):
        primes.append(candidate)
print (primes)