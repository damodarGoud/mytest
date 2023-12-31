import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-2, -2), -4)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-2, -2), 0)
        self.assertEqual(calc.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-2, -2), 4)
        self.assertEqual(calc.multiply(-1, 1), -1)
