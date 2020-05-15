# Author: Dimgba Martha O
# @martha_samuel_
# 07 converting miles to km

def convert_distance(miles):
    km = miles * 1.6
    result = '{} miles equals {:.1f} km'.format(miles, km)
    return result


print(convert_distance(12))
print(convert_distance(5.5))

my_trip_miles = 5.5
my_trip_km = my_trip_miles * 1.6
print('The distance in km is : ' + str(my_trip_km))
