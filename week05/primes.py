# This program will generate prime numbers
# Author: Stefanie Steffens

primes = []
upto = 101

for candidate in range(2,upto):
    #print (candidate)
    isPrime = True
    # only need to check if divisible by prime
    for divisor in primes:
        # if divisible by an int it is not a prime number
        if (candidate % divisor == 0): 
            isPrime = False
            # so there is no reason to keep checking
            break

    if isPrime: 
        primes.append(candidate)
print (primes)