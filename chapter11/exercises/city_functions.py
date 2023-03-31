def get_formatted_city_country(city, country, population=None):
    """Formats city name and country."""
    if population:
        city_country = f"{city}, {country} - {population}"
    else:
        city_country = f"{city}, {country}"
    return f"{city_country.title()}"
