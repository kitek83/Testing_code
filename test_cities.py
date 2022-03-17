import unittest
from tast_11_1_City import city_functions

class TestCity(unittest.TestCase):
    def test_city(self):
        formatted_city = city_functions('stetin','poland',5000)
        self.assertEqual(formatted_city,'Stetin,Poland - Population=5000')

if __name__ == '__main__':
    unittest.main()