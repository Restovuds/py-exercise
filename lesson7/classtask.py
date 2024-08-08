def prime_gen(my_num):
    for i in range(1, my_num + 1):
        if i == 1:
            yield i
        elif i == 2:
            yield i
        elif i % 2 == 0 and i != 2:
            continue
        else:
            counter = 1
            for n in range(i, 2, -1):
                if i % n == 0:
                    counter += 1
                if counter > 2:
                    break
            if counter == 2:
                yield i
    return


a = 100
# for i in prime_gen(a):
#     print(i)

x = list(prime_gen(a))
print(x)

