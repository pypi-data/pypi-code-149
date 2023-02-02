import unittest
import action

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(action.add(2, 3), 5)
        self.assertEqual(action.add(-2, -3), -5)
        self.assertEqual(action.add(0, 0), 0)
        
    def test_subtract(self):
        self.assertEqual(action.subtract(5, 3), 2)
        self.assertEqual(action.subtract(-5, -3), -2)
        self.assertEqual(action.subtract(0, 0), 0)
        
    def test_multiply(self):
        self.assertEqual(action.multiply(2, 3), 6)
        self.assertEqual(action.multiply(-2, -3), 6)
        self.assertEqual(action.multiply(0, 0), 0)
        
    def test_divide(self):
        self.assertEqual(action.divide(6, 3), 2)
        self.assertEqual(action.divide(-6, -3), 2)
        with self.assertRaises(ZeroDivisionError):
            action.divide(6, 0)
        
    def test_power(self):
        self.assertEqual(action.power(2, 3), 8)
        self.assertEqual(action.power(-2, 3), -8)
        self.assertEqual(action.power(0, 0), 1)
        
    def test_n_root(self):
          with self.assertRaises(ValueError):
            action.n_root(-4, 2)
          self.assertEqual(action.n_root(16, 2), 4)
          self.assertEqual(action.n_root(27, 3), 3)

if __name__ == '__main__':
    unittest.main()
