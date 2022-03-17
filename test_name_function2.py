import unittest
from name_function import get_formatted_name

class TestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('kris','kozak')
        self.assertEqual(formatted_name,'Kris Kozak')

if __name__ == '__main__':
    unittest.main()