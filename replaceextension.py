# Author: Dimgba Martha O
# @martha_samuel_
# 38   Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
filenames = ['program.c', 'studio.hpp', 'sample.hpp', 'a.out', 'math.hpp', 'hpp.out']
# using list comprehension
newfilenames = [(filename[:-2] if filename[-2:]=='pp' else filename) for filename in filenames]
print(newfilenames)
# using for loops
newfilenames=[]
for x in range (len(filenames)):
    old_name=filenames[x]
    if old_name.endswith('.hpp'):
        new_name=old_name.replace('hpp', 'h')
    else:
        new_name=old_name
    newfilenames.append(new_name)

print(newfilenames)
