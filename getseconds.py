# Author: Dimgba Martha O
# @martha_samuel_
# 04  this code converts hr,min,secs to seconds only


def get_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + minutes


amount_a = get_seconds(3, 40, 10)
amount_b = get_seconds(0, 47, 45)
result = amount_a + amount_b
print(str(result) + ' seconds')
