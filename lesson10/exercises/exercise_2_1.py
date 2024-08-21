"""
Задача 1: Логирование доступа к атрибутам
Создайте класс LoggedAttributes, который будет логировать все обращения к атрибутам объекта. Вам нужно переопределить
метод __getattribute__, чтобы каждый раз, когда атрибут запрашивается, в консоль выводилось сообщение с именем атрибута
и его значением.

Требования:

Логирование должно происходить для любого обращения к атрибуту объекта.
В случае, если атрибут не найден, должно выводиться сообщение об ошибке и генерироваться исключение AttributeError.
"""

class LoggedAttributes:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __getattribute__(self, item):
        try:
            value = super().__getattribute__(item)
            print(f'Accessing attribute "{item}": {value}')
            return value
        except AttributeError:
            print(f'Attribute "{item}" does not exist')
            raise


new1 = LoggedAttributes(name='John', surname='Smith', age=22)
print(new1.name)
print(new1.surname1)