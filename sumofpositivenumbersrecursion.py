# Author: Dimgba Martha O
# @martha_samuel_
# 22   This prints the sum of positive numbers using recursions
def sum_positive_nos(p):
    if p < 1:
        return 0
    else:
        return p + sum_positive_nos(p-1)

print(sum_positive_nos(5))
