# Author: Dimgba Martha O
# @martha_samuel_
# 53   # sample code on inheritance
class Clothing:
    stock={'name':[],'material':[],'amount':[]}
    def __init__(self,name):
        material=''
        self.name=name
    def additem(self,name,material,amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    def stockbymaterial(self,material):
        count=0
        n=0
        for item in Clothing.stock['material']:
            if item ==material:
                count+=Clothing.stock['amount'][n]
        return count

class Shirt(Clothing):
    material='cotton'
class Pant(Clothing):
    material='cotton'

polo=Shirt('Polo')
sweatpants=Pant('sweatPantS')
polo.additem(polo.name,polo.material,4)
sweatpants.additem(sweatpants.name,sweatpants.material,6)
currentstock=polo.stockbymaterial('cotton')
print(currentstock)