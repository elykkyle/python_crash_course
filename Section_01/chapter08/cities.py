def describe_city(city_name, country="USA"):
    """prints country of city"""
    print(f"{city_name.title()} is in {country.title()}.")


describe_city('berlin', 'germany')
describe_city('new york')
describe_city('sydney', 'australia')
