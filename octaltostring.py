# Author: Dimgba Martha O
# @martha_samuel_
# 39  The permissions of a file in a Linux system are split into three sets of three permissions: read, write,
# and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing
# each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using
# the letters r, w, and x or - when the permission is not granted. For example: 640 is read/write for the owner, read
# for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----" 755 is read/write/
# execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
def octal_to_string(octal):
    result = ''
    value_letters = [(4, 'r'),(2, 'w'),(1, 'x')]
    for n in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if n>= value:
                result += letter
                n -= value
            else:
                result+='_'
    return result
print(octal_to_string(755))
print(octal_to_string(644))
print(octal_to_string(600))
