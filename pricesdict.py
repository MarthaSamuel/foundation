# Author: Dimgba Martha O
# @martha_samuel_
# 45   The add_prices function returns the total price of all of the groceries in the dictionary.
def add_prices(basket):
    total = 0
    for groceries,prices in basket.items():
        total += prices
    return round(total, 2)
groceries = {'bananas': 1.56, 'apples':2.50,'oranges':0.99,'bread':4.59}
print(add_prices(groceries))



# iterate through the keys and values of the car_prices dictionary,
def carlistings(car_prices):
    result =''
    for cars, prices in car_prices.items():
        result+='{} costs {} dollars'.format(cars, prices) + '\n'
    return result
print(carlistings({'Kia':19000,'lamborghini':55000}))