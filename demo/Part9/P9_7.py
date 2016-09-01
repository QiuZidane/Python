from Part9.P9_3 import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user',
                           ]

class Admin(User):
    def __init__(self):
        super().__init__('Q', 'Zidane')
        self.privileges = Privileges().privileges

    def show_privileges(self):
        for pr in self.privileges:
            print(pr)

admin1 = Admin()
admin1.show_privileges()