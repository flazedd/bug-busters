import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)
        self.assertEqual(self.calculator.subtract(1, 3), -2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-1, 3), -3)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(5, 1), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
