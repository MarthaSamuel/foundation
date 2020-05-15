# Author: Dimgba Martha O
# @martha_samuel_
# 36     The replace_ending function replaces the old string in a sentence with the new string, but only if the
# sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the
# one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz,
# not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return
# abcabc (no changes made).
def replace_ending(sentence, old, new):
    if sentence.endswith(old) and sentence[-3:-1]==old[-3:-1]:
    # using i as thr slicing index, combine the part of the the sentence uo to the matched string at the end with the
# new string
        i = sentence.rfind(old[0:])
        new_sentence = sentence[ :i]+new
        return new_sentence
    return sentence


print(replace_ending('its`s raining cats and cats', 'cats', 'dogs'))
print(replace_ending('She sells seashells by the seashore', 'seashells', 'donuts'))
print(replace_ending('The weather is nice in May', 'may', 'april'))
print(replace_ending('The weather is nice in May', 'May', 'April'))