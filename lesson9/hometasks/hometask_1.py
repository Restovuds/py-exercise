class Counter:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@Counter
def square(x):
    return x * x


# print(square(5))
# print(square(10))
# print(square(11))
#
# print(square.count)


#  ---------------------------------------------------------------------------------------------------------------------

# as example
def decorator(f):
    f.count = 0

    def wrapper(*args, **kwargs):
        f.count += 1
        return f(*args, **kwargs)

    return wrapper


@decorator
def func1():
    return "hello"

@decorator
def func2():
    return "world"


print(func1())
print(func1())
print(func2())
print(f'{func1.count} - {func2.count}')
