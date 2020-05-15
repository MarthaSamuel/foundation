# Author: Dimgba Martha O
# @martha_samuel_
# 37   this creates a new list containing one person per string including their name and email address between angled
# brackets
def full_emails(people):
    result = []
    for email, name in people:
        result.append('{} <{}>'.format(name, email))
    return result


print(full_emails([('alex@eg.com', 'Alex Dirgo')]))
