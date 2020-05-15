# Author: Dimgba Martha O
# @martha_samuel_
# 49    Taylor and Rory are hosting a party. They sent out invitations,
# and each one collected responses into dictionaries, with names of their friends and how many guests each friend is
# bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests.
# this code combines both dictionaries into one, with each friend listed only once, and the number of guests from
# Rory's dictionary taking precedence, if a name is included in both dictionaries.
def combineguests(guests1, guests2):
    guests2.update(guests1)
    return guests2

Rorysguests = {'Adam':4, 'Brenda':2,'David':1,'Jose':3,'Robert':4}
Taylorsguests = {'David':4,'Nancy':1,'Robert':2,'Adam':1,'Sam':5}

print(combineguests(Rorysguests, Taylorsguests))

