"""
2) Создайте декоратор класса с параметром. Параметром должна быть
строка, которая должна дописываться (слева) к результату работы метода
__str__.
"""


def prefix(string):
    def decorator(func):
        def inner(*args, **kwargs):
            return f'{string} {func(*args, **kwargs)}'
        return inner
    return decorator


class Person:
    def __init__(self, name):
        self.name = name

    @prefix('Mr')
    def __str__(self):
        return self.name


per_1 = Person('John')
print(per_1)