# Author: Dimgba Martha O
# @martha_samuel_
# 46   The format_address function separates out parts of the address string into new strings: house_number and
# street_name, and returns: "house number X on street named Y"
def format_address(address_string):
    house_number=''
    street_name=''
    address= address_string.split()
    for part in address:
            if part.isnumeric():
                house_number+=part
            else:
                street_name+=part
                street_name+=''
    return 'house number {} on street named {}'.format(house_number,street_name)
print(format_address('123 Main Street'))
print(format_address('1001 1st Ave'))
