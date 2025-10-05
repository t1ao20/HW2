import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_sub(self):
        calc = Calculator()
        result = calc.sub(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2

    def test_mul(self):
        calc = Calculator()
        result = calc.mul(4, 3)
        self.assertEqual(result, 12)  # Expect 4 * 3 = 12

    def test_div(self):
        calc = Calculator()
        result = calc.div(10, 2)     # fix test case here
        self.assertEqual(result, 5)  # Expect 10 / 2 = 5
    
    def test_div_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.div(10, 0)  # Division by zero should raise ValueError

if __name__ == "__main__":
    unittest.main()

    