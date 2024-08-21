"""
Задача 1: Управление атрибутом с вычисляемым свойством
Создайте класс Rectangle, который будет представлять прямоугольник. Класс должен иметь атрибуты width (ширина) и height
(высота). Используйте property для создания вычисляемого свойства area, которое будет возвращать площадь прямоугольника,
и perimeter, которое будет возвращать периметр.

Требования:

Свойства width и height должны быть доступными для чтения и записи.
Свойства area и perimeter должны быть доступны только для чтения.
"""


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height

    @property
    def perimeter(self):
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError()
        self.__width = value

    @width.deleter
    def width(self):
        raise ValueError('width cannot be deleted')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError()
        self.__height = value

    @height.deleter
    def height(self):
        raise ValueError('height cannot be deleted')

    def __str__(self):
        return f'width: {self.__width}, height: {self.__height}'


if __name__ == '__main__':
    rectangle = Rectangle(10, 20)
    print(rectangle)
    print(rectangle.area)
    print(rectangle.perimeter)
    rectangle.width = 1
    rectangle.height = 2
    print(rectangle)
    print(rectangle.area)
    print(rectangle.perimeter)


