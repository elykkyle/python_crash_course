pet_0 = {
    'name': 'hank',
    'owner': 'john',
    'type': 'dog',
}
pet_1 = {
    'name': 'charlie',
    'owner': 'kyle',
    'type': 'cat',
}
pet_2 = {
    'name': 'kermit',
    'owner': 'alysia',
    'type': 'squirrel',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(
        f"{pet['name'].title()} is a {pet['type']} and belongs to {pet['owner'].title()}.")
