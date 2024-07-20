import math
import unittest
from shape_area_calculator import AreaCalculator


class MyTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(6, AreaCalculator.calculate_area([3, 4, 5]))

    def test_circle_area(self):
        self.assertEqual(math.pi, AreaCalculator.calculate_area([1]))


if __name__ == '__main__':
    unittest.main()
