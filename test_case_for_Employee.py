import unittest
from task_11_3_emploee import Employee

class TestTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Kris','Kozak',2000)

    def test_give_default_rise(self):
        self.employee.give_rise()
        self.assertEqual(7000,self.employee.annual_salary)

    def test_give_custom_rise(self):
        self.employee.give_rise(3000)
        self.assertEqual(5000,self.employee.annual_salary)

if __name__ == '__main__':
    unittest.main()
