import math
from functools import reduce
from errors import NoAppropriateShapeException, NotShapeException


class AreaCalculator:
    shapes = set()

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('This class is not meant to be instantiated')

    @classmethod
    def calculate_area(cls, sides, shape=None):
        if shape is not None:
            try:
                shape.criterion(sides)
            except AttributeError:
                print(f'{shape} is not a shape')
            except NotImplementedError:
                print(f'{shape} does not have an implemented criterion method')
        for shape in cls.shapes:
            if shape.criterion(sides):
                area = shape(sides).area()
                return area
        raise NoAppropriateShapeException('No matching supported shape found')

    @classmethod
    def add_shapes(cls, shapes):
        for shape_candidate in shapes:
            try:
                shape_candidate.criterion([0])
            except AttributeError:
                print(f'{shape_candidate} is not a shape')
                continue
            except NotImplementedError:
                print(f'{shape_candidate} does not have an implemented criterion method')
                continue
            cls.shapes.add(shape_candidate)


class Shape:
    def __new__(cls, sides):
        if cls.criterion(sides):
            return super().__new__(cls)
        else:
            raise NotShapeException(
                'Cannot instantiate shape: input values do not satisfy the criterion for this shape')

    def __init__(self, sides):
        self.sides = sides

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        AreaCalculator.add_shapes([cls])

    @staticmethod
    def criterion(*args):
        raise NotImplementedError('This class does not have a criterion method')

    def area(self):
        raise NotImplementedError('This class does not have an area-calculation method')


class Triangle(Shape):
    @staticmethod
    def criterion(sides=None):
        if sides is None:
            return False
        return (len(sides) == 3 and
                all(side > 0 for side in sides) and
                sides[0] < sides[1]+sides[2] and
                sides[1] < sides[0]+sides[2] and
                sides[2] < sides[0]+sides[1])

    def area(self):
        half_perimeter = sum(self.sides) / 2
        area = math.sqrt(reduce(lambda x, y: x * (half_perimeter - y), [half_perimeter, *self.sides]))  # Heron's formula
        return area

    def check_if_rectangular(self):
        tmp = sorted(self.sides)
        return tmp[0] ** 2 + tmp[1] ** 2 == tmp[2] ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius[0]

    @staticmethod
    def criterion(radius):
        if radius is None:
            return False
        return len(radius) == 1 and radius[0] > 0

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area
