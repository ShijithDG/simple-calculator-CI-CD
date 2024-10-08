import unittest
from calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(0, 10), 10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), 0)  # No negative results allowed

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calc.add(-1, 5)
        with self.assertRaises(ValueError):
            self.calc.subtract(5, -1)
        with self.assertRaises(ValueError):
            self.calc.multiply(3, "a")

if __name__ == "__main__":
    unittest.main()
