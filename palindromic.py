# Author: Dimgba Martha O
# @martha_samuel_
# 35   this code checks if a string is palindromic. Spaces and letters are ignored.
# A palindrome is a string that can be equally read from left to right or right to left,
# omitting blank spaces, and ignoring capitalization
def palindrome(input_string):
    new_string = input_string.casefold()
    new_string = ''.join(new_string.split())
    reverse_string = reversed(new_string)
    if list(new_string)==list(reverse_string):
        return True
    return False
print(palindrome('Never Odd or Even'))
print(palindrome('abc'))
print(palindrome('kayak'))