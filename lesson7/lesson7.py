# lesson code #

def func(start, stop):
    return [i for i in range(start, stop)]


def gen_funk(start, stop):
    index = start
    while index <= stop:
        yield index
        index += 1


# x = func(10, 20)
# print(x)


# y = gen_funk(10, 20)
# print(y)

# for item in y:
#     print(item)

#####################################

# generator OBJECT >
# z = (i * i for i in range(10))


# print(z)  # generator OBJECT >
# print([i for i in z])

#####################################

def square_gen(n):
    i = 0
    exponent = 2
    while i < n:
        temp_exponent = (yield i ** exponent)
        if temp_exponent:
            exponent = temp_exponent
        i += 1


l = square_gen(20)
for i in l:
    print(i)
    if i > 100:
        l.send(3)
