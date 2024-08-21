"""
Реализуйте класс Person с дескриптором для проверки валидности имени и возраста. Имя должно быть строкой и не
может быть пустым, а возраст должен быть положительным числом.
"""


class PersonName:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        instance.__dict__['_name'] = value


class PersonAge:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Age must be int")
        instance.__dict__['_age'] = value


class Person:
    name = PersonName()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'


per_1 = Person('John', 25)
per_2 = Person('Vika', 35)
print(per_1)
print(per_2)
per_1.age = 23
per_1.name = 'John1'
print(per_1)
print(per_2)
