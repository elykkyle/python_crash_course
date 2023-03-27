favorite_numbers = {
    'john': [25, 28],
    'april': [8, 12],
    'david': [11, 98],
    'patrice': [7, 6],
    'ralph': [36, 2]
}

for k, v in favorite_numbers.items():
    print(f"{k.title()}'s favorite number are {v[0]} and {v[1]}")
