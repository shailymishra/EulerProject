#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
#  and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

## Time taken : really quick  : like in 5 mins

## for n natural number
def findSumOfSquare(n):
    return n*(n+1)*(2*n+1) // 6

def findSquareOfSum(n):
    return (n*(n+1) //2 )**2

sumOfSquare = findSumOfSquare(100)
sqaureOfSum = findSquareOfSum(100)
print('sumOfSquare',sumOfSquare)
print('sqaureOfSum',sqaureOfSum)
print('answer:',  sqaureOfSum - sumOfSquare )