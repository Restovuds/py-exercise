

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


print(square(5))
print(square(10))
print(square(11))

print(square.count)
