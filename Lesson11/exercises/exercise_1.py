"""
Suppose we want to create a program that calculates the area and perimeter of various shapes, such as rectangles,
squares, and circles. We can create an abstract class called Shape that defines the common interface for all shapes,
and then create derived classes for each specific shape.
"""

import abc
import math


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        # pass
        raise NotImplementedError

    @abc.abstractmethod
    def perimeter(self):
        # pass
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'w={self.width} h={self.height}'


class Square(Shape):
    def __init__(self, side: int | float):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f'side={self.side}'


class Circle(Shape):
    def __init__(self, radius: int | float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'r={self.radius}'


figures = [
    Rectangle(5, 6),
    Rectangle(5, 8),
    Square(5),
    Square(12),
    Circle(5),
    Circle(8),
]


def give_me_info(my_list):
    for i in my_list:
        print(i.area(), i.perimeter(), sep='\t')


give_me_info(figures)


