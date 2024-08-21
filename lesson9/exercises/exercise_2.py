"""
Декоратор для кэширования: Реализовать декоратор, который будет кэшировать результаты вызова
функции для заданного набора аргументов.
"""

cache = {}


def cache_decorator(func):
    def inner(*args, **kwargs):
        if func.__name__ in cache:
            if (args, kwargs) in cache[func.__name__]['args-kwargs']:
                ind = cache[func.__name__]['args-kwargs'].index((args, kwargs))
                return cache[func.__name__]['result'][ind]
            else:
                cache[func.__name__]['args-kwargs'].append((args, kwargs))
                cache[func.__name__]['result'].append(func(*args, **kwargs))
        if func.__name__ not in cache:
            cache[func.__name__] = {
                'args-kwargs': [],
                'result': []
            }
            cache[func.__name__]['args-kwargs'].append((args, kwargs))
            cache[func.__name__]['result'].append(func(*args, **kwargs))

        return func(*args, **kwargs)

    return inner


@cache_decorator
def my_func2(x):
    return x ** x


@cache_decorator
def my_func3(x, y):
    return x + y


print(my_func2(2))
print(my_func3(2, 6))
print(my_func2(10))
print(my_func3(2, 10))
print(cache)


