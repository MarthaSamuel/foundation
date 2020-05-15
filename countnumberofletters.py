# Author: Dimgba Martha O
# @martha_samuel_
# 41   this counts how many times each  letter appears in a text
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result :
            result [letter] = 0#we initialize an entry for the word in the dict
        result[letter]+=1
    return result
print(count_letters('a long string with a lot of letters'))




#count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or
# punctuation. Upper case should be considered the same as lower case.
def countletters(text):
    result ={}
    text=text.casefold()
    for letter in text:
        if letter.isalpha():
            if letter not in result:
                result[letter]=0
            result[letter] +=1
    return result
print(countletters('This is a sentence! 2+2=4.'))