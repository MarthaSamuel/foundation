# Author: Dimgba Martha O
# @martha_samuel_
#  10 using loops

x = 0
while x < 5:
    print('Not there yet. x = ' + str(x))
    x += 1
print('x = ' + str(x))


# prints number of attempts
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)




# this code adds the first n numbers and also gives product of first n numbers
x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

x = 1
product = 1
while x < 10:
    product *= x
    x += 1


print(sum, product)




# using for loops for cubes
for y in range(1, 11):
    print(str(y**3))



#using for loops for finding multiples of 7
for s in range (1, 100):
    if s%7==0:
        print(s)
