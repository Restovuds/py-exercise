import math
import random


# + -

class Fraction:
    """
    Represents a real fraction
    """

    def __init__(self, num: int, den: int):
        if num > den:
            raise ValueError("The numerator must be greater than the denominator.")
        if den <= 0:
            raise ValueError("The denominator must be greater than zero.")

        self.num = num
        self.den = den

    def __str__(self) -> str:
        """
        :return: str of the object of type Fraction
        """
        return f'{self.num}\\{self.den}'

    def lcm(self, other):
        return math.lcm(self.den, other.den)

    def remainder(self):
        return self.num / self.den

    def __eq__(self, other):
        """
        :param other: object of type Fraction
        :return: bool or NotImplemented
        """
        if isinstance(other, Fraction):
            return self.remainder() == other.remainder()
        return NotImplemented

    def __ne__(self, other):
        """
        :param other: object of type Fraction
        :return: bool or NotImplemented
        """
        if isinstance(other, Fraction):
            return self.remainder() != other.remainder()
        return NotImplemented

    def __gt__(self, other):
        """
        :param other: object of type Fraction
        :return: bool or NotImplemented
        """
        if isinstance(other, Fraction):
            return self.remainder() > other.remainder()
        return NotImplemented

    def __ge__(self, other):
        """
        :param other: object of type Fraction
        :return: bool or NotImplemented
        """
        if isinstance(other, Fraction):
            return self.remainder() >= other.remainder()
        return NotImplemented

    def __lt__(self, other):
        """
        :param other: object of type Fraction
        :return: bool or NotImplemented
        """
        if isinstance(other, Fraction):
            return self.remainder() < other.remainder()
        return NotImplemented

    def __le__(self, other):
        """
        :param other: object of type Fraction
        :return: bool or NotImplemented
        """
        if isinstance(other, Fraction):
            return self.remainder() <= other.remainder()
        return NotImplemented

    def __add__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        den = self.lcm(other)
        num = (self.num * (den // self.den)) + (other.num * (den // other.den))
        return Fraction(num, den)

    def __radd__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        den = self.lcm(other)
        num = (self.num * (den // self.den)) + (other.num * (den // other.den))
        return Fraction(num, den)

    def __iadd__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        den = self.lcm(other)
        num = (self.num * (den // self.den)) + (other.num * (den // other.den))
        return Fraction(num, den)

    def __sub__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        den = self.lcm(other)
        num = (self.num * (den // self.den)) - (other.num * (den // other.den))
        return Fraction(num, den)

    def __rsub__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        den = self.lcm(other)
        num = (self.num * (den // self.den)) - (other.num * (den // other.den))
        return Fraction(num, den)

    def __isub__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        den = self.lcm(other)
        num = (self.num * (den // self.den)) - (other.num * (den // other.den))
        return Fraction(num, den)

    def __mul__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den)
        return NotImplemented

    def __rmul__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den)
        return NotImplemented

    def __imul__(self, other):
        """
        :param other: object of type Fraction
        :return: object of type Fraction
        """
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den)
        return NotImplemented


if __name__ == '__main__':
    try:
        # fractions = [Fraction(random.randint(1, 5), random.randint(5, 10)) for _ in range(10)]
        # print('\n'.join(map(str, fractions)))

        fr_1 = Fraction(1, 2)
        fr_2 = Fraction(2, 77)
        print(fr_1, fr_2, sep='\n')
        print(fr_1 - fr_2)

    except ValueError as error:
        print(error)
