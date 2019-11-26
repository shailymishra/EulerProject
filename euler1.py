# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# find all 3 multiple
# 3,6,9...till 1000. 1000/3, and find how many.
# 5
# 15

#Mistake 1 : first just add everything to sum, 
#Mistake 2 : i took while condition as <= limit

limit = 1000
multipleof3 = 3
count = 0
sum=0
while(multipleof3<limit):
    count=count+1
    sum = sum + multipleof3
    multipleof3 = multipleof3+3
multipleof5 = 5
while(multipleof5<limit):
    count=count+1    
    sum = sum + multipleof5
    multipleof5 = multipleof5+5

multipleof15 = 15
while(multipleof15<limit):
    count=count+1
    sum = sum - multipleof15
    multipleof15 = multipleof15+15

print ("Sum",sum)
print ("Count",count)
