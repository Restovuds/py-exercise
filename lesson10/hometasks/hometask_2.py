"""
2) Реализуйте функционал, который будет запрещать установку полей класса
любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
попытаться присвоить, например, строку, то должно быть возбужденно
исключение.
"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        print(self.width)
        return f'{self.width}x{self.height}'

    def __setattr__(self, key, value):
        if key != 'width' and key != 'height':
            raise AttributeError(f'Cannot add attribute "{key}" to Rectangle')

        if not isinstance(value, int):
            raise AttributeError(f'Attribute "{key}" must be an <class \'int\'>, not {type(value)}')

        self.__dict__[key] = value


test = Rectangle(5, 6)
print(test)
test.width = 10
print(test)
test.height = "11"
print(test)
# test.width = 1.1
test.dsdfds= "dfsdfds"

