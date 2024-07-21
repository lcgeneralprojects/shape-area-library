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
                if shape.criterion(sides):
                    area = shape(sides).area()
                    return area
            except AttributeError:
                print(f'{shape} is not a shape')
                return
            except NotImplementedError:
                print(f'{shape} does not have an implemented criterion method')
                return
        for shape in cls.shapes:
            if shape.criterion(sides):
                area = shape(sides).area()
                return area
        raise NoAppropriateShapeException('No matching supported shape found')

    @classmethod
    def add_shapes(cls, shapes_to_add):
        for shape_candidate in shapes_to_add:
            try:
                shape_candidate.criterion()
            except AttributeError:
                print(f'{shape_candidate} is not a shape')
                continue
            except NotImplementedError:
                print(f'{shape_candidate} does not have an implemented criterion method')
                continue
            cls.shapes.add(shape_candidate)

    @classmethod
    def remove_shapes(cls, shapes_to_delete=None):
        if shapes_to_delete is None:
            cls.shapes.clear()
        else:
            for shape in shapes_to_delete:
                cls.shapes.remove(shape)


class Shape:
    target_calculator = AreaCalculator

    def __new__(cls, sides):
        if cls.criterion(sides):
            return super().__new__(cls)
        else:
            raise NotShapeException(
                'Cannot instantiate shape: input values do not satisfy the criterion for this shape')

    def __init__(self, sides):
        self.sides = sides

    def __init_subclass__(cls, **kwargs):
        if cls.target_calculator is not None:
            cls.target_calculator.add_shapes([cls])

    @staticmethod
    def criterion(*args):
        raise NotImplementedError('This class does not have a criterion method')

    def area(self):
        raise NotImplementedError('This class does not have an area-calculation method')


class Triangle(Shape):
    def __init__(self, sides):
        super().__init__(sides=sides)
        self.sides.sort()

    @staticmethod
    def criterion(sides=None):
        if sides is None:
            return False
        tmp = sorted(sides)
        return (len(sides) == 3 and
                all(side > 0 for side in sides) and
                tmp[0]+tmp[1] > tmp[2])

    def area(self):
        half_perimeter = sum(self.sides) / 2
        area = math.sqrt(reduce(lambda x, y: x * (half_perimeter - y), [half_perimeter, *self.sides]))  # Heron's formula
        return area

    def check_if_rectangular(self):
        return self.sides[0] ** 2 + self.sides[1] ** 2 == self.sides[2] ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius[0]

    @staticmethod
    def criterion(radius=None):
        if radius is None:
            return False
        return len(radius) == 1 and radius[0] > 0

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area
