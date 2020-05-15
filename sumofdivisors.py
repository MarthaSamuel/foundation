## Author: Dimgba Martha O
# @martha_samuel_
# 12   this code prints sum of all divisors without the number itself. zero should have no divisor
def sum_divisor(number):
   if number == 0:
        return 0

   divisor = [1]
   for divisors in range (2, number - 1):
       if number % divisors == 0:
           divisor.append(divisors)
   return sum(divisor)





print(sum_divisor(3))
print(sum_divisor(0))
print(sum_divisor(36))
