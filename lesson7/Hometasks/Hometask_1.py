def gen_geometry(n, limit):
    res = n
    for i in range(limit):
        if i != 0:
            res = res * n
            command = yield res
            if command:
                return None


x = gen_geometry(5, 1000)
try:
    for item in x:
        print(item)
        if item > 1000:
            x.send('stop')
except StopIteration:
    pass
