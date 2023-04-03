from random import randint


class Die:
    """A class to represent dice"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(f"die: {number}")


print("SIX SIDES")
six_sided_die = Die()
for num in range(0, 10):
    six_sided_die.roll_die()

print("TEN SIDES")
ten_sided_die = Die(10)
for num in range(0, 10):
    ten_sided_die.roll_die()

print("TWENTY SIDES")
twenty_sided_die = Die(20)
for num in range(0, 10):
    twenty_sided_die.roll_die()
