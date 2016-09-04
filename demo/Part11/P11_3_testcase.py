import unittest
from Part11.P11_3 import Employee as EPL


class P11_3_TestCase(unittest.TestCase):
    def setUp(self):
        self.employee = EPL('zidane', 200000)

    def test_give_default(self):
        default_income = self.employee.get_income()
        self.assertTrue(default_income)
        self.assertEqual(default_income, 200000)

    def test_give_default_raise(self):
        print(self.employee)
        self.employee.give_raise()
        income = self.employee.get_income()
        self.assertEqual(income, 205000)

    def test_give_custom_raise(self):
        print(self.employee)
        self.employee.give_raise(10000)
        income = self.employee.get_income()
        self.assertEqual(income, 210000)


unittest.main()
