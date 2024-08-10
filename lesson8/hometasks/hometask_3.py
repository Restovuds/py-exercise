import random


def user_function(n: int) -> float:
    return n * 1.1


def my_sum(l: list, func) -> float:
    usum = sum(map(func, l))
    return usum


user_list = [random.randint(1, 100) for _ in range(30)]
print(user_list)
print(my_sum(user_list, user_function))
