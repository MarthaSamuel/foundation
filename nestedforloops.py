# Author: Dimgba Martha O
# @martha_samuel_
# 19   This prints dominoes game tiles, it prints either 3/2 or 2/3 for 2 and 3
for left in range (7):
    for right in range (left, 7):
        print('['+str(left)+'|'+str(right)+']',end='')
        print()