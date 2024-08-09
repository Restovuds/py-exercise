def my_range(*args: int | tuple):
    """
    param args: int or tuple \n
    :1_param,  only finish, start = 0, step = 1 \n
    :2_params,  start and finish, step = 1 \n
    :3_params, start, finish and step \n

    start must be less than finish
    """

    ranger = {
        'start': 0,
        'stop': 0,
        'step': 1
    }

    if len(args) == 1:
        ranger['stop'] = args[0]

    if len(args) == 2:
        ranger['start'] = args[0]
        ranger['stop'] = args[1]

    if len(args) == 3:
        ranger['start'] = args[0]
        ranger['stop'] = args[1]
        ranger['step'] = args[2]

    if ranger['stop'] < ranger['start']:
        raise ValueError("Start value must be less than stop value")

    j = ranger['start']
    while j < ranger['stop']:
        yield j
        j += ranger['step']


user_range = my_range()
if __name__ == '__main__':
    for i in user_range:
        print(i)
