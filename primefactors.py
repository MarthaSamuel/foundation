# Author: Dimgba Martha O
# @martha_samuel_
# 11  this code prints the prime factors of given numbers
def prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number /= factor
        else:
            factor += 1



prime_factors(100)
prime_factors(450)