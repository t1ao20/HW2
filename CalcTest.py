import unittest
from Calc import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_sub(self):
        calc = Calculator()
        result = calc.sub(5, 3)
        self.assertEqual(result, 2)

    def test_mul(self):
        calc = Calculator()
        result = calc.mul(4, 3)
        self.assertEqual(result, 12)

    def test_div(self):
        calc = Calculator()
        result = calc.div(10, 2)
        self.assertEqual(result, 5)

    def test_div_by_zero(self):
        calc = Calculator()
        # 新增測試：除以零應回傳 None
        result = calc.div(10, 0)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
