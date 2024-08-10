def my_generator(first: int, count: int, predicate):
    for i in range(first, count + 1):
        if predicate(i):
            stopper = yield i
            if stopper:
                break


my_result = my_generator(1, 500, lambda x: x % 17 == 0)
try:
    for i in my_result:
        print(i, end='  ')
        if i > 300:
            my_result.send('d')
except StopIteration:
    pass

