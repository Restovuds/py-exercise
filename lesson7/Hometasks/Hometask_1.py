def gen_geometry(n, limit):
    res = n
    for i in range(limit):
        if i != 0:
            res = res * n
            yield res


x = gen_geometry(5, 100)
for i in x:
    print(i)
    # if i > 100_000_000:
    #     x.close()
