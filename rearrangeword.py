# Author: Dimgba Martha O
# @martha_samuel_
# 40   this code turns text into pig latin: a simple text transformation that modifies each word moving the first
# character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
    say = ''
    words = text.split()
    for word in words:
        words = word[1:]+word[0]+'ay'+' '
        say+=''.join(words)
    return say
print(pig_latin('hello how are you'))