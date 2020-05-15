# Author: Dimgba Martha O
# @martha_samuel_
# 28   The counter function counts down from start to stop when start is bigger than stop,
# and counts up from start to stop otherwise
def counter(start, stop):
    x = start
    if x > stop:
        return_string = 'Counting down: '
        while x >= stop:
            return_string += str(x)
            if x > stop:
                for x in range(x-1, stop-1, -1):
                #x-=1
                    return_string += ',' + str(x)
            break
    else:
            return_string = 'Counting up: '
            while x <= stop:
                return_string += str(x)
                if x<stop:
                    for x in range(x+1, stop+1):
                        #x+=1
                        return_string += ',' + str(x)

                break
    return return_string
print(counter(1, 10))
print(counter(2, 1))
print(counter(5, 5))