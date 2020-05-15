# Author: Dimgba Martha O
# @martha_samuel_
# 14  This code finds numbers that are powers of 2

def power_of_two(n):
    count = 0
    while n % 2 == 0 and n!= 0:
        n/=2
        count += 1
    print('Power is : ' + str(count))
    if n == 1:
        return True
    return False



print(power_of_two(0))
print(power_of_two(1))
print(power_of_two(256))
print(power_of_two(2048))



