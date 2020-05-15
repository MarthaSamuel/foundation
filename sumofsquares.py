# Author: Dimgba Martha O
# @martha_samuel_
# 16  This finds the sum of squares
def sum_squares(n):
    squares = []
    for x in range (0, n+1):
        result= x * x
        squares.append(result)
    return sum(squares)


print(sum_squares(4))