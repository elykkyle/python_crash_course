person_0 = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 55,
    'city': 'minneapolis'
}
person_1 = {
    'first_name': 'jane',
    'last_name': 'doe',
    'age': 52,
    'city': 'saint paul'
}
person_2 = {
    'first_name': 'ralph',
    'last_name': 'tomato',
    'age': 27,
    'city': 'fridley'
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in the city of {person['city'].title()}.")
