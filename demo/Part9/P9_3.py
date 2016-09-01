class User:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.full_name = self.first_name + self.last_name

    def describe_user(self):
        msg = 'your name = ' + self.full_name
        print(msg)

    def greet_user(self):
        msg = 'hello : ' + self.full_name
        print(msg)



# user1 = User('qiu', 'zidane')
# user1.describe_user()
# user1.greet_user()
