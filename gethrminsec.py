# Author: Dimgba Martha O
# @martha_samuel_
# 05 this code converts seconds to hr,mins,secs

def convert_seconds(seconds):
    Hour = seconds // 3600
    minute = (seconds - (Hour * 3600)) // 60
    seconds_left = seconds - Hour * 3600 - minute * 60
    return str(Hour) + 'hr ' + str(minute) + 'mins ' + str(seconds_left) + 'secs'
print(convert_seconds(2400))
print(convert_seconds(5000))
print(convert_seconds(32000))

