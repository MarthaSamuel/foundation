# Author: Dimgba Martha O
# @martha_samuel_
# 27   This prints the number of digits in a number
def digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        n //= 10
        count += 1
    return count


print(digits(1325))
