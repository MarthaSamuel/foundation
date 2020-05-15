# Author: Dimgba Martha O
# @martha_samuel_
# 50  This code shows that when 2 people who have 1 orange each exchange their oranges they will have 1 orange each but
# when they exchange an idea they will have 2 ideas each.Famoue quote by George Bernard
class Person:
    pass

class Person:
    apples =0
    ideas =0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    joh = martin.apples
    mart=johanna.apples
    you.apples=joh
    me.apples=mart
    return you.apples, me.apples

def exchange_ideas(you, me):
    you.ideas = martin.ideas + johanna.ideas
    me.ideas=you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print('Johanna has {} apples and Martin has {} apples'.format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print('Johanna has {} ideas and Martin has {} ideas'.format(johanna.ideas, martin.ideas))

