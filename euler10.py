# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# keep finding primes till 2m
# Modified the code 
# Need to find a better solution
import math
def isPrime(n):
    sqrtn = math.ceil(math.sqrt(n))
    for i in range(2,sqrtn+1):
        if(n%i == 0):
            return False
    return True


def findTheNextPrime(start):
    i = start+1
    print(i)
    while(not isPrime(i)):
        i += 1
    return i


# limit = 2000000
limit = 10
currPrineNumber = 2
sumvalue = 0
while(currPrineNumber<limit):
    sumvalue += currPrineNumber
    currPrineNumber = findTheNextPrime(currPrineNumber)

print(sumvalue)

