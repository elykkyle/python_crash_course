vacations = {}

while True:
    name = input("Please enter your name: ")
    vacation = input(
        "If you could visit one place in the world, where would you go? ")
    vacations[name] = vacation
    repeat = input("Would someone else like to complete the poll? (yes/no)")
    if repeat == 'no':
        break

for k, v in vacations.items():
    print(f"{k.title()} want to go to {v.title()}")
