favorite_places = {
    'kyle': ['bergen', 'venice', 'freudenstadt'],
    'darryl': ['puerto vallarta', 'emily', 'san diego'],
    'frank': ['palm springs', 'new york', 'paris']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places:")
    for place in places:
        print(f"{place.title()}")
    print("\n")
