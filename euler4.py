# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


## Also in recurrsive function return the function, otherwise it will show none

## Have a palindrome function 889x11 = 9779 which then becomes largest  palindrome
## This logic failed - because 
## Find the max no i.e. 999x999
## Divide it by 111, and get the max number
## now keep decreasing that number, and multiply with 111 till we have a palindrome

## Logic 2  :: FAILED
## obviously for a palindrome it , one of the multiplicant will be 99,999, ...
## so just keep reducing it , and keep checking
## this also didnt work, because 999x91 = 90909, now there will be obviously better palindrome
import math

def palindrome(value):
    length = len(value)
    if(length>1):
        if(value[0] == value[length-1]):
            return palindrome(value[1:length-1])
        else:
            return False
    else:
        return True


numberOfDigit = 3
string = ''
for i in range(numberOfDigit):
    string += '9'

multiplicant1 = int(string)
multiplicant2 = multiplicant1
while(True):
    multiplication = multiplicant1 * multiplicant2
    if(palindrome(str(multiplication))):
        print('found', multiplication)
        print('multiplicant1', multiplicant1)
        print('multiplicant2', multiplicant2)
        break
    multiplicant2 -= 1
