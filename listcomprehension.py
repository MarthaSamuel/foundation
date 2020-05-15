# Author: Dimgba Martha O
# @martha_samuel_
# 38   This experiments with list comprehensions
# to create a list from 7 to 70
multiples =  []
for x in range (1, 11):
    multiples.append(x * 7)
print(multiples)
# using list comprehensiom
multiples = [ x * 7 for x in range (1, 11)]
print(multiples)



# to find the length of each of these languages using list comprehension
languages = ['Python', 'Pearl', 'Ruby', 'Go', 'Java', 'C']
lengths = [len(language) for language in languages]
print(lengths)




# listing multiples of 3
multiplesof3= [y for y in range (0, 101) if y % 3 ==0]
print(multiplesof3)



#  list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end,
#  and returns a list of squares of consecutive numbers between start and end inclusively
def squares(start, end):
    return[n*n for n in range (start, end+1)]
print(squares(0, 10))