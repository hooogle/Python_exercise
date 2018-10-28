from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


for i in range(1,10):
    six_sides = Die(6)
    six_sides.roll_die()

    ten_sides = Die(10)
    ten_sides.roll_die()

    twelten_sides = Die(20)
    twelten_sides.roll_die()