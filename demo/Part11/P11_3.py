class Employee:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def give_raise(self, amount=''):
        if amount:
            self.income += amount
        else:
            self.income += 5000

    def get_income(self):
        print(self.name + "'s income = " + str(self.income))
        return self.income

emp1 = Employee('zidane', 200000)
emp1.get_income()
emp1.give_raise(10000)
emp1.get_income()
emp1.give_raise()
emp1.get_income()
