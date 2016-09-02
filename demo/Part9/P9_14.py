from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        rollresult = randint(1, self.sides)
        msg = 'roll result = ' + str(rollresult)
        print(msg)

die20 = Die(20)
for times in range(10):
    die20.roll_die()


