# Author: Dimgba Martha O
# @martha_samuel_
# 30  The loop function is similar to range(), but handles the parameters somewhat differently: it takes in 3 parameters
# : the starting point, the stopping point, and the increment step. When the starting point is greater than the
# stopping point, it forces the steps to be negative. When, instead, the starting point is less than the stopping point,
# it forces the step to be positive. Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line
# , space-separated string of numbers. For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0)
# should return 1 2 3 4
def loop(start, stop, step):
    count=start
    return_string = ''
    if step == 0 and count<0:
        step=-1
    if step==0 and count>0:
        step =1

    if count>stop:
        step=abs(step)*-1
    else:
        step = abs(step)
    for count in range (count, stop, step):
        return_string += str(count) + ' '
    return return_string.strip()
print(loop(11, 2, 3))
print(loop(1, 5, 0))
print(loop(-1, -2, 0))