"""
Декоратор для проверки типов:
Написать декоратор, который будет проверять типы передаваемых аргументов функции и
выбрасывать исключение при несовпадении.
"""


def my_decorator(func):
    def inner(*args, **kwargs):
        annotations = func.__annotations__
        del annotations['return']
        for key, value in kwargs.items():
            if annotations[key] is not type(value):
                raise TypeError(f'"{key}" must be {annotations[key]} not {type(value)}')
            if annotations[key] == type(value):
                del annotations[key]

        annotations_list = list(annotations.keys())

        for index in range(len(args)):
            if type(args[index]) is not annotations[annotations_list[index]]:
                raise TypeError(f'One of the positional argument must be {annotations[annotations_list[index]]}')

        return func(*args, **kwargs)

    return inner


@my_decorator
def my_func1(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError
    return x / y


print(my_func1(1, y=10))
