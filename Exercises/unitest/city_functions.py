def cities_countries():
    """
    Get information from user about cities and countries
    """
    print('Digit \'q\' at any time to quit')
    while True:
        city = input('What\'s the name of the city: ')
        if city.lower() == 'q':
            break
        country = input('What\'s the name of the country: ')
        if country.lower() == 'q':
            break
        population = input(f'What\'s the population of {city.title()} : ')
        if population.lower() == 'q':
            break
        formatted_cities = format_cities_countries(city, country, population)
        print(f'\t\tNeatly formatted info: {formatted_cities}')


def format_cities_countries(city, country, population=''):
    """
    Receive name of city and name of country
    return: "City, Country", Ex: "Barranquilla, Colombia"
    """
    city_country_formmated = (f'{city.title()}, {country.title()} - Population: {population}')
    return city_country_formmated


if __name__ == '__main__':
    cities_countries()
