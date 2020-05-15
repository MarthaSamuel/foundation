# Author: Dimgba Martha O
# @martha_samuel_
# 21   this uses recursions to find factorials
def factorials(n):
    if n > 1:
        return n * factorials(n - 1)
    else:
        return 1


print(factorials(5))
