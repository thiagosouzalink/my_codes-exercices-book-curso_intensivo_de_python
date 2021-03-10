def city_country(city, country, population=None):
    if population:
        city_country_formatted = f"{city.title()}, {country.title()} - população {population}"
    else:
        city_country_formatted = f"{city.title()}, {country.title()}"
    return city_country_formatted