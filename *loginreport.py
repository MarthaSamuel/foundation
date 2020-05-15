# Author: Dimgba Martha O
# @martha_samuel_
# 57   this code creates a daily report that tracks the use of machines. it shows which users are curently logged in to
#which machines


def get_event_date(event):
    return event.date#we use this to sort the list
def current_users(events):#coding our sort function
    events.sort(key=get_event_date)#we sort our events using sort() and passing the fn we just created as key

    machine ={}#we create a dict to store names and users of machine before iterating list of events
    for event in events:
        #check if machine affected by event ,if not add list,an empty set as value
        if event.machine not in machines:
            machine[event.machine]==set()
        if event.type == 'login':
            machine[event.machine].add(event.user)#if event type is login we add user to list and viceversa
        elif event.type =='logout':
            machine[event.machine].remove(event.user)
    return machines# dict will contain machines we have seen as key with a set containing current users of machine as values.
def generate_report(machines):
    for machine,users in machines.items():#this returns both keys and values
        if len(users)>0:# this makes sure we dont print any machine where  nobody is currently logged in
            user_list=','.join(users)#we want tp print machine name followed by users
            print('{}: {}'.format(machine, user_list))

# to check our code is working wel,we create a an event claa
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date= event_date
        self.type = event_type
        self.machine=machine_name
        self.user=user


events=[Event('2020-01-21 12:45:56','login','myworkstation.local','jordan'),
Event('2020-01-22 15:45:07', 'logout','webserver.local','jordan'),
Event('2020-01-21 18:43:33', 'login', 'webserver.login','lane'),
Event('2020-01-22 13:55:22','logout','myworkstation.local','jordan'),
Event('2020-01-21 08-20-01','login','webserver.local','jordan'),
Event('2020-01-23 11:24:35', 'login','mailserver.local','Chris')]

user=current_users(events)
print(user)

generate_report(machines)
