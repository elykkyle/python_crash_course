cities = {
    'minneapolis': {
        'country': 'united states',
        'population': 425_000,
        'fact': 'Nicknamed the \'City of Laked\''
    },
    'strasbourg': {
        'country': 'france',
        'population': 290_500,
        'fact': 'One of the few cities in the world that is not a state capital that hosts international organizations of the first order.'
    },
    'yaounde': {
        'country': 'cameroon',
        'population': '2_765_000',
        'fact': 'Local residents often engage in urban agriculture. The city is estimated to have 50,000 pigs and over a million chickens.'
    }
}

for city, info in cities.items():
    print(f"{city.title()}:")
    for k, v in info.items():
        if k == 'country':
            print(f"{k.title()}: {v.title()}")
        else:
            print(f"{k.title()}: {v}")
