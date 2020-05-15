# Author: Dimgba Martha O
# @martha_samuel_
# 24 This prints the result when a given number is raised to a given power
def power(base, exp):
    if exp == 0:
        return 1
    elif exp == base:
        return base
    else:
        return base * base ** (exp - 1)


print(power(5, 3))
