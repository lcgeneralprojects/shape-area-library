import unittest
from shape_area_calculator import Shape, AreaCalculator

class MyTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(AreaCalculator([3, 4, 5]), 2)  # add assertion here

if __name__ == '__main__':
    unittest.main()
