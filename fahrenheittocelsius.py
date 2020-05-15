# Author: Dimgba Martha O
# @martha_samuel_
# 33  this converts from fahrenheits to celsuis
def to_celsuis(x):
    return(x-32)*5/9
for x in range(0, 101,10):
    print(x, to_celsuis(x))
    print('{:>3}F |{:>6.2f}C'.format(x, to_celsuis(x)))
