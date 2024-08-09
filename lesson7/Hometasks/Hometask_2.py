def my_range(*args: int | tuple):
    """
    param args: int or tuple \n
    :using 1 param, only finish, start = 0, step = 1 \n
    :using 2 params, start and finish, step = 1 \n
    :using 3 params, start, finish and step \n

    start must be less than finish
    """

    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    elif len(args) == 0:
        raise ValueError("min 1 arg")
    else:
        raise ValueError("max 3 args")

    if not isinstance(start, int):
        raise TypeError('start must be an integer')
    if not isinstance(stop, int):
        raise TypeError('stop must be an integer')
    if not isinstance(step, int):
        raise TypeError('step must be an integer')

    if step == 0:
        raise ValueError("step must be >0 or <0")
    elif step > 0 and start > stop:
        raise ValueError("start must be less than stop while step greater than 0")
    elif step < 0 and start < stop:
        raise ValueError("start must be greater than stop while step less than 0")

    if start < stop:
        while start < stop:
            yield start
            start += step
    elif start > stop:
        while start > stop:
            yield start
            start += step
    elif start == stop:
        yield start


if __name__ == '__main__':
    for i in my_range(1, 1):
        print(i)
