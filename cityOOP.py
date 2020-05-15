# Author: Dimgba Martha O
# @martha_samuel_
# 51  This returns the name of the city and its country (separated by a comma), when comparing the 3 defined instances
# for a specified minimal population
class City:
    pass
# initializing attributes
class City:
    name =''
    country=''
    elevation = 0
    population = 0
# instances of class and its attributes
city1=City()
city1.name='Cusco'
city1.country='Peru'
city1.elevation=3399
city1.population=358052

city2=City()
city2.name='Sofia'
city2.country='Bulgaria'
city2.elevation=2290
city2.population=1241675

city3=City()
city3.name='Seoul'
city3.country='South Korea'
city3.elevation = 38
city3.population=9733509

def max_elevation_city(min_population):
    #initialize the variable that will hold the name of the city with highest elevation
    return_city = City()
    # we want the city that has the min population and highest elevation
    if city1.population>=min_population and city1.elevation>return_city.elevation:
        return_city = city1
    if city2.population>=min_population and city2.elevation>return_city.elevation:
        return_city = city2
    if city3.population>=min_population and city3.elevation>return_city.elevation:
        return_city = city3

    if return_city.name:
        return '{}, {}'.format(return_city.name, return_city.country)
    else:
        return ''

print(max_elevation_city(100000))
print(max_elevation_city(1000000))
print(max_elevation_city(10000000))





