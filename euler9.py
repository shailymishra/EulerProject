# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

## Making complexity O(n^2)
## combining the two formula => 2000a+2000b-2ab-(1000)^2 = 0

a = range(1,999) ## minimum can be 1 and max is been 998
b = range(1,999)
conditionMet = False
productvalue = 1
print('True')
for avalue in a:
    for bvalue in b:
        if((2000*avalue + 2000*bvalue - 2*avalue*bvalue - 1000000) == 0):
            conditionMet = True
            cvalue = 1000-avalue-bvalue
            productvalue = avalue * bvalue * cvalue
            print('a', avalue)
            print('b', bvalue)
            print('c', cvalue)
            print('Answer is ', productvalue )
            break
    if(conditionMet):
        break

print('End')