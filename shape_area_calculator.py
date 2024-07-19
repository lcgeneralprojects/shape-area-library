import math
from functools import reduce
from errors import NoAppropriateShapeException


class Shape:
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('This class is not meant to be instantiated')

    @classmethod
    def criterion(cls, *args):
        raise NotImplementedError('This class has no criterion method')

    @classmethod
    def area(cls, *args):
        raise NotImplementedError('This class has no area calculation method')


class Triangle(Shape):
    @classmethod
    def criterion(cls, *args):
        return len(args) == 3

    @classmethod
    def area(cls, *args):
        perimeter = sum(args)/2
        area = math.sqrt(reduce(lambda x, y: x*(perimeter-y), [0, *args]))
        return area


class Circle(Shape):
    @classmethod
    def criterion(cls, *args):
        return len(args) == 1

    @classmethod
    def area(cls, *args):
        radius = args[0]
        area = math.pi * (radius ** 2)
        return area


class AreaCalculator:
    shapes = [Circle, Triangle]

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('This class is not meant to be instantiated')

    @classmethod
    def calculate_area(cls, *args):
        for shape in cls.shapes:
            if shape.criterion(*args):
                area = shape.area(*args)
                return area
        raise NoAppropriateShapeException('No matching supported shape found')

    @classmethod
    def add_shapes(cls, *args):
        cls.shapes+list(args)
