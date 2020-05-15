# Author: Dimgba Martha O
# @martha_samuel_
# 17  This calculates average of a list
values = [23,52,59,37,48]
average = sum(values) / len(values)

print('The average of values = ' + str(average))




#method 2
values = [24,76,98,45]
sum = 0
length = 0
for value in values:
    length += 1
    sum += value

print('The average of values = ' +str(sum/length))