# Author: Dimgba Martha O
# @martha_samuel_
# 48  A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they
# arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the
# class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them
# into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order.
# the code combines them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse
# order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
    newlist = list2
    revlist1= reversed(list1)
    newlist += revlist1
    return newlist
Jamies_list = ['Alice','cindy','bobby','Jan','Peter']
Drews_list = ['mike','carol','Greg','Marcia']
print(combine_lists(Jamies_list,Drews_list))