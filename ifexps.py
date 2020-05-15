# Author: Dimgba Martha O
# @martha_samuel_
#  09 using if statements

def hint_username(username):
    if len(username) < 4:
        print('Invalid username.Must be more than 4 characters long')
    elif len(username) > 13:
        result = 'Invalid username.Must be at most 13 characters long'
        return result
    else:
        print('Valid Username')


def put_username(result):
    if result == 'Invalid username.Must be at most 13 characters long':
        print(result + '\n' + ' Enter new password...\n')


put_username(hint_username('martha_samuel_'))
hint_username('Mekwos')
hint_username('Emy')


# this checks if a number is a positive number
def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(7))
print(is_positive(-4))


# this checks if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(19))
print(is_even(980))


# This returns whether the given number is positive, negative or zero
def real_number(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Zero'


print(real_number(-8))
print(real_number(15))
print(real_number(0))


# this function recieves colors and prints their hexadecimal values
def color_translator(color):
    if color == 'green':
        hexadecimal = '#@00ff00'
    elif color == 'red':
        hexadecimal = '#ff0000'
    elif color == 'blue':
        hexadecimal = '#0000ff'
    else:
        hexadecimal = 'Unknown'
    return hexadecimal


print(color_translator('blue'))


# this code prints score above 95 as top score, score 60 and above as pass and below 60 is fail
def exam_grade(score):
    if score > 95:
        grade = 'Top score'
    elif score >= 60:
        grade = 'pass'
    else:
        grade = 'fail'
    return grade


print(exam_grade(99))
print(exam_grade(70))
print(exam_grade(30))


# this returns last name, then first name
def format_name(first_name, last_name):
    if first_name and last_name:
        return 'Name : ' + last_name + ',' + first_name
    elif first_name or last_name:
        return 'Name :' + last_name + first_name
    else:
        return ' '


print(format_name('Martha', 'Samuel'))
print(format_name('Emekwo', ''))
print(format_name('', 'Ukoha'))
print(format_name('', ''))


# this function is used for comparing words to return longest word
def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word2):
        word = word1
    elif len(word2) >= len(word3) and len(word2) >= len(word1):
        word = word2
    else:
        word = word3
    return word


print(longest_word('photo', 'photosynthesis', 'wallpaper'))


# this function returns only fractional part after division and if denominator is 0,we have 0, not error
def fractional_part(number, denominator):
    if denominator == 0:
        return 0
    else:
        return (number / denominator) - (number // denominator)


print(fractional_part(7, 0))
print(fractional_part(9, 4))
print(fractional_part(4, 4))


# this function shows off function in function
def Sum(x, y):
    return x + y


print(Sum(Sum(1, 3), Sum(4, 5)))
