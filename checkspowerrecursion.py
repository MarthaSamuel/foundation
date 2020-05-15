# Author: Dimgba Martha O
# @martha_samuel_
# 25    This checks if a number is a power of a given base using recursion
def is_power_of(number, base):
    if number == 1: # base case always comes first
        return True
    if number < base:
        return False
    number /= base
    return is_power_of(number, base)


print(is_power_of(169, 13))
print(is_power_of(70, 7))




# *this code checks power without using recursion method
def ispower(number, base):
    while number % base == 0:
        number/=base
        if number == 1:
            return True
    if number < base:
        return False
    else:
        return False


print(ispower(128, 2))
print(ispower(70, 6))
