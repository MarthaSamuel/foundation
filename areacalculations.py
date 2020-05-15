# Author: Dimgba Martha O
# @martha_samuel_
# 03 finding area of a rectangle
length = 10
width = 2
Area = length * width
print('The area of the rectangle is ' + str(Area))


# finding sum of two areas using definitions
def area_triangle(base, height):
    return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum_area = area_a + area_b
print('The sum of both areas are : ' + str(sum_area))



# Area of a cirle

def area_circle(radius):
    pi = 3.14
    return pi*(radius**2)


print(area_circle(5))
