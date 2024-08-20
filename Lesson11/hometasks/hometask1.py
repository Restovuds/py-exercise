"""
1) Создайте ABC класс с абстрактным методом проверки целого числа на
простоту. Т.е., если параметром этого метода является целое число и оно
простое, то метод должен вернуть True, а в противном случае False.

2) Создайте класс его наследующий.

3) Создайте класс, который не наследует пользовательский ABC класс, но
обладает нужным методом. Зарегистрируйте его в качестве виртуального
подкласса.

4) Проверьте работоспособность проекта.
"""

import abc


class PrimeNumCheckABC(abc.ABC):
    @abc.abstractmethod
    def is_prime(self, num: int) -> bool:
        pass


class PrimeNumCheck():
    def is_prime(self, num: int) -> bool:
        prime_nums = []
        for i in range(1, num + 1):
            if i == 1:
                prime_nums.append(i)
            elif i == 2:
                prime_nums.append(i)
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
                    prime_nums.append(i)

        if num in prime_nums:
            return True
        return False

PrimeNumCheckABC.register(PrimeNumCheck)
my_prime_num = PrimeNumCheck()
print(my_prime_num.is_prime(11))
