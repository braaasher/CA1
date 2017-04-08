import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calc_add(self):
        res = self.calc.add(5, 5)
        self.assertEqual(res, 10)
        
    def test_calc_subtract(self):
        res = self.calc.subtract(10, 5)
        self.assertEqual(res, 5)
        
    def test_calc_multiply(self):
        res = self.calc.multiply(5, 5)
        self.assertEqual(res, 25)
        
    def test_calc_divide(self):
        res = self.calc.divide(10, 5)
        self.assertEqual(res, 2)
        
    def test_calc_square(self):
        res = self.calc.square(5)
        self.assertEqual(res, 25)
        
    def test_calc_cube(self):
        res = self.calc.cube(5)
        self.assertEqual(res, 125)
        
    def test_calc_expon(self):
        res = self.calc.expon(6, 4)
        self.assertEqual(res, 1296)
        
    def test_calc_sqrt(self):
        res = self.calc.sqrt(49)
        self.assertEqual(res, 7.0)

    def test_calc_pi(self):
        res = self.calc.pi(1)
        self.assertEqual(res, 3.14159265359)
        
    def test_calc_factorial(self):
        res = self.calc.factorial(5)
        self.assertEqual(res, 120)
          
if __name__ == '__main__':
    unittest.main()