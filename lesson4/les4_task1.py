class Rectangle:
    """
    Class describing a rectangle.
    """
    def __init__(self, w: int | float, h: int | float):
        self.w = w
        self.h = h

    def area(self) -> int | float:
        """
        :return: area of the rectangle
        """
        return self.w * self.h

    def __str__(self) -> str:
        """
        :return: a string representation of the rectangle.
        """
        return f'{self.w}x{self.h}'

    def __eq__(self, other) -> bool:
        """
        implementation of equality check
        :param other: object of type Rectangle or (int | float) num
        :return: bool | NotImplemented
        """
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        if isinstance(other, (int, float)):
            return self.area() == other
        return NotImplemented

    def __ne__(self, other) -> bool:
        """
        implementation of inequality check
        :param other: object of type Rectangle or (int | float) num
        :return: bool | NotImplemented
        """
        if isinstance(other, Rectangle):
            return self.area() != other.area()
        if isinstance(other, (int, float)):
            return self.area() != other
        return NotImplemented

    def __gt__(self, other) -> bool:
        """
        implementation of greedy inequality check
        :param other: object of type Rectangle or (int | float) num
        :return: bool | NotImplemented
        """
        if isinstance(other, Rectangle):
            return self.w > other.w
        if isinstance(other, (int, float)):
            return self.w > other
        return NotImplemented

    def __ge__(self, other) -> bool:
        """
        implementation of greedy inequality check
        :param other: object of type Rectangle or (int | float) num
        :return: bool | NotImplemented
        """
        if isinstance(other, Rectangle):
            return self.w >= other.w
        if isinstance(other, (int, float)):
            return self.w >= other
        return NotImplemented

    def __lt__(self, other) -> bool:
        """
        implementation of greedy inequality check
        :param other: object of type Rectangle or (int | float) num
        :return: bool | NotImplemented
        """
        if isinstance(other, Rectangle):
            return self.w < other.w
        if isinstance(other, (int, float)):
            return self.w < other
        return NotImplemented

    def __le__(self, other) -> bool:
        """
        implementation of greedy inequality check
        :param other: object of type Rectangle or (int | float) num
        :return: bool | NotImplemented
        """
        if isinstance(other, Rectangle):
            return self.w <= other.w
        if isinstance(other, (int, float)):
            return self.w <= other
        return NotImplemented

    def __add__(self, other):
        """
        implementation of the direct summation method
        :param other: object of type Rectangle or (int | float) num
        :return: object of type Rectangle or NotImplemented
        """
        if isinstance(other, Rectangle):
            self.w += other.w
            self.h += other.h
            return self
        if isinstance(other, (int, float)):
            self.w += other
            self.h += other
            return self
        return NotImplemented

    def __radd__(self, other):
        """
        implementation of the Inverse summation method
        :param other: object of type Rectangle or (int | float) num
        :return: object of type Rectangle or NotImplemented
        """
        if isinstance(other, Rectangle):
            self.w += other.w
            self.h += other.h
            return self
        if isinstance(other, (int, float)):
            self.w += other
            self.h += other
            return self
        return NotImplemented

    def __iadd__(self, other):
        """
        implementation of the method At the place of method summation
        :param other: object of type Rectangle or (int | float) num
        :return: object of type Rectangle or NotImplemented
        """
        if isinstance(other, Rectangle):
            return Rectangle(self.w + other.w, self.h + other.h)
        if isinstance(other, (int, float)):
            return Rectangle(self.w + other, self.h + other)
        return NotImplemented

    def __mul__(self, other: int | float):
        """
        implementation of the direct multiplication method
        :param other: object of int | float num
        :return: object of type Rectangle or NotImplemented
        """
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Rectangle(self.w * other, self.h * other)

    def __rmul__(self, other: int | float):
        """
        implementation of the multiplication method
        :param other: object of int | float num
        :return: object of type Rectangle or NotImplemented
        """
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Rectangle(self.w * other, self.h * other)

    def __imul__(self, other: int | float):
        """
        implementation of the multiplication method
        :param other: object of int | float num
        :return: object of type Rectangle or NotImplemented
        """
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Rectangle(self.w * other, self.h * other)


if __name__ == '__main__':
    rectangle_1 = Rectangle(5, 5)
    rectangle_2 = Rectangle(4, 6)

    print(rectangle_1, rectangle_2, sep='\n')
    rectangle_1 += rectangle_2
    print(rectangle_1)


