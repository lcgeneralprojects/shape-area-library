from errors import NoAppropriateShapeException


class Shape:
    def __new__(cls, *args, **kwargs):
        if cls is Shape:
            for shape_class in AreaCalculator.shapes:
                if shape_class.criterion(*args):
                    return shape_class(*args)
            raise NoAppropriateShapeException('No appropriate shape found')

    def criterion(self, *args):
        pass

    def area(self):
        pass


class Triangle(Shape):
    pass


class Circle(Shape):
    pass


class AreaCalculator:
    shapes = [Circle, Triangle]

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('This class is not meant to be instantiated')

    def calculate_area(*args):
        area = Shape(*args).area()
        return area
