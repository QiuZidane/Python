# -*- coding: utf-8 -*-
class Restaurant:
    def __init__(self, restaurant_name='', cuisine_type=''):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('restaurant_name = ' + self.restaurant_name)
        print('cuisine_type = ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + ' is open now')


res1 = Restaurant('motel168', 'food')
res1.describe_restaurant()
res1.open_restaurant()
