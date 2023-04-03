party_size = input('How many people are in your dinner party? ')
party_size = int(party_size)

if party_size > 8:
    print('There will be a wait to seat you.')
else:
    print('Your table is ready.')
