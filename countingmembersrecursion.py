# Author: Dimgba Martha O
# @martha_samuel_
# 26   This recursively counts the amount of users that belong to a group in a system going through each member of
# a group  and if one of them is a group, recursively calling the function and counting the members.
def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member)-1
    return count

print(count_users('sales'))
#this exerpt from a code just demonstrates recursion and wont run because
# some functions are undefined