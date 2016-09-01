from Part9.P9_3 import User


class Admin(User):
    def __init__(self):
        super().__init__('Q','Zidane')
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user',
                           ]
    def show_privileges(self):
        for pr in self.privileges:
            print(pr)


class Privileges:
    def __init__(self):
        self.privileges