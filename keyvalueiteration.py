# Author: Dimgba Martha O
# @martha_samuel_
# 42   iterating through keys and values of dictionary
cool_beasts = {'octopus': 'tentacles', 'dolphins':'fin', 'rhinos':'horns'}
for beasts, features in cool_beasts.items():
    print('{} have {}'.format(beasts, features))




#
wardrobe = {'shirt' : ['red','blue','white'], 'jeans':['blue','black']}
for wears, colors in wardrobe.items():
    for color in colors:
        print('{} {}'.format(color, wears))