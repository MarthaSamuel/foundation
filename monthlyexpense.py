# Author: Dimgba Martha O
# @martha_samuel_
# 06 this code can do a simple calculation and help give a monthly report on cost if rate is constant
def print_monthly_expense(month, hours):
    cost = hours * 0.65
    return 'The monthly expense for ' + month + ' is ' +'$'+str(cost)
print(print_monthly_expense('June', 345))
print(print_monthly_expense('July', 491))
print(print_monthly_expense('August', 215))