class PrimeNumbers:
    """
    PrimeNumbers
    """
    def __init__(self, num: int):
        """
        :param num:
        """
        if not isinstance(num, int):
            raise TypeError('num must be an integer')

        if num < 1:
            raise ValueError('num must be greater than 0')

        self.__prime_numbers_list = []
        self.__get_prime_numbers_list(num)

    def __get_prime_numbers_list(self, num: int):
        """
        :param num:
        :return:
        """
        for i in range(1, num + 1):
            if i == 1:
                self.__prime_numbers_list.append(i)
            elif i == 2:
                self.__prime_numbers_list.append(i)
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
                    self.__prime_numbers_list.append(i)

    def __len__(self):
        """
        :return:
        """
        return len(self.__prime_numbers_list)

    def __getitem__(self, index: int | slice):
        """
        :param index:
        :return:
        """
        if not isinstance(index, (slice, int)):
            raise TypeError('index must be an integer or slice')

        return self.__prime_numbers_list[index]

    def __str__(self):
        """
        :return:
        """
        return '['+", ".join(map(str, self.__prime_numbers_list))+']'


if __name__ == '__main__':
    a = PrimeNumbers(100)
    print(a)
