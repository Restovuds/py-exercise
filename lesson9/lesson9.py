#  Lecture code

# from unittest import result
# my_list = []
#
#
# def decorator_func(f):
#     my_list.append(f)
#     return f
#
#
# @decorator_func
# def add(a, b):
#     return a + b
#
#
# @decorator_func
# def multiply(a, b):
#     return a * b
#
#
# print(my_list)
#
#
# for i in my_list:
#     print(i(2, 3))

#  # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

def tags(tag):
    def decorator(func):
        def inner(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return inner
    return decorator


@tags('p')
@tags('a')
def get_text(name):
    return f'Hello {name}'


@tags('i')
def get_text_1(name, surname):
    return f'Hello {surname} {name[0]}.'


@tags('b')
def get_text_2(name, surname, second_name=None):
    return f'Hello {surname} {name[0]}. {second_name}'


print(get_text('Oleh'))
print(get_text_1('Dima', 'Rayko'))
print(get_text_2('Dima', 'Rayko', second_name='Serhiyovich'))

#  # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

# def tags(tag):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#         return inner
#     return decorator
#
#
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     @tags('a')
#     def __str__(self):
#         return f'Hello {self.name}'
#
#
# obj = A('Bob')
# print(obj)

#  # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

# import time
#
#
# class TimeDecorator:
#     def __init__(self, func):
#         self.func = func
#         self.start = 0
#         self.stop = 0
#
#     def __call__(self, *args, **kwargs):
#         self.start = time.time()
#         res = self.func(*args, **kwargs)
#         self.stop = time.time()
#         return res
#
#
# @TimeDecorator
# def greetings(name):
#     return f'Hello, {name}'
#
#
# print()
#
# print(greetings('John'))
# print(greetings.start)
# print(greetings.stop)


