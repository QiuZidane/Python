def cityName(city, country, population=''):
    citycondition = city.title() + ', ' + country.title() + ' - population:' + str(population)
    print('the citycondition is : ' + citycondition)
    return citycondition

# cityName('santiago', 'chile')
