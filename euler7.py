##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
## What is the 10 001st prime number?

## write method to find prime
## and then keep finding until you find

import math
def isPrime(n):
    sqrtn = math.ceil(math.sqrt(n))
    for i in range(2,sqrtn+1):
        if(n%i == 0):
            return False
    return True


def findTheNextPrime(start):
    i = start+1
    while(not isPrime(i)):
        i += 1
    return i

print(findTheNextPrime(7))

limit = 10001
# limit = 6
currPrineNumber = 2
counter = 1
while(counter<limit):
    print(currPrineNumber)
    currPrineNumber = findTheNextPrime(currPrineNumber)
    counter += 1
print(currPrineNumber)

