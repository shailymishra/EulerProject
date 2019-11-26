# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


#how to find factors.... first find the square root

#did correct in the first try
import math


def findfactors( n ):
    factors = []
    sqrtofN = math.sqrt(n)
    count = math.ceil(sqrtofN)
    while(count>1):
        if(n%count ==0):
            factors.append(count)
            factors.append(math.ceil(n/count))
        count = count-1
    return factors

def findLargestPrimeFactor(n):
    largest = 0
    sqrtofN = math.sqrt(n)
    count = math.ceil(sqrtofN)
    # loop will go from sqrtOfN till 2
    while(count>1):
        # if count is a factor of n then we find small and large factor. if large factor is prime, then its the largest
        # and we break from while loop.
        # if small factor is largest prime till now, we keep continuing, because maybe we might find a larger prime factor
        if(n%count == 0):
            smallerfactor = count
            largerfactor = n/count
            factorsOflargerfactor = findfactors(largerfactor)
            if not factorsOflargerfactor:
                largest = (largest<= largerfactor) and largerfactor or largest  
                break
            
            factorsOfsmallerfactor = findfactors(smallerfactor)
            if not factorsOfsmallerfactor:
                largest = (largest<= smallerfactor) and smallerfactor or largest  
        count = count-1
    
    print(largest)
    return largest
    
findLargestPrimeFactor(600851475143)
