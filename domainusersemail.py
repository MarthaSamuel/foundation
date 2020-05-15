# Author: Dimgba Martha O
# @martha_samuel_
# 43   The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values
def email_list(domains):
    emails =[]
    index = 0
    for domain in domains:
        for user in domains[domain]:
            emails.insert(index, user + '@' + domain)
            index +=1
    return(emails)
print(email_list({'gmail.com':['clark.ken','diana.prince','peter.parker'],
                  'yahoo.com':['barbara.gordon','jean.gray'],'hotmail.com':
                  ['bruce.wayne']}))
