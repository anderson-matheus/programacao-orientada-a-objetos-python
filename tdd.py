import unittest
from calculadora import Calculadora


class TddExample(unittest.TestCase):
    def test_soma(self):
        calc = Calculadora()
        result = calc.somar(10, 20)
        self.assertEqual(30, result)

    def test_sub(self):
        calc = Calculadora()
        result = calc.subtrair(40, 20)
        self.assertEqual(20, result)


if __name__ == '__main__':
    unittest.main()
