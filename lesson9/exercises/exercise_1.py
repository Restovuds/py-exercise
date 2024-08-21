"""
Декоратор для логирования: Создать декоратор, который будет записывать в лог файл имя функции, аргументы,
время начала и окончания выполнения, а также результат работы.
"""
from datetime import datetime
import logging



def my_decorator(func):
    function_name = func.__name__

    def inner(*args, **kwargs):
        start = datetime.timestamp(datetime.now())
        result = func(*args, **kwargs)
        finish = datetime.timestamp(datetime.now())
        logging.info(f'{function_name}\targs: {args}, kwargs: {kwargs} \t result: {result} \t\t time: {start} - {finish} ')
        return result

    return inner


@my_decorator
def my_func1():
    print("Hello World")


@my_decorator
def my_func2(x):
    return x ** x


@my_decorator
def my_func3(x, y):
    return x + y


print(my_func1())
print(my_func2(2))
print(my_func3(2, 6))