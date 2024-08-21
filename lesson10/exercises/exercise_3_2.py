"""
Задача 2: Свойство с валидацией
Создайте класс Person, который будет представлять человека. У этого класса должен быть атрибут age (возраст).
Используйте property для создания свойства age, которое будет проверять, что возраст всегда является положительным
числом.

Требования:

Если попытаться установить возраст меньше или равный нулю, должно генерироваться исключение ValueError.
Свойство age должно быть доступным для чтения и записи.
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string.')
        self.__name = value

    @name.deleter
    def name(self):
        raise AttributeError('Cannot delete attribute.')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Age must be positive integer.')
        self.__age = value

    @age.deleter
    def age(self):
        raise AttributeError('Cannot delete attribute.')

    def __str__(self):
        return f'{self.name} is {self.age} years old'


person_1 = Person('John', 20)
print(person_1)
print(person_1.name)
print(person_1.age)
person_1.age = 'd'
