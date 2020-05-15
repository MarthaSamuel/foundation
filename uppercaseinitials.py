# Author: Dimgba Martha O
# @martha_samuel_
# 34    this prints out initials of phrase in uppercase
def initials(phrase):
    words = phrase.split()
    result = ''
    for word in words:
        result += ''.join([word[0].upper()])
    return result


print(initials('Universal Series Bus'))
print(initials('local area network'))



# this code returns first name and second name as initial
def nametag(first_name, last_name):
    return(first_name+' '+'{:.1s}.'.format(last_name))
print(nametag('Jane', 'Smith'))
print(nametag('Emekwo', 'Ukoha'))
print(nametag('Martha-Samuel', 'Dimgba'))