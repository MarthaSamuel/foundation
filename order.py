# Author: Dimgba Martha O
# @martha_samuel_
# 08 this function compares two numbers and returns them in increasing order

def order_numbers(number1, number2):
    if number1 > number2:
        return number2, number1
    else:
        return number1, number2


print(order_numbers('cat', 'Cat'))
print(order_numbers('Yellow', 'cyan'))
print(order_numbers(108, 88))
print(order_numbers(5, 5))
