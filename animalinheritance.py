# Author: Dimgba Martha O
# @martha_samuel_
# 54   samples inheritance in animals
class Animal:
    name=''
    category=''
    def __init__(self,name):
        self.name=name
    def setcategory(self,category):
        self.category=category
class Turtle(Animal):
    name='Turtle'
    category='reptile'
turtle=Turtle('Turtle')
print(Turtle.category)
class Snake(Animal):
    name='snake'
    category=Turtle.category
snake=Snake('Snake')
print(Snake.category)




#Using composition
class Zoo:
    def __init__(self):
        self.current_animals={}
    def addanimal(self,animal):
        self.current_animals[animal.name]=animal.category
    def totalofcategory(self,category):
        result=0
        for animal in self.current_animals.values():
            if animal == category:
                result+=1
        return result
zoo=Zoo()
turtle=Turtle('Turtle')
snake=Snake('Snake')
zoo.addanimal(turtle)
zoo.addanimal(snake)
print(zoo.totalofcategory('reptile'))