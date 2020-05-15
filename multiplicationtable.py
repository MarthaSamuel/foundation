# Author: Dimgba Martha O
# @martha_samuel_
# 15 This writes multiplication table from 1 to 5 of a number with result < 25
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + 'x' + str(multiplier) + '=' + str(result))
        multiplier += 1


print(multiplication_table(9))
print(multiplication_table(3))




# This function prints out a multiplication table (where each number is the result of multiplying the first number
# of its row by the number at the top of its column)
def multiplicationtable(start, stop):
    for x in range (1, 4):
        for y in range (1, 4):
            print(str(x*y),end=' ')
        print()
multiplicationtable(1, 3)