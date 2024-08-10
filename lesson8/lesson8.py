import random


# x = input()
# if x.lower() == 'start':
#
#     def my_func():
#         return 'Hello World'
#
#     print(my_func())
#
# print("Finish")


# def my_function():
#     return "Hello World"
#
#
# y = my_function
# print(y())


# func = None
#
# price = float(input("Enter good price: "))
# type_good = input("Enter good type: ")
#
# if type_good == "eat":
#     def get_price(price):
#         return price * 1.45
#
#     func = get_price
# else:
#     def get_price(price):
#         return price * 5.85
#
#     func = get_price
#
# print(func(price))


# def my_filter(seq: list, predicate: callable):
#     res = []
#     for i in seq:
#         res.append(predicate(i, 2))
#
#     return res
#
#
# my_list = list(random.randint(-10, 10) for _ in range(20))
# print(my_list)
# print(my_filter(my_list, lambda item, power: item ** power))
#
# g = lambda x: x**2
# print(type(g))


# def outer():
#     def inner():
#         return 'Hello'
#
#     return inner
#
#
# x = outer()
# print(x)  # <function outer.<locals>.inner ...
# print(x())  # Hello


# class Average:
#     def __init__(self):
#         self.numbers = []
#
#     def __call__(self, number):
#         self.numbers.append(number)
#         return sum(self.numbers) / len(self.numbers)
#
#     def set_zero(self):
#         self.numbers = []
#
#
# f = Average()
# print(f(5))  # 5
# print(f(3))  # 4
# print(f(1))  # 3


# def get_sum(a: int, b: int):  # get_sum.__annotations__ > {'a': <class 'int'>, 'b': <class 'int'>}
#     return a + b
#
#
# print(dir(get_sum))
# # _________^_______
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
# # '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__',
# # '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__',
# # '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
# # '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']
# print(get_sum.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>}


#  closures example
# def calc_pow(exponent):
#     def calculate(number):
#         return pow(number, exponent)
#
#     return calculate
#
#
# x = calc_pow(2)
# print(x)  # <function calc_pow.<locals>.calculate at
# print(x.__closure__)  # (<cell at 0x0...: int object at 0x0...>,)
#
# #  x.__code__ >> co_freevars = {tuple: 1} (exponent) >> 0 = {str} 'exponent', __len__ = {int} 1
#
# for i in range(10):
#     print(x(i), end=' ')  # 0 1 4 9 16 25 36 49 64 81


# def fibonacci():
#     first_number = 0
#     second_number = 1
#
#     def get_next():
#         nonlocal first_number, second_number  # Must be "nonlocal" due to scope
#         next_number = first_number + second_number
#         first_number = second_number
#         second_number = next_number
#         return next_number
#     return get_next
#
#
# x = fibonacci()
#
# for _ in range(10):
#     print(x())


# def factorial():
#     result = [1, ]
#
#     def get_next_factorial(n):
#         if n < len(result):
#             return result[n]
#
#         index = len(result) - 1
#         res = result[-1]
#         for i in range(index + 1, n + 1):
#             res *= i
#             result.append(res)
#
#         return res
#
#     return get_next_factorial
#
#
# x = factorial()
# print(x(3))
# print(x(5))
# print(x(4))
# print(x(0))





