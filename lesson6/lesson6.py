# lecture code #

# class UserSeq:
#     """
#     pass
#     """
#     def __init__(self, number):
#         self.number = number
#
#     def __len__(self):
#         """
#         «Магический» метод, который Магический» метод, который возвращает длину последовательности
#         :param self:
#         :return:
#         """
#         return self.number
#
#     def __getitem__(self, index):
#         """
#         «Магический» метод, который Магический» метод, который перегружает получение элемента по индексу
#         :param index: int (must be int | slice)
#         :return:
#         """
#         if index < self.number:
#             return index ** 2
#         raise IndexError
#
#
# my_seq = UserSeq(10)
# for i in my_seq:
#     print(i)
#
# print(len(my_seq))


class Student:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Group:
    def __init__(self):
        self.__students = []

    def __str__(self):
        return '\n'.join(map(str, self.__students))

    def add_student(self, student: Student):
        self.__students.append(student)

    def __iter__(self):
        return GroupIter(self.__students)

    # def __len__(self):
    #     return len(self.__students)
    #
    # def __getitem__(self, index):
    #     if isinstance(index, int):
    #         return self.__students[index]
    #     if isinstance(index, slice):
    #         result = []
    #         start = index.start or 0
    #         stop = index.stop or len(self)
    #         step = index.step or 1
    #
    #         for i in range(start, stop, step):
    #             result.append(self.__students[i])
    #
    #         return result
    #
    #     raise TypeError


class GroupIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]

        raise StopIteration



st_1 = Student('John')
st_2 = Student('Mary')
st_3 = Student('Max')

gr = Group()
gr.add_student(st_1)
gr.add_student(st_2)
gr.add_student(st_3)

for student in gr:
    print(student)
# print('\n')
# tmp = gr[::1]
# print(tmp)
# print('\n')

