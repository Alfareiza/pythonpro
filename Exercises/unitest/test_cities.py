import unittest
from Exercises.unitest import city_functions


class TestCities(unittest.TestCase):
    """Tests para city_functions.py"""

    def test_city_country(self):
        input_value = city_functions.format_cities_countries('barranquilla', 'colombia', '1000000')
        self.assertEqual('Barranquilla, Colombia - Population: 1000000', input_value)


if __name__ == '__main__':
    unittest.main()
