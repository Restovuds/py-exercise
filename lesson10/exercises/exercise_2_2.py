"""
Задача 2: Управление атрибутами с валидацией
Реализуйте класс ValidatedAttributes, который использует метод __setattr__ для валидации устанавливаемых атрибутов.
Например, если атрибут называется age, его значение должно быть положительным числом.

Требования:

Метод __setattr__ должен проверять, что значение атрибута age — положительное целое число.
Если значение не соответствует требованиям, должно генерироваться исключение ValueError.
"""


class ValidatedAttributes:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        if key == 'age':
            if not isinstance(value, int) or value <=0:
                raise ValueError('Age must be positive integer')

        super().__setattr__(key, value)

    def __str__(self):
        return f'{self.name} {self.age}'


#test = ValidatedAttributes('name', 'age')
test = ValidatedAttributes('Oleh', -1)
print(test)
