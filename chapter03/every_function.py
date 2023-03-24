pets = ['dog', 'cat', 'fish', 'hamster', 'guinea pig', 'reptiles', 'frogs']

print(f'there are {len(pets)} pets in the list')

pets.append('goat')

print(f'now there are {len(pets)} listed')

removed = pets.pop()

print(f'people don\'t really want a {removed} as a pet')

print(sorted(pets))

pets.sort(reverse=True)

print()
