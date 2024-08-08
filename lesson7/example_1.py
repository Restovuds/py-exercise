import random
import timeit



time_1 = """
with open('test.txt', 'r') as f:
    res = 0
    for line in f:
        res += int(line.strip())
"""

time_2 = """
with open('test.txt', 'r') as f:
    res = (int(line.strip()) for line in f)
    res = sum(res)
"""

print(timeit.timeit(time_1, number=1000))
print(timeit.timeit(time_2, number=1000))
