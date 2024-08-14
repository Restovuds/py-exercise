from timeit import timeit


class Chronometric:
    def __init__(self, filename, repeats):
        self.filename = filename + '.txt'
        self.repeats = repeats
        self.func = None
        self.args = None
        self.kwargs = None
        self.result = None

    def __call__(self, func):
        def inner(*args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs
            self.test()

            return self.func(*args, **kwargs)

        return inner

    def test(self):
        stmt = lambda: self.func(*self.args, **self.kwargs)
        self.result = timeit(stmt=stmt, number=self.repeats)
        with open(self.filename, 'a') as file:
            file.write(f'{self.func.__name__} : {self.repeats} times\t\t'+'{0:.20f}'.format(self.result)+'\n')


@Chronometric('my_funct', 2)
def my_funct():
    for i in range(1_000_000):
        print(i * 2)


my_funct()
