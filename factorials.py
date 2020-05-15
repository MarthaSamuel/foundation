# Author: Dimgba Martha O
# @martha_samuel_
# 18  This prints factorials of given numbers
def factorial(n):
    result = 1
    # or use result = n
    # for i in range (1, n):
    for i in range (1, n+1):
        result *= i
    return result
print(factorial(4))


for n in range (1, 10):
    print(n, factorial(n))