from city_functions import get_formatted_city_country


def test_city_country():
    """does santiago chile work?"""
    formatted_city_country = get_formatted_city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'


def test_city_country_population():
    """does santiago chile work?"""
    formatted_city_country = get_formatted_city_country(
        'santiago', 'chile', 5000000)
    assert formatted_city_country == 'Santiago, Chile - 5000000'
