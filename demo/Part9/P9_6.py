from Part9.P9_1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['AAA', 'BBB', 'CCC']

    def showFlavors(self):
        print(self.flavors)

icecream1 = IceCreamStand('baiyun_hotel', 'CAIPU')
icecream1.showFlavors()

