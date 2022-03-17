import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('kris','kozak','wladyslaw')
        self.assertEqual(formatted_name,'Kris Wladyslaw Kozak')

if __name__ == '__main__': #if this file is run as the main program, the value of __name__ is set to __main__
    unittest.main()