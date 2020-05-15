# Author: Dimgba Martha O
# @martha_samuel_
# 31  we use this function to replace old domain with new domain in any outdated email addresses
def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email