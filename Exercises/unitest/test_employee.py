import unittest

from Exercises.unitest.employees import Employee


class TestEmploye(unittest.TestCase):

    def setUp(self):
        self.user0 = Employee('alfonso', 'areiza', 3000)

    def test_give_default_raise(self):
        self.user0.give_raise()
        self.assertEqual(self.user0.salary, 8000)

    def test_give_custom_raise(self):
        self.user0.give_raise(1000)
        self.assertTrue(self.user0.salary == 4000)


if __name__ == '__main__':
    unittest.main()
