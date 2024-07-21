import math
import unittest
from shape_area_calculator import Shape, Triangle, Circle, AreaCalculator


class MyTestCase(unittest.TestCase):
    def test_triangle_area_non_instantiated(self):
        cases = [
            {'Expected': 6, 'Input': [3, 4, 5]}
        ]
        for case in cases:
            self.assertEqual(case['Expected'], AreaCalculator.calculate_area(case['Input']))

    def test_triangle_area_instantiated(self):
        cases = [
            {'Expected': 6, 'Input': [3, 4, 5]}
        ]
        for case in cases:
            test_triangle = Triangle(case['Input'])
            self.assertEqual(case['Expected'], test_triangle.area())

    def test_circle_area_non_instantiated(self):
        cases = [
            {'Expected': math.pi, 'Input': [1]}
        ]
        for case in cases:
            self.assertEqual(case['Expected'], AreaCalculator.calculate_area(case['Input']))

    def test_circle_area_instantiated(self):
        cases = [
            {'Expected': math.pi, 'Input': [1]}
        ]
        for case in cases:
            test_circle = Circle(case['Input'])
            self.assertEqual(case['Expected'], test_circle.area())

    def test_custom_shape_area(self):
        class CustomShape(Shape):
            target_calculator = None

            @staticmethod
            def criterion(sides=None):
                return True

            def area(self):
                return -1

        self.assertEqual(-1, AreaCalculator.calculate_area([], CustomShape))

    def test_failed_criteria(self):
        cases = [
            {'Expected': False, 'Shape': Triangle, 'Input': [-1, -2, -3]},
            {'Expected': False, 'Shape': Triangle, 'Input': [1, 2, 8]},
            {'Expected': False, 'Shape': Triangle, 'Input': [1]},
            {'Expected': False, 'Shape': Circle, 'Input': [-1]},
        ]
        for case in cases:
            self.assertEqual(case['Expected'], case['Shape'].criterion(case['Input']))


if __name__ == '__main__':
    unittest.main()
