# Author: Dimgba Martha O
# @martha_samuel_
# 23  this prints the nth fibonacci number using rcursions. fibonacci numbers is a set of numbers which start with 2 1's
# and the next number in the sequence are the sum of the first two numbers.
def fibonacci(x):
    if x <= 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


print(fibonacci(7))
for x in range (1, 15):
    print(fibonacci(x))