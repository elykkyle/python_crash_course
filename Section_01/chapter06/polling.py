favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'david', 'patricia', 'edward', 'john']

for person in people:
    if person not in favorite_languages:
        print(f"{person.title()}, you need to take the poll!")
    else:
        print(
            f"Hi {person.title()}, I see your favorite language is {favorite_languages[person].title()}.")
