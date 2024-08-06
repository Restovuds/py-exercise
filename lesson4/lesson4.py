# lecture code #

import random


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def value(self):
        return self.x * self.y * self.z

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'

    def __add__(self, other):
        return Box(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return Box(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __rmul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        return Box(self.x * other, self.y * other, self.z * other)

    def __mul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        return Box(self.x * other, self.y * other, self.z * other)

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __ne__(self, other):
        return self.value() != other.value()


# box_1 = Box(1, 1, 1)
# box_2 = 3 * box_1
# print(box_1, box_2, sep='\n')
# box_2 += box_1
# print(box_2)
# box_2 = Box(2, 2, 2)
# box_3 = Box(3, 3, 3)
# box_4 = box_1 + box_2 + box_3
# print(box_1, box_2, box_3, box_4, sep='\n')

# boxes = [Box(random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)) for i in range(10)]
# print('\n'.join(map(str, boxes)))
#
# print(min(boxes))

class Circle:

    def __init__(self, r):
        self.r = r

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.r == other.r
        if isinstance(other, (int, float)):
            return self.r == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.r != other.r
        if isinstance(other, (int, float)):
            return self.r != other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.r > other.r
        if isinstance(other, (int, float)):
            return self.r > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.r >= other.r
        if isinstance(other, (int, float)):
            return self.r >= other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.r < other.r
        if isinstance(other, (int, float)):
            return self.r < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.r <= other.r
        if isinstance(other, (int, float)):
            return self.r <= other
        return NotImplemented

    def __mul__(self, other: int | float):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Circle(self.r * other)

    def __rmul__(self, other: int | float):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Circle(self.r * other)

    def __imul__(self, other: int | float):
        if not isinstance(other, (int, float)):
            return NotImplemented
        self.r *= other
        return self

    def __str__(self):
        return f'Circle radius: {self.r}'


def u_mult(data):
    return str(data * 3)


circles = [Circle(random.randint(1, 50)) for _ in range(10)]
print('\n'.join(map(str, circles)))
print('\n')
print('\n'.join(map(str, sorted(circles))))
print('\n')
print('\n'.join(map(str, sorted(circles, reverse=True))))
print('\n')
print('\n'.join(map(u_mult, circles)))
