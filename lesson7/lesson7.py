# lesson code #

def func(start, stop):
    return [i for i in range(start, stop)]


def gen_funk(start, stop):
    index = start
    while index <= stop:
        yield index
        index += 1


x = func(10, 20)
print(x)


y = gen_funk(10, 20)
print(y)

for item in y:
    print(item)
