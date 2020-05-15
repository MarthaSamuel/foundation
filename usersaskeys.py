# Author: Dimgba Martha O
# @martha_samuel_
# 44    The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. this code return a dictionary with the users as keys and a list of their
# groups as values.
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            user_groups[user] = user_groups.get(user, []) + [group]
    return(user_groups)
print(groups_per_user({'local':['admin','userA'], 'administrator':['admin']}))