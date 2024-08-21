"""
Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами
"""


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __setattr__(self, key, value):
        if value <= 0:
            raise ValueError()
        if key == 'x':
            object.__setattr__(self, key, value)
        elif key == 'y':
            object.__setattr__(self, key, value)
        elif key == 'z':
            object.__setattr__(self, key, value)
        else:
            raise AttributeError()

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    @property
    def value(self):
        return self.x * self.y * self.z

    @staticmethod
    def sum_values(instance_2, instance_1):
        return instance_2.value + instance_1.value


if __name__ == '__main__':
    box_1 = Box(1, 2, 3)
    print(box_1)
    box_2 = Box(4, 5, 6)
    print(box_2)

    print(Box.sum_values(box_1, box_2))