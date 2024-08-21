"""
Задача 3: Удаление и динамическое создание атрибутов
Создайте класс DynamicAttributes, который использует методы __getattr__ и __delattr__ для динамического управления
атрибутами. Если атрибут не существует, он должен быть автоматически создан с значением None. Также реализуйте
возможность удаления атрибута с логированием.

Требования:
Если запрашивается несуществующий атрибут, он должен автоматически создаваться с значением None.
Метод __delattr__ должен удалять атрибут и выводить сообщение о том, что атрибут был удален.
"""


class DynamicAttributes:
    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = None

        return self.__dict__[name]

    def __delattr__(self, name):
        if name in self.__dict__:
            print(f'{name} was deleted')
            del self.__dict__[name]

    def __str__(self):
        return self.__dict__


test1 = DynamicAttributes()
print(test1.a1)
test1.a1 = "hello"
print(test1.a1)
print(test1.a2)
del test1.a2
