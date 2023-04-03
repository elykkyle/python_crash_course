def city_country(city_name, country):
    """returns formatted string of city name and country"""
    return f"{city_name.title()}, {country.title()}"


print(city_country('paris', 'france'))
print(city_country('berlin', 'germany'))
print(city_country('london', 'england'))
