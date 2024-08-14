"""
2) Создайте декоратор, который зарегистрирует декорируемую функцию в
списке функций, для обработки последовательности.
"""

funk_list =[]


def registrator(f):
    funk_list.append(f)
    return f


@registrator
def add(a, b):
    return a + b


@registrator
def subtract(a, b):
    return a - b


@registrator
def multiply(a, b):
    return a * b


@registrator
def divide(a, b):
    return a / b


for i in range(len(funk_list)):
    print(funk_list[i](6, 2))
