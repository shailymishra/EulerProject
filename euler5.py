# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## 
## Need to find LCM of all the numbers

## Start taking two numbers serially
## x,y and so we find its gcd and then lcm becomes x.y // gcd


## Can make gcd logic better. check online
def gcd(number1,number2):
    if(number1>number2):
        rem = (number1%number2)
    else:
        rem = (number2%number1)
    if(rem == 0 ):
        if(number1 > number2):
            return number2
        else:
            return number1
    else:
        return gcd(number2,rem)


def LCM(listOfNumbers):
    lcmvalue = 1
    for number in listOfNumbers:
        gcdValue = gcd(lcmvalue,number)
        lcmvalue = (lcmvalue*number) // gcdValue
    return lcmvalue

print(LCM(range(1,20)))





