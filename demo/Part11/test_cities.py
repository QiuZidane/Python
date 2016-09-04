import unittest
from Part11.P11_1 import cityName


class MyTestCase(unittest.TestCase):
    def test_city_country(self):
        cityname = cityName('guangzhou', 'china', 10000000)
        self.assertEqual(cityname, 'Guangzhou, China - population:10000000')


unittest.main()
