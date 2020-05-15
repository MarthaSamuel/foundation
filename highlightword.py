# Author: Dimgba Martha O
# @martha_samuel_
# 47  The highlight_word function changes the given word in a sentence to its upper-case version.
def highlightword(sentence, word):
    return(sentence.replace(word,word.upper()))
print(highlightword('Have a nice day', 'nice'))