import unittest

from employee import Employee


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee('José', 'Silva', 60000)
        self.initial_value = self.employee1.annual_salary

    def test_give_default_raise(self):
        new_value = self.initial_value + 5000 # Valor desejado
        self.employee1.give_raise()
        self.assertEqual(new_value, self.employee1.annual_salary)

    def test_give_custom_raise(self):
        new_value = self.initial_value + 8000 # Valor desejado
        self.employee1.give_raise(8000)
        self.assertEqual(new_value, self.employee1.annual_salary)


unittest.main()