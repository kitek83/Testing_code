import unittest
from city import city_funtions

class TestCities(unittest.TestCase):
    def test_cities(self):
        formatted_name = city_funtions('stetin','poland',5000)
        self.assertEqual(formatted_name,'Stetin, Poland - Population=5000')

if __name__ == '__main__':
    unittest.main()